# 給 AI 助理

- 使用者同時使用 ChatGPT 與 Claude，兩者都必須讀這份 `AGENTS.md`；不要建立或改用 `CLAUDE.md`。
- 想保存記憶（使用者的偏好、糾正，以及之後都要遵守的規則）時，直接寫進這份 `AGENTS.md` 的對應段落，不要只存在單一工具自己的記憶或 `CLAUDE.md` 裡，這樣 ChatGPT 與 Claude 都讀得到。
- 使用者用注音輸入法，有時忘記切換，訊息會變成按鍵本身的「火星文」，例如 `su3cl3`（ㄋㄧˇ ㄏㄠˇ，你好）、`ji394su3`（ㄨㄛˇ ㄞˋ ㄋㄧˇ，我愛你）、`hk4g4`（ㄘㄜˋ ㄕˋ，測試）。看到英文字母夾著 `3`、`4`、`6`、`7` 或 `,`、`.`、`/`、`;` 的怪字串時，不要當成亂碼或英文縮寫：先依下面的大千式鍵位轉回注音（`3`、`4`、`6`、`7` 與空白是聲調，也是字與字的分界），再大致轉成漢語拼音，用讀音猜意思。猜不準時，在 chat 中說出猜測並向使用者確認。

  ```text
  1ㄅ 2ㄉ 3ˇ 4ˋ 5ㄓ 6ˊ 7˙ 8ㄚ 9ㄞ 0ㄢ -ㄦ
  qㄆ wㄊ eㄍ rㄐ tㄔ yㄗ uㄧ iㄛ oㄟ pㄣ
  aㄇ sㄋ dㄎ fㄑ gㄕ hㄘ jㄨ kㄜ lㄠ ;ㄤ
  zㄈ xㄌ cㄏ vㄒ bㄖ nㄙ mㄩ ,ㄝ .ㄡ /ㄥ
  ```

# 環境

- SageMath 裝在 `~/miniforge3/envs/sage`，不在 `PATH` 上：執行 Sage 用 `~/miniforge3/envs/sage/bin/sage`，執行講義用同一個環境的 `jupyter`（`sagemath` kernel 也在這裡）。驗證 Sage 程式碼時直接用它跑，不要因為 `which sage` 找不到就略過。

# Complex2026 課程進度與待補主題

- 截至 2026-10-16，講義進度約到 residue theorem（*Complex Variables and Applications* 第 6.5 節、*Advanced Engineering Mathematics* 第 19.5 節）。稽核講義是否遺漏 PDF 內容時，只比較已經到達的課程進度；不把 residue theorem 之後的內容或 conformal mappings 等後半學期主題列為缺漏。進度往後推進時，再更新此截止點。
- 已寫入 `1030.ipynb`（期中考後的第一次上課，尚未上課）：複變函數極限與極限運算律、用不同路徑判定極限不存在、一般複數 $n$ 次方根、$z^n$、$z^{1/n}$、$1/z$ 之下的 images 與 preimages、root branches、一般複數冪 $z^\alpha$ 與 $z^w$、inverse trigonometric functions、inverse hyperbolic functions、不額外假設 $f'$ 連續的 Cauchy–Goursat theorem 證明、Morera's theorem、harmonic functions、Laplace's equation、harmonic conjugates、正交 level curves、maximum-modulus principle（含 minimum-modulus 版本與 harmonic functions 的 maximum principle）。
- 依照上述截止點，目前已確認的講義缺漏均已補入 `1030.ipynb`；後續稽核仍只比較已經到達的課程進度。

# 考卷

