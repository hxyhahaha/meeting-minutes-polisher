---
name: meeting-minutes-polisher
description: Use when the user pastes one or more blocks of company meeting speech-to-text text across multiple messages and wants them rewritten into a faithful, structured, more written Chinese meeting memo, followed by a concise key-points summary and a final Word document. This skill preserves key logic and all important facts while improving grammar, wording, topic structure, Q&A labeling, company and product names, and readability. It is especially appropriate when the user provides a company name together with a large pasted transcript delivered in several chunks and asks for a polished Chinese meeting note without losing numbers, dates, timelines, scale, or material statements.
---

# Meeting Minutes Polisher

## Overview

Use this skill when the user directly pastes one or more long blocks of raw meeting speech-to-text text, possibly across multiple messages, and wants them rewritten into a readable Chinese meeting memo that feels like the live discussion has been faithfully restored in a more written and organized form.

The goal is not summarization. The goal is full-information reconstruction: improve order, grammar, terminology, and structure without dropping any important content. After the full memo is finished, also provide a short, clear key-points section organized as several major points containing several sub-points, and generate a Word file for delivery.

## Required Input

The minimum required input is:

- Company name
- One or more pasted blocks of raw meeting transcript or speech-to-text text

If the company, brand, product, business line, or acronym is likely to be error-prone, first use the company name to verify core proper nouns from official company materials or other reliable materials provided by the user. If no reliable source is available, make only conservative corrections.

The user should paste transcript content directly into the conversation. Do not assume there is an attachment, link, file, or external source unless the user explicitly provides one.

The user may continue sending additional transcript chunks in later messages. Treat all pasted chunks in the same thread as parts of the same source material unless the user clearly starts a new task.

## Multi-Message Intake

When the transcript arrives in several messages:

- Keep accumulating the pasted transcript mentally across turns.
- Do not rewrite prematurely after the first chunk if the user is clearly still sending more.
- If the user indicates `继续`、`还有`、`下一段`、`先收着` or similar, continue absorbing the content and wait.
- If the user indicates `整理一下`、`开始整理`、`输出纪要`、`可以了` or similar, then rewrite the full accumulated transcript into one integrated memo.
- Once the user has indicated the transcript is complete, produce the full memo first, then a concise key-points summary, then save the result as a Word document.
- If the boundary is unclear, make the conservative assumption that the user may still be pasting more content and respond briefly instead of producing a premature final memo.

## Workflow

### 1. Build Context First

Before rewriting:

- Merge all transcript chunks already provided in the current thread into one working source text in chronological order.
- Identify the company name, meeting type, and whether the text contains management remarks, analyst Q&A, or mixed discussion.
- Scan the full transcript once to identify topic shifts, repeated points, broken sentences, and probable speech-to-text errors.
- Verify obvious company-specific proper nouns when possible, especially company name, brands, products, business segments, plant names, customer names, and commonly confused homophones.
- If the user provides internal samples, prior memos, or公众号文章, read those first and align tone to that house style.

### 2. Preserve Information Rigorously

Do not omit material information. Preserve:

- Core logic and causal relationships
- Numbers, ratios, prices, dates, months, years, time ranges, production capacity, shipment scale, order size, utilization, margins, and other operating data
- Management judgment, uncertainty, constraints, timing, and comparisons
- Important qualifiers such as “大概”“同比”“环比”“阶段性”“目前”“明年”等

This is a rewrite task, not a compression task. You may merge duplicate filler wording, but you must not remove unique facts, logic, or data points.

Do not delete, compress, or simplify content on your own initiative. Any cleanup must preserve the full substance of the original discussion.

### 3. Rewrite into Written Chinese

Rewrite the transcript into concise written Chinese:

- Remove口语化表达, redundant hesitations, false starts, and repeated fillers.
- Correct sentence grammar and reorder clauses when needed for readability.
- Prefer short sentences.
- Use书面语 instead of spoken phrasing.
- Do not add interpretation that is not supported by the transcript.
- Do not invent missing subjects, numbers, dates, or conclusions.

Formatting normalization:

- Remove speaker names and speaker labels.
- Do not leave unexplained or stray spaces anywhere in the output.
- Do not leave spaces between Chinese and English.
- Do not insert thousands separators or other commas inside numbers unless the source itself requires that exact format; default to plain digits such as `1000000` rather than `1,000,000`.
- Convert month expressions to Arabic numerals where appropriate, such as “March” to “3月”.
- Keep product names, model names, and financial units in their correct form.

### 4. Structure the Memo

Organize the output so it is easy to read without losing content:

- When the discussion shifts to a new non-Q&A topic, add a short thematic subheading on its own line before that section.
- When one paragraph contains multiple parallel points, split them into ordered items such as `①…；②…；③…` when that improves clarity.
- Use semicolons, short paragraphs, and parentheses naturally.
- Keep the tone close to a sell-side or institutional deep-dive memo: dense in information, clear in logic, and economical in wording.

### 5. Handle Q&A Explicitly

When the transcript enters a Q&A exchange:

- Add one topic line before the question-answer pair summarizing the theme of that pair.
- Prefix the question with `Q：`
- Prefix the answer with `A：`
- Remove speaker names.
- Preserve all important detail in both the question and the answer.

If one question triggers a long answer with several sub-points, keep them organized within the same `A：` block rather than splitting the pair apart.

### 6. Validate Before Finalizing

Before returning the rewritten memo, check:

- All transcript chunks provided by the user have been incorporated
- No important statement has been dropped
- No content has been deleted, over-compressed, or simplified without basis
- All numbers and time references are preserved and not accidentally changed
- No number has been reformatted with commas or other unnecessary separators
- Obvious speech-to-text mistakes in company, brand, and product names have been corrected conservatively
- No professional term, brand name, product name, subsidiary name, project name, or financial term has been casually rewritten into a wrong term
- Topic headings match the content that follows
- Q&A pairs are correctly labeled and grouped
- The final text is fully in written Chinese style, has no unnecessary speaker traces, and contains no stray spaces

If a number or proper noun remains uncertain after checking, preserve the most defensible wording and avoid aggressive normalization.

Perform an explicit self-check before delivery:

- Compare the final memo against the accumulated source text and confirm no material point is missing
- Confirm that no passage was deleted merely for brevity
- Re-scan every number, date, month, percentage, production capacity, shipment figure, price, and margin reference
- Re-scan the final text for stray spaces and comma-separated numbers
- Re-scan all proper nouns that were corrected and confirm the correction is defensible
- If any correction is uncertain, revert to the safer wording rather than forcing a possibly wrong normalization

### 7. Produce Key Points

After the full memo, produce a concise key-points section.

Requirements:

- Organize it as several major points, each containing several short sub-points
- Prioritize the most decision-relevant information
- Keep it concise and clear
- Do not introduce information that does not appear in the transcript
- Do not let the summary replace the full memo; it is a supplement after the full reconstructed minutes

Recommended pattern:

- `一、经营与业绩`
- `1. ……`
- `2. ……`
- `二、产能与项目`
- `1. ……`
- `2. ……`

### 8. Generate a Word File

After the memo and key-points section are complete, generate a `.docx` file containing:

- Title with company name
- Full reconstructed meeting memo
- Key-points summary at the end

Default file naming:

- `{公司名称}会议纪要.docx`

If the user provides another file name, follow the user's preference.

Use the bundled script at `scripts/export_minutes_to_docx.py` when a Word file needs to be created.

## Output Rules

Return the rewritten memo and key-points section unless the user explicitly asks for commentary about the editing process.

Default output expectations:

- No speaker names
- No meta explanation of what was changed
- No bullet list of editing notes
- No summary that replaces the full content
- No missing data, dates, scale, or logic
- No stray spaces and no comma-separated numbers
- A concise key-points section after the full memo
- A generated Word file unless the user explicitly says not to create one

## Output Pattern

Use this pattern unless the user requests another format:

```text
【会议纪要】

【主题一】
正文……

【主题二】
①……；②……；③……

【Q&A主题：……】
Q：……
A：……

【Q&A主题：……】
Q：……
A：……

【要点总结】
一、……
1. ……
2. ……
二、……
1. ……
2. ……
```

Subheadings should be short and informative. Prefer business themes such as `产能投放`、`价格走势`、`海外订单`、`资本开支`、`盈利展望` rather than vague labels.

## Reference

For formatting detail and rewrite examples, see [references/style-guide.md](references/style-guide.md).
