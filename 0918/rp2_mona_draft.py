from pathlib import Path

from PIL import Image, ImageDraw


SOURCE_GIF = Path("0918/rp2_mona.gif")
MONA_PATH = Path("0918/mona.jpg")
OUT_PATH = Path("0918/rp2_mona_draft.gif")

S = 400
HALF_SIDE = S / 2
MARGIN = 40
CANVAS = S + 2 * MARGIN
BORDER = 3
SPRITE_HEIGHT = 150


def load_sprite():
    if MONA_PATH.exists():
        mona = Image.open(MONA_PATH).convert("RGBA")
        width = round(mona.width * SPRITE_HEIGHT / mona.height)
        return mona.resize((width, SPRITE_HEIGHT), Image.Resampling.LANCZOS)

    # The original source image is not currently in the repository.  Recover the
    # unobstructed 100-by-150 sprite from frame 20 of the existing animation so
    # this draft changes only the quotient geometry, not the artwork.
    old_animation = Image.open(SOURCE_GIF)
    old_animation.seek(20)
    old_frame = old_animation.convert("RGBA")
    return old_frame.crop((158, 65, 258, 215))


sprite = load_sprite()
sprite_reflected = sprite.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
half_sprite_width = sprite.width / 2


def to_px(x, y):
    return MARGIN + x + HALF_SIDE, MARGIN + HALF_SIDE - y


square_clip = Image.new("L", (CANVAS, CANVAS), 0)
ImageDraw.Draw(square_clip).rectangle(
    [MARGIN, MARGIN, MARGIN + S, MARGIN + S],
    fill=255,
)


def arrow(draw, point, direction, color, size=14):
    px, py = point
    dx, dy = direction
    draw.line(
        [px - dx * size, py - dy * size, px + dx * size, py + dy * size],
        fill=color,
        width=3,
    )
    tip = px + dx * size, py + dy * size
    left = tip[0] - dy * 6 - dx * 8, tip[1] + dx * 6 - dy * 8
    right = tip[0] + dy * 6 - dx * 8, tip[1] - dx * 6 - dy * 8
    draw.polygon([tip, left, right], fill=color)


def draw_fundamental_square(draw):
    upper_left = to_px(-HALF_SIDE, HALF_SIDE)
    lower_right = to_px(HALF_SIDE, -HALF_SIDE)
    draw.rectangle([upper_left, lower_right], outline="black", width=BORDER)

    red = (180, 0, 0, 255)
    green = (0, 140, 0, 255)

    # (HALF_SIDE, y) ~ (-HALF_SIDE, -y)
    arrow(draw, to_px(HALF_SIDE, S / 4), (0, -1), red)
    arrow(draw, to_px(-HALF_SIDE, -S / 4), (0, 1), red)

    # (x, HALF_SIDE) ~ (-x, -HALF_SIDE)
    arrow(draw, to_px(S / 4, HALF_SIDE), (-1, 0), green)
    arrow(draw, to_px(-S / 4, -HALF_SIDE), (1, 0), green)


def render(x, y, reflected):
    canvas = Image.new("RGBA", (CANVAS, CANVAS), "white")
    layer = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))

    def paste(center_x, center_y, use_reflection):
        image = sprite_reflected if use_reflection else sprite
        px, py = to_px(center_x, center_y)
        layer.alpha_composite(
            image,
            (round(px - image.width / 2), round(py - image.height / 2)),
        )

    paste(x, y, reflected)

    # Extend the moving rectangle through the quotient seam.  Across either
    # vertical edge, the correct local continuation is
    #
    #     (X, Y) -> (X - S, -Y)    at the right edge,
    #     (X, Y) -> (X + S, -Y)    at the left edge.
    #
    # Thus the copy is translated by S in x and reflected in y.  Replacing x
    # by -x would reverse the motion and is not the quotient transition map.
    if x + half_sprite_width > HALF_SIDE:
        paste(x - S, -y, not reflected)
    if x - half_sprite_width < -HALF_SIDE:
        paste(x + S, -y, not reflected)

    red, green, blue, alpha = layer.split()
    clipped_alpha = Image.composite(
        alpha,
        Image.new("L", alpha.size, 0),
        square_clip,
    )
    layer = Image.merge("RGBA", (red, green, blue, clipped_alpha))

    canvas.alpha_composite(layer)
    draw_fundamental_square(ImageDraw.Draw(canvas))
    return canvas.convert("RGB")


frames = []
velocity = 8
x = -HALF_SIDE + velocity
y = S / 4
reflected = False

# Each 50-frame crossing applies (x, y) -> (x - S, -y) and reverses the
# portrait vertically.  Two crossings restore both y and the orientation, so
# 100 frames form a seamless loop representing the nontrivial class squared.
for _ in range(100):
    frames.append(render(x, y, reflected))
    x += velocity
    if x > HALF_SIDE:
        x -= S
        y = -y
        reflected = not reflected

frames[0].save(
    OUT_PATH,
    save_all=True,
    append_images=frames[1:],
    duration=45,
    loop=0,
    disposal=2,
)
print(f"wrote {OUT_PATH} with {len(frames)} frames")