- 考卷用 LaTeX（xelatex）出，格式沿用 `~/Correct2026/1013/1013midmock.tex`：題目卷加答案卷，`\end{document}` 之後放依講義日期分類的題庫。檔案放在以日期命名的資料夾，後綴是 `midmock`（模擬考）與 `midtrue`（正式考），例如 `1018/1018midmock.tex`、`1030/1030midtrue.tex`（這門課星期五上課）；`.tex` 含答案註解，已在 `.gitignore` 排除，只有 PDF 進 git。編譯時一律加 `-synctex=1`（`xelatex -synctex=1 ...`），使用者需要 SyncTeX 在 PDF 與原始碼之間跳轉。正式考卷在考完之前，整個資料夾先加進 `.gitignore`（例如 `1030/`），PDF 也不進 git。
- 考卷的數學內容只用英文；考試規則、學號雜湊（salt）、是非題的作答方式（答 $q_j$ 或 $9 - q_j$）、計分方式這類 logistics 則中英並行，先英文、再中文，兩者之間不要換段（原始碼中不要空行）。學號的指示尤其重要。是非題（第一組 bomb）之後一律只用英文，不再寫任何中文，連作圖位置之類的作答說明也一樣；唯一的例外是之後再用 $q_j$ 保護的題組，「答 $q_j$ 或 $9 - q_j$」的作答說明仍要中英並行。中文保留課堂上用的英文術語（holomorphic、branch cut、winding number 等），比照 Correct2026 考卷的中文寫法。
- 考卷用 A3 列印（版面仍是 A4，列印時放大），所以作圖題一個題號只放一張圖，同一張圖上要做的幾件事（例如拆 loops 與標 winding number）在說明裡各算一分，不拆成兩個題號。
- 要學生在答案卷上作圖的題目，答案卷上的底圖用點線（dotted），也不要畫出要學生自己標記的資訊（例如方向箭頭）；題目卷上的圖照常用實線並給出完整資訊。
- 本班考試不開放使用計算機（包括 991），題目要能徒手算出精確答案，不出需要容許誤差或科學記號的數值題。
- 數字不要直接取自講義的例題或作業；同一個概念要換成新的函數或數值。
- 多出依學號變化的題目。模擬考（1018midmock）用學號最後兩碼：$p$ 是倒數第二碼、$q$ 是最後一碼、$N = 10p + q$（研究生學號倒數第三碼可能是字母，所以不用末三碼）。正式考（從 1030midtrue 起）在題目卷開頭多一題：把學號去掉字母當作十進制數，乘以 $1002003 = 10^6 + 2 \times 10^3 + 3$（徒手容易算）再模 $10^8$，在答案卷上寫成八位數（不足往前補零），由左到右記作 $q_1q_2\dotsm q_8$。
- 正式考中每個依學號變化的題目（或共用說明的 bomb）各自隨機選一或兩位 $q_k$，相鄰題目不共用同一位，兩位的組合也不重複。乘以 $1002003$ 時，同一班（學號只差最後三碼）內 $q_3$、$q_6$ 只有約兩種值、$q_5$ 約五種，所以單一位數的參數只用 $q_1$、$q_2$、$q_4$、$q_7$、$q_8$，也不用 $(q_1, q_3)$、$(q_1, q_6)$、$(q_3, q_6)$、$(q_5, q_8)$ 這幾組相關的兩位。
- 每個參數從 0 到 9 都要能做、答案要能用公式寫在註解裡讓助教對照。每個 bomb（是非題、計算、圍道積分等連續小題組）至少要有一題依學號變化；模擬考不必，沒有依學號變化不影響練習的本質。用兩位時盡量用和或差混合（如 $q_i + q_j$、$q_i - q_j$），避免難度只跟單一位有關；需要避開零或邊界時可加小位移，例如 $q_i - q_j - \frac13$。需要 0–9 單一數字的題目（例如圖上的標號）直接用單一位 $q_k$，不用 $|q_i - q_j|$，因為差的絕對值分布不均（0 有 10 組、9 只有 2 組）。
- 考卷的 LaTeX 不用 `\left` / `\right`，改用固定大小的 `\Bigl` / `\Bigr`（或 `\bigl` / `\bigr`）。
- 考卷行內公式一律不用 `\frac`、`\dfrac`（尤其分母有 $q_j$ 之類的上下標時更不行），改寫成 `(...)/(...)` 或負次方：$-1$ 次方一律寫成斜線，例如 `$z^2/(z^2 + 9)$`、`$e^{ikz}/(z^2 + 4)$`、`$\sin(1/z)$`；其他負次方可以保留，例如 `$z^{-10q_7-q_8}\sin z$`，但同一個分母同時有 $-1$ 與其他次方時合併成一個斜線，例如 `$e^z/z^2(z - 2)$`。並列的乘法比斜線先算，所以分母是並列的乘積時不加括號：寫 `$1/AB$`、`$1/nP_n$`、`$e^z/z^2(z - 2)$`，不寫 `$1/(AB)$`、`$e^z/\bigl(z^2(z - 2)\bigr)$`；分母本身有 `+`、`-` 時才需要括號，例如 `$1/(z + 1)$`。問 Laurent series 某一項（例如 $(z - n)^{-1}$ 的係數）時照常寫負次方。避免一列題目太擠；展示公式可以用 `\frac`。
- 每題只問一個答案；需要兩個量時（例如圓的圓心與半徑）拆成兩題，各一分。
- 題目中的人名用台灣各大學正式英文校名裡的羅馬拼音（不用漢語拼音），格式比照 HsinPo：每個音節首字母大寫、直接連寫，不加空格或連字號。例如 TsingHua（清華）、ChiaoTung（交通）、ChengKung（成功）、ChengChi（政治）、ChungHsing（中興）、ChungCheng（中正）、YangMing（陽明）、ChangGung（長庚）、ChungYuan（中原）、SooChow（東吳）、FuJen（輔仁）、TamKang（淡江）、FengChia（逢甲）、YuanZe（元智）、TungHai（東海）、DongHwa（東華）、ChiNan（暨南）、MingChuan（銘傳）、ShihHsin（世新）。正式英文名不是羅馬拼音的學校（例如中央 Central、師大 Normal）或會變成真人名字的（中山 Sun Yat-sen）不用；題目要像 Correct2026 那樣讓人名參與情境（某人宣稱、計算、展開），不要只是掛名。bomb（連續小題組）的說明不需要人名。（Correct2026 的人名是晶片製造商，這門課沒有晶片。）
- 用到 $\operatorname{Log}$、$\operatorname{Arg}$ 時，考卷要明確寫出主值與 branch cut：$\operatorname{Arg}z \in (-\pi, \pi]$，branch cut 在負實軸。寫在用到的大題說明裡，不寫在考卷開頭；同理，圍道方向（counterclockwise）也寫在大題說明或題目本身，不寫在開頭。
- 期中考範圍以講義中的 `midterm cutting line` 為界；residue 本身在截止線之後，但用 residue 想法（Cauchy integral formula、Laurent 係數 $a_{-1}$）算的圍道積分可以出，題目中不出現 residue 一詞。
- 正式考 `1030/1030midtrue.tex` 要控制在 90 題。使用者說要從中刪掉的題目，連同答案註解與用到的圖檔移到 `1029/1029midmock2.tex`，當作第二次模擬考（2026-10-19 那週颱風假）。兩份都重新編譯；使用者說的題號以最新編譯的 PDF 為準。

