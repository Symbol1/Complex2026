# 給 AI 助理

- 使用者同時使用 ChatGPT 與 Claude，兩者都必須讀這份 `AGENTS.md`；不要建立或改用 `CLAUDE.md`。
- 想保存記憶（使用者的偏好、糾正，以及之後都要遵守的規則）時，直接寫進這份 `AGENTS.md` 的對應段落，不要只存在單一工具自己的記憶或 `CLAUDE.md` 裡，這樣 ChatGPT 與 Claude 都讀得到。

# 環境

- SageMath 裝在 `~/miniforge3/envs/sage`，不在 `PATH` 上：執行 Sage 用 `~/miniforge3/envs/sage/bin/sage`，執行講義用同一個環境的 `jupyter`（`sagemath` kernel 也在這裡）。驗證 Sage 程式碼時直接用它跑，不要因為 `which sage` 找不到就略過。

# Complex2026 課程進度與待補主題

- 截至 2026-10-16，講義進度約到 residue theorem（*Complex Variables and Applications* 第 6.5 節、*Advanced Engineering Mathematics* 第 19.5 節）。稽核講義是否遺漏 PDF 內容時，只比較已經到達的課程進度；不把 residue theorem 之後的內容或 conformal mappings 等後半學期主題列為缺漏。進度往後推進時，再更新此截止點。
- 已寫入 `1030.ipynb`（期中考後的第一次上課，尚未上課）：harmonic functions、Laplace's equation、harmonic conjugates、正交 level curves，以及 maximum-modulus principle（含 minimum-modulus 版本與 harmonic functions 的 maximum principle）。
- 依照上述截止點，目前確認待補的主題為：
  - 一般複數 $n$ 次方根、root mappings 與 branch 的選擇。
  - 系統性討論區域在 $z^n$、$z^{1/n}$ 與 $1/z$ 之下的 images 與 preimages。
  - 複變函數極限、極限運算律與用不同路徑判定極限不存在。
  - 一般複數冪 $z^\alpha$、$z^w$ 及其 branches。
  - inverse trigonometric functions 與 inverse hyperbolic functions。
  - Morera's theorem。
  - 不額外假設 $f'$ 連續的 Cauchy–Goursat theorem 證明；現有講義只給了依賴 Green's theorem 的版本。

# Notebook 格式

