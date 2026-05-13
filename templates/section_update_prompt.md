# Section Update Prompt

Use this prompt for Sections 2.1.1 through 2.1.5, 2.1.7, and 2.1.8.

```text
Read GEMINI.md, AGENTS.md, and skills/pr_section_update/SKILL.md.

I am updating Section [SECTION NUMBER] [SECTION TITLE] for inventory [INVENTORY NUMBER], [MODEL NAME].

Use the following materials:
- Intake file: [INTAKE FILE PATH]
- Prior PR report or prior section text: [PRIOR PR PATH OR TEXT]
- Current model documentation: [MODEL DOCUMENTATION PATH]
- Current-cycle evidence relevant to this section: [EVIDENCE PATHS]
- Findings, if any: [FINDINGS PATH OR SUMMARY]

Before drafting, confirm whether you have enough information on:
1. What changed in this area during the current cycle.
2. Additional key discussion points beyond the prior PR report.
3. Relevant findings, observations, documentation gaps, or open issues.
4. Whether the conclusion should remain the same as the prior PR.

Then draft report-ready language for Section [SECTION NUMBER] in formal validator voice.

Requirements:
- Preserve the prior report structure, tone, and validator voice.
- Refresh dates, cycle periods, evidence references, model name, and inventory number.
- Avoid verbatim reuse from the prior PR report.
- Incorporate relevant findings where applicable.
- Do not invent evidence, findings, test results, controls, or conclusions.
- End with a clear conclusion sentence.
```