# Notebook 格式

- 講義直接呈現整理後的知識，而不需要糾正 prompt 因為 prompt 寫太快本來就很容易錯。任何需要釐清 prompter 的用詞或觀念時，在 chat 中說明，不寫進講義。例如直接介紹螢光讀取，不加上「不宜直接稱為『化學放光』」之類的話。
- 中文排版請依照 [中文文案排版指北（GitHub README）](https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.md)。
- 中文的並列項目，要用頓號就全部用頓號（`BEC、BSC、AWGN`），要用連接詞就全部用連接詞（`BEC 或 BSC 或 AWGN`），不要混用。用逗號或分號隔開的並列項目也一樣，不要只在最後一項之前加連接詞（如 `，以及`、`；或`）。英文列舉「前面用逗號、最後一項前加 and 或 or」的文法不適用於中文，不論有沒有 Oxford comma 都不要套用：不寫 `BEC、BSC 或 AWGN`，也不寫 `BEC、BSC、或 AWGN`。
- 矩陣方向一律使用英文 `row` 與 `column`，不使用中文對應詞，以避免地域用法歧義。
- 數學符號與公式在中英文混排時也視為英文，適用相同的空格與標點規則：與中文字之間加空格，與全形標點之間不加空格。例如 `當 $p$ 很小時`、`若 $d = 4$，則能更正 1 個錯誤`、`距離（$d$）`。
- 講義中的英文散文請依照 AMS Style Guide（AMSSG）的規範書寫，不只限於引號規則。例如採用邏輯引號（logical quotation）：句尾標點（句號、逗號等）若不屬於被引用的文字本身，應放在右引號之外，如 `the term "bounded"` 而非 `"bounded."`；只有標點本身就是引文的一部分時才放在引號內。
- 建立或修改 `.ipynb` 講義時，每個 section title（包含各級 Markdown 標題 `#` 至 `######`）必須獨立放在一個 Markdown cell；內文、公式、表格、圖片、其他標題應放在其他 cells。
- 每個 cell 的內容不得有 leading empty line 或 trailing empty line；分段所需的空白行只保留在 cell 內容中間。
- cell 大概十行，這是為了 jk 翻 cell 的時候不要一次捲動太多
- 講義用到的照片與圖檔（板書照片、截圖等）放在以講義日期命名的資料夾（例如 `1012/`），檔名用簡短的英文名稱（小寫、以 `-` 連接），描述圖中畫了什麼，或補充、說明了什麼，例如 `0923/ball-leaves-hilltop-anytime.png`、`0930/two-paths-around-small-rectangle.png`。不要用 `image-1.png`、`IMG_1924.jpeg` 這類流水號，也不要加 `-board`、`-annotated` 這類只說明圖片形式的字尾。檔名會出現在講義原始碼、`git log`、`ls` 中，alt text 只有渲染後才看得到。改名時一併更新講義中的連結。照片保留拍攝時的完整解析度，不要另存縮小的複本。格式要能在 VS Code 與 GitHub 上直接顯示（JPEG、PNG、WebP）；iPhone 的 HEIC 先轉成同解析度的 JPEG 再放進資料夾。同一張照片在 repo 中只留一份。
- Markdown 內文按句子分行，讓每個句子在呈現時也另起一行；同一段落內使用行尾兩個空格加換行，不只在原始碼中換行。長句可依語意在子句之間分行，參照使用者既有排版。空行只用於真正換段，公式前後仍遵循下述 TeX 段落規則。
- Sage 程式碼的 cell 語言標記使用 `python`，以顯示語法配色；每個 code cell 的 `metadata.vscode.languageId` 與 notebook 的 `metadata.language_info.name` 都設為 `python`，不可設為 `sage`。執行核心仍使用 SageMath，保留 `metadata.kernelspec` 的 SageMath 設定。儲存後檢查所有 code cells，避免編輯器留下 `languageId: sage`。
  - **不要再把語法配色改成 sage。** 缺少 `metadata.vscode.languageId` 同樣算違規：VS Code 會退回 kernelspec 的 `"language": "sage"`，結果語法配色消失。因此每個 code cell（包含新增的 cell）都必須明確寫上 `"metadata": {"vscode": {"languageId": "python"}}`。
  - 不要修改 `metadata.kernelspec`（保留 `"language": "sage"`、`"name": "sagemath"`），也不要把 `language_info.name` 改成 `sage`。
  - 每次編輯 `.ipynb` 後都要跑一次檢查，確認所有 code cells 的 `languageId` 都是 `python`，缺漏或為 `sage` 就立即補正。
