# Translation Project Instructions

## Project Overview
This is a project to translate the old book *Blessed John the Wonderworker* (about St. John of Shanghai and San Francisco) from English into **Simplified Chinese (简体中文)**.

## Source Files
- `miracles/miracles.md` — main source text for the miracles section (Part III: A Record Book of Blessed John's Intercessions)
- `full/full.md` — the full book (later phase)

## Output Files
- `miracles/miracles-cn.md` — Chinese translation of the miracles section
- (later) `full/full-cn.md` — Chinese translation of the full book

## Translation Approach
1. Work in **parallel** using subagents on **header-separated chunks** (`#` and `##` headings).
2. Each chunk is translated independently and written to its own file under `ai/chunks/<source>/`.
3. After all chunks are translated, concatenate them into the final output file in section order.
4. The input text may contain OCR garble or artifacts — use best judgment to resolve them while preserving meaning.

## Translation Guidelines
- **Audience**: Orthodox Christian Chinese-speaking readers.
- **Bias**: This is an Orthodox Christian writing with an Orthodox Christian bias. **Do NOT censor, simplify, or alter the essence** of the original text. Translate faithfully but articulate it in a way appropriate for an Orthodox Christian Chinese reader.
- **Vocabulary**: Draw Orthodox terminology from `wikipedia/stjohnwiki-cn.txt` (the Chinese Wikipedia entry on St. John of Shanghai). Key terms include:
  - 圣伊望 / 伊望 (St. John / John — *NOT* 约翰, which is the Protestant rendering)
  - 主教 (Bishop), 总主教 (Archbishop), 都主教 (Metropolitan)
  - 罪人之保障圣母主教座堂 (Surety of Sinners Cathedral, Shanghai)
  - 众哀伤者之欢乐圣母主教座堂 (Joy of All Who Sorrow Cathedral, San Francisco)
  - 俄罗斯正教会域外教会 (Russian Orthodox Church Outside of Russia / ROCOR)
  - 中华正教会 (Chinese Orthodox Church)
  - 神职人员 (clergy), 司祭 (priest), 辅祭 (deacon)
  - 圣餐礼 / 圣体血 (Holy Communion / Holy Mysteries)
  - 圣髑 (relics), 灵迹 / 神迹 (miracles), 苦行僧 (ascetic)
  - 显行灵迹者 (wonderworker)
  - 法衣 (vestments), 主教座 (episcopal see)
  - 修士司祭 (hieromonk), 修士大司祭 (archimandrite)
  - 安息追思 (panikhida — memorial service for the departed)
  - 库尔斯克之根·符印之母 (Kursk Root Icon of the Mother of God)
  - 上海 (Shanghai), 旧金山 (San Francisco)
- **Names**: Use the Chinese conventions found in the wikipedia source. For names not covered there, transliterate phonetically using standard Chinese conventions.
- **Bible quotations**: Render Scripture quotations in a style consistent with Orthodox/classical Chinese Bible tradition where possible.
- **Tone**: Reverent, faithful, and accessible to a contemporary Chinese Orthodox reader.

## Process / Resumability
- Progress is tracked in `ai/progress_log.md`. Update it as chunks are completed so the work can resume incrementally even if a session ends.
- Chunk outputs are saved in `ai/chunks/miracles/` (or `ai/chunks/full/`) by chunk number.
- After all chunks are confirmed translated, the final output file is produced by concatenation in correct section order.

## Current Phase
Begin with `miracles/miracles.md` → output `miracles/miracles-cn.md`.
