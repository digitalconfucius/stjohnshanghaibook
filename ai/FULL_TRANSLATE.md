# Full Book Translation Plan — `full/full.md` → `full/full-cn.md`

## Overview

This document describes the plan for translating `full/full.md` (the complete book
*Blessed John the Wonderworker*) into Simplified Chinese as `full/full-cn.md`.

**Key optimization**: Part III of `full/full.md` (the "A Record Book of Blessed
John's Intercessions" section) is **SKIPPED** during translation because it has
already been translated as `miracles/miracles-cn.md`. The final output is
produced by appending `miracles/miracles-cn.md` verbatim to the end of the
translated non-miracles chunks.

This saves tokens by not re-translating ~1,448 lines of Part III content in
`full/full.md`, and also avoids ever reading the full contents of
`miracles/miracles-cn.md` or `full/full.md` into the main conversation — only
minimal boundary reconnaissance was performed.

## Source File Structure (discovered via Grep, not full reads)

`full/full.md` is **2,654 lines** total. Structure:

| Line range  | Content                                                          |
| ----------- | ---------------------------------------------------------------- |
| 1–28        | Front matter: title, copyright, ISBN, Contents heading           |
| 29          | `# PART I: MATERIALS ON THE LIFE OF BLESSED JOHN` (top-level)    |
| 29–41       | Part I TOC entries (listed as plain numbered items, not `##`)    |
| 42          | `# PART II: A PICTORIAL BIOGRAPHY 181` (still TOC)               |
| 42–50+      | Part II + Part III TOC entries                                   |
| ~51–673     | Part I narrative: Life of Blessed John, Vita Prima, Childhood, Bitol Seminary, Shanghai, Victim of Envy, Apostle to the West, Netherlands, Death of a Saint, Sepulchre |
| 674–966     | 19 personal testimonies with `## N.` headers (numbers 1–30, scrambled and non-sequential due to OCR; titles like "My First Meeting", "Spiritual Vigilance", "Deliverance From Death", etc.) — note these are **biographical testimonies** about meeting/knowing Vladika John, NOT the Part III miracle accounts |
| 967–1097    | Closing narrative of Part I: Death of Saint, Sepulchre description |
| 1098        | `# Part III` (OCR artifact stray header — belongs mid-sentence with "of this book" on line 1100) |
| 1102        | `# Part II: A Pictorial Biography` (the ACTUAL Part II header, out of order due to OCR) |
| 1102–1206   | Part II: Pictorial Biography — photo captions and picture descriptions |
| **1207**    | `# Part III: A F Blessed John's Intercessions` (START of miracles) |
| **1207–2654** | **Part III miracles — SKIPPED. Use `miracles/miracles-cn.md`.** |

Verification: `miracles/miracles.md` line 1 is `# Part III: A Record Book of
Blessed John's Intercessions` and its Editor's Preface, §1, §1 content, and
Epilogue all match `full/full.md` lines 1207–2654. The content is the same
(though `full/full.md` has more whitespace and OCR line-wrapping artifacts);
`miracles/miracles-cn.md` is a complete Chinese translation of exactly this
range and can be appended as-is.

## Chunking Plan (11 chunks)

Content to translate = lines 1–1206 of `full/full.md` (1,206 lines).
Partitioned into 11 chunks aligned with natural section boundaries where
available (the `## N.` testimonial headers at lines 674, 721, 729, 742, 753,
771, 783, 799, 811, 815, 824, 840, 858, 891, 904, 911, 934, 958, 967).

| Chunk | Source line range | Approximate content                                                  | Output file                           | Status    |
| ----- | ----------------- | -------------------------------------------------------------------- | ------------------------------------- | --------- |
| 01    | 1–120             | Front matter + Part I header + Part I TOC + start of Life narrative  | `ai/chunks/full/chunk-01.md`          | pending   |
| 02    | 121–240           | Part I: Vita Prima / Childhood                                       | `ai/chunks/full/chunk-02.md`          | pending   |
| 03    | 241–360           | Part I: Bitol Seminary, Yugoslavia years                             | `ai/chunks/full/chunk-03.md`          | pending   |
| 04    | 361–480           | Part I: Shanghai wonderworker (early)                                | `ai/chunks/full/chunk-04.md`          | pending   |
| 05    | 481–600           | Part I: Shanghai (continued), Victim of Envy                         | `ai/chunks/full/chunk-05.md`          | pending   |
| 06    | 601–673           | Part I: Apostle to the West + transition into testimonies            | `ai/chunks/full/chunk-06.md`          | pending   |
| 07    | 674–770           | Testimonies: ## 1 (My First Meeting) through ## 11                   | `ai/chunks/full/chunk-07.md`          | pending   |
| 08    | 771–857           | Testimonies: ## 12 (Holy Water) through ## 19 (My Brother George)    | `ai/chunks/full/chunk-08.md`          | pending   |
| 09    | 858–966           | Testimonies: ## 20 (Nameday Gift) through ## 29 (Removal of Wart)    | `ai/chunks/full/chunk-09.md`          | pending   |
| 10    | 967–1097          | ## 30 (Healing from Cancer), Death of Saint, Sepulchre description   | `ai/chunks/full/chunk-10.md`          | pending   |
| 11    | 1098–1206         | Part II: Pictorial Biography captions and photo descriptions         | `ai/chunks/full/chunk-11.md`          | pending   |
| ---   | **1207–2654**     | **SKIPPED — covered by `miracles/miracles-cn.md`**                   | (N/A)                                 | skipped   |

Chunks 01–06 cover ~120 lines each (Part I has no `##` header structure to
align on, so these are arbitrary boundaries — agents should handle mid-paragraph
content at chunk boundaries). Chunks 07–09 align on `## N.` testimonial
section boundaries. Chunk 10 covers the natural ending of Part I. Chunk 11 is
Part II (pictorial biography).

## Translation Guidelines (same as miracles phase)

- **Output**: Simplified Chinese (简体中文)
- **Vocabulary**: Draw from `wikipedia/stjohnwiki-cn.txt` and use the same
  conventions established for miracles (see `ai/INSTRUCTIONS.md`). Key terms
  must be consistent with the already-produced `miracles/miracles-cn.md`:
  - 圣伊望 (St. John) — NEVER 约翰
  - 弗拉迪卡 (Vladika) as transliteration
  - 总主教 / 主教 / 都主教 (Archbishop / Bishop / Metropolitan)
  - 司祭 / 辅祭 / 修士司祭 / 修士大司祭 (priest / deacon / hieromonk / archimandrite)
  - 神圣礼仪 / 圣体血 (Divine Liturgy / Holy Communion)
  - 圣髑 / 灵迹 / 神迹 / 苦行僧 / 显行灵迹者 (relics / miracle / ascetic / wonderworker)
  - 法衣 / 主教冠 / 修士帽 (vestments / mitre / klobuk)
  - 安息追思 / 帕尼希达 (panikhida)
  - 库尔斯克之根·符印之母 (Kursk Root Icon)
  - 罪人之保障圣母主教座堂 (Surety of Sinners Cathedral, Shanghai)
  - 众哀伤者之欢乐圣母主教座堂 (Joy of All Who Sorrow Cathedral, San Francisco)
  - 俄罗斯正教会域外教会 (ROCOR)
- **Orthodox Christian bias** — do NOT censor, simplify, or soften content
- **OCR artifacts**: Use best judgment to resolve scrambled clauses, dropped
  words, stray running headers/page numbers, and mid-paragraph line breaks
- **Preserve** `#` and `##` header structure in Chinese. OCR artifacts where
  headers got pushed inline should be rendered as `###` subheadings
- **Bible quotations** in classical/Orthodox Chinese Bible style

## Final Output Assembly

After all 11 chunks are marked completed, assemble `full/full-cn.md` by:

1. Concatenating `ai/chunks/full/chunk-01.md` through `ai/chunks/full/chunk-11.md`
   in order (produces the Chinese for lines 1–1206 of `full/full.md`)
2. Appending `miracles/miracles-cn.md` verbatim (the Chinese for Part III
   lines 1207–2654 — already complete)

This can be done with a single shell command:

```bash
cat ai/chunks/full/chunk-01.md ai/chunks/full/chunk-02.md \
    ai/chunks/full/chunk-03.md ai/chunks/full/chunk-04.md \
    ai/chunks/full/chunk-05.md ai/chunks/full/chunk-06.md \
    ai/chunks/full/chunk-07.md ai/chunks/full/chunk-08.md \
    ai/chunks/full/chunk-09.md ai/chunks/full/chunk-10.md \
    ai/chunks/full/chunk-11.md miracles/miracles-cn.md \
    > full/full-cn.md
```

Note: `miracles/miracles-cn.md` starts with `# 第三部分：圣伊望代祷事迹纪录`
(the Chinese for "Part III: A Record Book of Blessed John's Intercessions"),
so it slots in naturally as the Part III section of `full-cn.md`.

**DO NOT read the contents of `miracles/miracles-cn.md` into the conversation**
— simply concatenate it at the shell level. It has already been translated and
verified in the miracles phase.

## Resumability

If this session is interrupted:

1. Check `ai/progress_log.md` for the current status of each chunk.
2. Chunks marked `completed` have output files in `ai/chunks/full/chunk-NN.md`.
3. Dispatch new translation agents only for chunks still marked `pending`.
4. After all 11 chunks are `completed`, run the concatenation step above.
5. Update `ai/progress_log.md` to mark the full translation project as completed.

## Token Economy

This plan specifically avoids:

- **Reading all of `full/full.md`** into the conversation — only ~80 lines of
  boundary reconnaissance were read (lines 1–50, 669–680, 963–975, 1093–1112,
  1200–1229). Grep was used to discover all `#` and `##` headers.
- **Reading `miracles/miracles-cn.md`** into the conversation at all — it is
  simply appended via shell concatenation.
- **Re-translating Part III** of `full/full.md` (~1,448 lines of OCR-noisy
  English) — this content is already translated as `miracles/miracles-cn.md`.

Each translation chunk is dispatched to a subagent with only the specific line
range it needs to process, keeping the main conversation context small.