- 講義直接呈現整理後的知識，而不需要糾正 prompt 因為 prompt 寫太快本來就很容易錯。任何需要釐清 prompter 的用詞或觀念時，在 chat 中說明，不寫進講義。例如直接介紹螢光讀取，不加上「不宜直接稱為『化學放光』」之類的話。
- 中文排版請依照 [中文文案排版指北（GitHub README）](https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.md)。
- 數學符號與公式在中英文混排時也視為英文，適用相同的空格與標點規則：與中文字之間加空格，與全形標點之間不加空格。例如 `當 $p$ 很小時`、`若 $d = 4$，則能更正 1 個錯誤`、`距離（$d$）`。
- 講義中的英文散文請依照 AMS Style Guide（AMSSG）的規範書寫，不只限於引號規則。例如採用邏輯引號（logical quotation）：句尾標點（句號、逗號等）若不屬於被引用的文字本身，應放在右引號之外，如 `the term "bounded"` 而非 `"bounded."`；只有標點本身就是引文的一部分時才放在引號內。
- 建立或修改 `.ipynb` 講義時，每個 section title（包含各級 Markdown 標題 `#` 至 `######`）必須獨立放在一個 Markdown cell；內文、公式、表格、圖片與其他標題應放在其他 cells。
- cell 大概十行，這是為了 jk 翻 cell 的時候不要一次捲動太多
- Sage 程式碼的 cell 語言標記使用 `python`，以顯示語法配色；每個 code cell 的 `metadata.vscode.languageId` 與 notebook 的 `metadata.language_info.name` 都設為 `python`，不可設為 `sage`。執行核心仍使用 SageMath，保留 `metadata.kernelspec` 的 SageMath 設定。儲存後檢查所有 code cells，避免編輯器留下 `languageId: sage`。
- LaTeX 原始碼要加上適當空格，讓公式容易閱讀：二元運算子與關係符號（如 `+`、`-`、`=`、`\in`、`\le`）兩側留空格，逗號後留空格。例如 `s_b(t) = A\cos(2\pi f_ct + \pi b),\qquad b \in \{0, 1\}`。上下標內例外，見下一條。
- 上標與下標（`_{...}`、`^{...}`）內的原始碼不加空格：TeX 排版上下標時本來就省略運算子、關係符號與逗號周圍的間距，原始碼也比照呈現效果。例如寫 `a_{n+1}`、`(z - a)^{n+1}`、`\sum_{n=0}^\infty`、`\oint_{|z-a|=r}`、`\sum_{n\ge1}`、`\lim_{z\to a}`，不寫 `a_{n + 1}`、`\sum_{n = 0}`、`\oint_{|z - a| = r}`、`\sum_{n \ge 1}`。`\ge`、`\to` 等控制序列前面不加空格；後面只在接字母時保留一個空格，因為 TeX 需要它來結束控制序列名稱（如 `\to a`、`\ge N`）；接數字或其他符號時不加（如 `\ge1`、`\to0`、`\to\infty`）。`\text{...}` 內的文字照常空格。上下標以外的部分仍依上一條加空格。
- 行內公式與前後文字的間距依上述混排規則處理；`$` 與公式內容之間不加空格。
- 展示公式 `$$ ... $$` 前後的空行依 TeX 的段落語意處理：空行代表換段，不是單純增加視覺留白。公式延續前文時，前文與公式之間不加空行；後文延續同一段時，公式與後文之間也不加空行。上下都有空行會讓公式獨立成段，通常不合講述脈絡，因此不要慣例性地在兩側都加空行；只在語意確實換段時留空行。
- 同一段落內要換行時（結尾加兩個空格的 Markdown 換行），依優先順序選擇斷點：句號後幾乎都要換行（`\allowbreak[4]` 的感覺）；分號後盡量換行（`\allowbreak[3]`），除非分號後的子句太短；非列舉用途的逗號（如 `Because A, so B` 這種連接子句而非列舉項目的逗號）也是很好的斷點，因為這類句子通常很長；行內公式 `$...$` 的開頭與結尾同樣是很好的斷點。
- 對 LaTeX 空格的詳細用法有疑問時，參照既有 `.ipynb` 講義與使用者已調整的公式格式。但既有原始碼可能有使用者沒注意到的不一致，不能當作規範的依據，也不要從既有寫法反推出新慣例。新寫的內容依 AGENTS.md 的規則；發現既有寫法與規則衝突，或遇到規則沒涵蓋的情況時，在 chat 中向使用者提出（指出位置與兩種寫法），由使用者決定。
- 同時存在三門課的講義 ~/Correct2026, ~/Complex2026, ~/Differ2026，請互相參考
  - 互相參考只限於格式與排版慣例。三門是不同的課，學生不一定同時修，所以每門課的講義都要自成一體：不要引用其他課的內容，也不要假設學生學過（例如 Differ2026 的 exact equation、closed form 或 winding number 作業）；需要的概念在本課講義中自行定義。本課較早的講義則可以沿用。
- 英文標題大小寫依層級統一：`# GOOD JOB`（全大寫）、`## Good Job`（Title Case）、`### Good job`（Sentence case，以下層級亦同）。Title Case 的冠詞、連接詞與介系詞通常小寫，標題開頭、結尾或冒號後開頭除外；Sentence case 保留專有名詞與縮寫的慣用大小寫。數學公式、程式碼與連結網址保持原樣。
- LaTeX 數字的千分位分隔符號使用 `{,}`，括號內不加空格，例如 `201{,}000`；一般列舉項目或參數之間的逗號仍依原規則在逗號後留空格。
- 新建 `.ipynb` 講義時，先加入兩個佔位的作業 section，依序為 `## Homework Due <Today+4>` 與 `## Homework Due <Today+7>`，之後再補上實際題目內容。
- 新寫的教學內容放進當天（或下一次上課）的講義，不要回頭加進已經上過的講義，即使主題上更貼近舊講義；使用者要求把內容從舊講義移出時則照做。講義檔名是上課日期（例如 `1002.ipynb`），以今天的日期判斷是哪一份；提到舊講義中的圖時，寫成 from the previous lecture 這類說法。
