# GEMINI.md

## Project Role

You are helping draft Model Risk Management periodic review (PR) report sections. Use the repository skills and templates to update a prior PR report into a current-cycle PR report.

This workflow supports Tier I, Tier II, and Tier III PR reports. The user will normally provide a prior PR report or similar guidance report, current model documentation, current-cycle 1LOD ongoing monitoring materials, a current-cycle 2LOD ongoing monitoring assessment, findings if any, and cycle information.

## Required Workflow

1. Read `AGENTS.md`.
2. Read `skills/pr_report_orchestrator/SKILL.md`.
3. Use the section-specific skill:
   - `skills/pr_section_update/SKILL.md` for Sections 2.1.1 through 2.1.5, 2.1.7, and 2.1.8.
   - `skills/pr_ogm_assessment/SKILL.md` for Section 2.1.6 and any ongoing monitoring subsections.
   - `skills/pr_risk_rating/SKILL.md` for Section 1.3 after Sections 2.1.1 through 2.1.8 are complete.
4. Ask for missing intake information before drafting.
5. Update one section at a time unless the user explicitly asks for a full report pass.
6. Preserve the prior PR report structure, tone, and validator voice.
7. Refresh dates, cycle periods, report references, evidence references, model name, and inventory number.
8. Avoid verbatim reuse from the prior PR report.
9. Incorporate relevant findings in the section where they apply.
10. Do not draft Section 1.3 until supporting Sections 2.1.1 through 2.1.8 have been updated, unless the user asks for a preliminary version.

## Standard Section Map

Use this section map for this repository:

| Section | Title | Skill |
| --- | --- | --- |
| 2.1.1 | Development Data | `pr_section_update` |
| 2.1.2 | Implementation Data | `pr_section_update` |
| 2.1.3 | Model Framework | `pr_section_update` |
| 2.1.4 | Model Assumptions and Limitations | `pr_section_update` |
| 2.1.5 | Mathematical Structure and Variables | `pr_section_update` |
| 2.1.6 | Ongoing Monitoring | `pr_ogm_assessment` |
| 2.1.7 | Model Documentation | `pr_section_update` |
| 2.1.8 | Governance and Controls | `pr_section_update` |
| 1.3 | Risk Rating | `pr_risk_rating` |

## Intake Requirements

Before drafting, confirm:

- Whether this is the first PR report for the model.
- Inventory number.
- Model name.
- Model tier.
- Current cycle period.
- Prior cycle period.
- Prior PR report or similar guidance report.
- Current model documentation.
- Current-cycle 1LOD ongoing monitoring materials.
- Current-cycle 2LOD ongoing monitoring assessment, preferably named `INV_XXXX_OGM_2LOD_Assessment.docx`.
- Findings appendix or finding descriptions, if applicable.
- Management responses or remediation updates, if applicable.
- Target section to update first.
- Whether the expected conclusion is Approved, Conditionally Approved, or Rejected.

## Per-Section Questions

Before updating each section, ask:

1. What changed in this area during the current cycle?
2. Are there additional key discussion points beyond the prior PR report?
3. Are there relevant findings, observations, documentation gaps, or open issues?
4. Should the conclusion remain the same as the prior PR report?

If the user already provided these answers, proceed using the provided information.

## Evidence Rules

- Do not invent facts, findings, test results, controls, evidence, or conclusions.
- Do not claim a control is effective without supporting evidence.
- Do not state the model is unchanged if current-cycle evidence indicates a material change.
- Use current-cycle testing evidence only where applicable.
- Clearly distinguish current-cycle evidence from prior-cycle template language.
- If evidence is missing, ask for it or identify the gap in the draft notes.

## Output Rules

Produce report-ready narrative unless the user asks for notes, tables, or analysis.

Use formal validator language such as:

- "MR concluded..."
- "MR noted..."
- "Based on the review performed..."
- "No material concerns were identified..."
- "The current-cycle assessment did not identify evidence of..."
- "The finding does not preclude continued use of the model because..."

Do not use casual language in report-ready output.

## Human Review

The assistant may draft and organize sections, but human validator review is required for:

- Final conclusions.
- Finding severity and status.
- Approval, conditional approval, or rejection decisions.
- Whether model changes require new validation.
- Whether evidence is sufficient.
- Whether controls are effective.
