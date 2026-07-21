# Meeting Transcript Style Guide

## Core Standard

The finished text should read like a professional Chinese meeting memo reconstructed from the live discussion, not like a rough transcript and not like a short summary.

If the user sends the transcript in multiple messages, the final memo should read as one continuous reconstructed meeting record rather than several separately polished fragments.

Priorities in order:

1. Information completeness
2. Data accuracy
3. Logical order
4. Written language quality
5. Readability
6. Summary clarity

## What to Keep

Always keep:

- All important numbers and time expressions
- Management views, operating changes, guidance, and caveats
- Reasons, conditions, assumptions, and comparisons
- Any statement that affects investment understanding, operating judgment, or business interpretation
- All substantive content unless the user explicitly asks for deletion or compression

## What to Clean Up

Usually remove or rewrite:

- “就是”“然后”“那个”“其实”“大概是这样”之类口头填充
- Broken starts and repeated fragments
- Redundant self-corrections when the intended meaning is clear
- Speaker tags such as “董事长：”“分析师：”
- Stray spaces introduced by speech-to-text cleanup or formatting drift

## Proper Nouns and Terminology

When speech-to-text likely misrecognizes a proper noun:

- Check the company's official name first
- Then check brand names, products, subsidiaries, project names, and industry terms
- Prefer conservative correction
- If two interpretations are both plausible and cannot be verified, avoid over-correcting

Examples:

- `恒力十话` should likely become `恒力石化`
- `德州一体化` may need correction based on the company's actual project naming

## Q&A Formatting Example

```text
【Q&A主题：需求恢复节奏】
Q：管理层如何看待下半年需求恢复节奏，以及订单改善何时能够体现到出货端？
A：管理层表示，当前订单恢复仍是结构性的，不同行业节奏不同；消费电子相关需求改善更快，工业端仍需观察。若按目前在手订单看，改善会先体现在排产和稼动率，再逐步传导至收入和利润端。
```

## Topic Shift Example

```text
【资本开支与产能规划】
公司表示，明年的资本开支将更聚焦于已落地项目的完善和配套环节，而不是大规模新增扩产；现阶段更关注项目达产、成本优化和客户导入。
```

## Sentence Pattern Guidance

Prefer:

- Short declarative sentences
- One paragraph for one theme
- Ordered items when there are parallel points
- Semicolons for tightly related parallel statements

Good pattern:

```text
公司表示，今年利润改善主要来自三点：①原材料价格回落；②高附加值产品占比提升；③费用控制更加严格。
```

Avoid:

- Long spoken run-on sentences
- Excessive literal transcript order when the logic can be made clearer
- Turning the text into abstract bullet-point summaries that lose detail

## Data Handling Rules

When dealing with data:

- Preserve the original unit
- Preserve whether the comparison is同比、环比、累计或绝对值
- Do not “round” casually
- Do not replace vague source wording with fake precision
- Recheck dates, months, percentages, capacity figures, and currency amounts
- Do not insert commas inside numbers by default; prefer `10000` over `10,000`

## Spacing Rules

- Remove stray spaces in Chinese text
- Do not leave unnecessary spaces between Chinese and English
- Do not leave unnecessary spaces around punctuation
- Before final delivery, scan once specifically for formatting artifacts caused by editing

## Summary Rules

After the full memo, provide a concise key-points section:

- Use several major points, each with several short sub-points
- Cover the most important business, operating, financial, project, demand, and guidance information
- Keep wording tight and clear
- Do not omit a major theme that appears repeatedly in the transcript
- Do not let the summary become longer than the full memo section

Example:

```text
【要点总结】
一、经营表现
1. 本期经营改善主要来自产品结构优化和成本回落。
2. 下半年利润弹性仍取决于需求恢复节奏和价格传导。

二、产能与项目
1. 新项目推进仍按既定节奏进行，但投放更强调稳妥。
2. 管理层更关注达产、客户导入和投资回报，而非激进扩产。
```

## Proper-Noun Safety Check

Before final delivery, explicitly verify:

- Whether any company name,品牌名,产品名,子公司名,项目名 was changed
- Whether that change is supported by the transcript context or reliable company information
- Whether any industry term or financial term was accidentally rewritten into a wrong term

If uncertain, use the safer wording and avoid over-correction.

## Final Self-Check

Ask:

- Did I integrate every transcript chunk the user sent?
- Did I preserve every material data point?
- Did I preserve every important causal link?
- Did I avoid deleting or over-compressing any substantive content on my own?
- Did I remove stray spaces and avoid comma-separated number formatting?
- Did I avoid unauthorized or incorrect changes to professional terms?
- Did I verify corrected proper nouns carefully?
- Did I label each Q&A pair clearly?
- Did I add headings only where they help?
- Does the output read like polished Chinese meeting minutes rather than a transcript?
