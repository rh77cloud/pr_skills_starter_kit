# Risk Rating Prompt

Use this prompt after Sections 2.1.1 through 2.1.8 have been updated.

```text
Read GEMINI.md, AGENTS.md, and skills/pr_risk_rating/SKILL.md.

I am updating Section 1.3 Risk Rating for inventory [INVENTORY NUMBER], [MODEL NAME].

Use the following materials:
- Intake file: [INTAKE FILE PATH]
- Prior PR Section 1.3 text: [PRIOR RISK RATING PATH OR TEXT]
- Updated Sections 2.1.1 through 2.1.8: [UPDATED SECTIONS PATH]
- Findings, if any: [FINDINGS PATH OR SUMMARY]
- Management responses or remediation updates, if applicable: [MANAGEMENT RESPONSE PATH]

Before drafting, confirm:
1. Whether the conclusion is Approved, Conditionally Approved, or Rejected.
2. Whether the conclusion is the same as the prior PR.
3. Whether there are current-cycle findings.
4. Whether any findings affect continued model use or require conditional approval.
5. Whether prior findings should be discussed as closed, repeated, or still open.
6. Whether Section 2.1.6 is complete and ready to summarize.

Then draft report-ready Section 1.3 language.

Requirements:
- Summarize Sections 2.1.1 through 2.1.8 without introducing new evidence.
- Emphasize ongoing monitoring results and 2LOD assessment.
- Incorporate findings in the relevant paragraph.
- Explain why the final conclusion is appropriate.
- Do not contradict supporting sections.
```
