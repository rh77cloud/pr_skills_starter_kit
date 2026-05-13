# Ongoing Monitoring Prompt

Use this prompt for Section 2.1.6 Ongoing Monitoring and its subsections.

```text
Read GEMINI.md, AGENTS.md, and skills/pr_ogm_assessment/SKILL.md.

I am updating Section 2.1.6 Ongoing Monitoring for inventory [INVENTORY NUMBER], [MODEL NAME].

Use the following materials:
- Intake file: [INTAKE FILE PATH]
- Prior PR Section 2.1.6 text: [PRIOR SECTION PATH OR TEXT]
- 1LOD ongoing monitoring package: [1LOD PATH]
- 2LOD ongoing monitoring assessment: [2LOD PATH]
- Findings, if any: [FINDINGS PATH OR SUMMARY]

Before drafting, confirm:
1. Required ongoing monitoring tests in scope.
2. Whether the `INV_XXXX_OGM_2LOD_Assessment.docx` file was provided.
3. Testing period, thresholds, and results.
4. Breaches, exceptions, overrides, output adjustments, or missing tests.
5. Relevant findings or observations.
6. Whether the prior conclusion should remain the same.

Then draft Section 2.1.6 and only create subsections for tests that are actually in scope.

Requirements:
- Use current-cycle monitoring evidence.
- Incorporate both 1LOD results and 2LOD assessment.
- Do not invent tests, thresholds, breaches, or conclusions.
- Discuss exceptions or missing tests if present.
- End with an overall Section 2.1.6 conclusion.
```