- LaTeX 原始碼要加上適當空格，讓公式容易閱讀：二元運算子與關係符號（如 `+`、`-`、`=`、`\in`、`\le`）兩側留空格，逗號後留空格。例如 `s_b(t) = A\cos(2\pi f_ct + \pi b),\qquad b \in \{0, 1\}`。上下標內例外，見下一條。
- 上標與下標（`_{...}`、`^{...}`）內的原始碼不加空格：TeX 排版上下標時本來就省略運算子、關係符號、逗號周圍的間距，原始碼也比照呈現效果。例如寫 `a_{n+1}`、`(z - a)^{n+1}`、`\sum_{n=0}^\infty`、`\oint_{|z-a|=r}`、`\sum_{n\ge1}`、`\lim_{z\to a}`，不寫 `a_{n + 1}`、`\sum_{n = 0}`、`\oint_{|z - a| = r}`、`\sum_{n \ge 1}`。`\ge`、`\to` 等控制序列前面不加空格；後面只在接字母時保留一個空格，因為 TeX 需要它來結束控制序列名稱（如 `\to a`、`\ge N`）；接數字或其他符號時不加（如 `\ge1`、`\to0`、`\to\infty`）。`\text{...}` 內的文字照常空格。上下標內也不加 `\,` 等間距指令，例如寫 `q^{\max(u-d+1,0)}`。積分的微分符號前的 `\,` 不受這項規則限制，例如 `e^{-\int P\,dx}`。上下標裡並列兩組條件時，用 `\ ` 隔開比較好讀，例如 `_{1\le i\le n,\ 0\le j\le n-k-1}`。上下標以外的部分仍依上一條加空格。
- 行內公式與前後文字的間距依上述混排規則處理；`$` 與公式內容之間不加空格。
- 函數的冪次寫在引數之後，此時引數加括號：`\sin(\pi t)^3`、`\cos(\theta)^2`，不寫成 `\sin^3(\pi t)`、`\cos^2\theta`。指數是對函數值取冪，不是函數名的一部分。
- 除此之外，函數引數**只在會被誤讀時**才加括號，不要一律加。後面緊接另一個因式或上標時加：`\cos(a) I`、`\sin(\pi t)^3`、`\ln(3/2)`、`\sin(x)\cos(x)`。後面是關係符、運算子、逗號、`\frac` 之類的群組邊界或行尾時不加，因為那些本來就分隔得很清楚：`\ln2 \approx 6.93`、`\frac{\ln2}{0.005}`、`$\sin x$`、`\sin y = 0`、`\ln|y|`。
- 算子與其作用對象之間、以及帶有上下標的因式之間，在原始碼留一個空格：`T_a y`、`D y`、`D T_a y`、`P(D) y`、`e^{-ia} z`、`\frac{a^2 D^2}{2!}`。純量並列不加空格，例如 `cy`、`iy'`、`Ce^{rt}`。函數值與其後因式之間同樣留一個空格：`\cos(a) I + \sin(a) D`，不寫成 `\cos a\,I + \sin a\,D`。
- 展示公式 `$$ ... $$` 前後的空行依 TeX 的段落語意處理：空行代表換段，不是單純增加視覺留白。公式延續前文時，前文與公式之間不加空行；後文延續同一段時，公式與後文之間也不加空行。上下都有空行會讓公式獨立成段，通常不合講述脈絡，因此不要慣例性地在兩側都加空行；只在語意確實換段時留空行。
- 同一段落內要換行時（結尾加兩個空格的 Markdown 換行），依優先順序選擇斷點：句號後幾乎都要換行（`\allowbreak[4]` 的感覺）；分號後盡量換行（`\allowbreak[3]`），除非分號後的子句太短；非列舉用途的逗號（如 `Because A, so B` 這種連接子句而非列舉項目的逗號）也是很好的斷點，因為這類句子通常很長；行內公式 `$...$` 的開頭與結尾同樣是很好的斷點。
- 對 LaTeX 空格的詳細用法有疑問時，參照既有 `.ipynb` 講義與使用者已調整的公式格式。但既有原始碼可能有使用者沒注意到的不一致，不能當作規範的依據，也不要從既有寫法反推出新慣例。新寫的內容依 AGENTS.md 的規則；發現既有寫法與規則衝突，或遇到規則沒涵蓋的情況時，在 chat 中向使用者提出（指出位置與兩種寫法），由使用者決定。
- 同時存在三門課的講義 ~/Correct2026, ~/Complex2026, ~/Differ2026，請互相參考，尤其是互相參考對方的 AGENTS.md
  - 互相參考只限於格式與排版慣例。三門是不同的課，學生不一定同時修，所以每門課的講義都要自成一體：不要引用其他課的內容，也不要假設學生學過（例如 Differ2026 的 exact equation、closed form 或 winding number 作業）；需要的概念在本課講義中自行定義。本課較早的講義則可以沿用。
- 英文標題大小寫依層級統一：`# GOOD JOB`（全大寫）、`## Good Job`（Title Case）、`### Good job`（Sentence case，以下層級亦同）。Title Case 的冠詞、連接詞、介系詞通常小寫，標題開頭、結尾、冒號後開頭除外；Sentence case 保留專有名詞與縮寫的慣用大小寫。數學公式、程式碼、連結網址保持原樣。
- LaTeX 數字的千分位分隔符號使用 `{,}`，括號內不加空格，例如 `201{,}000`；一般列舉項目或參數之間的逗號仍依原規則在逗號後留空格。
- 定義 LaTeX 巨集時使用 `\def`，不使用 `\newcommand` 或 `\renewcommand`，例如 `\def\FF{\mathbb F}`。
- 新建 `.ipynb` 講義時，先加入兩個佔位的作業 section，依序為 `## Homework Due <Today+4>` 與 `## Homework Due <Today+7>`，之後再補上實際題目內容。
- 新寫的教學內容放進當天（或下一次上課）的講義，不要回頭加進已經上過的講義，即使主題上更貼近舊講義；使用者要求把內容從舊講義移出時則照做。講義檔名是上課日期（例如 `1002.ipynb`），以今天的日期判斷是哪一份；提到舊講義中的圖時，寫成 from the previous lecture 這類說法。
