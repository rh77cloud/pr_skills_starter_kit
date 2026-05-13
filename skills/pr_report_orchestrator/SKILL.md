# PR Report Orchestrator Skill

## Purpose

Use this skill to coordinate a periodic review (PR) report update for Model Risk Management reports, especially Tier I, Tier II, and Tier III periodic reviews. The goal is to update a prior PR report into the current-cycle PR report by refreshing cycle dates, evidence, section conclusions, ongoing monitoring assessments, findings, and the final risk rating narrative.

This skill does not replace validator judgment. It structures the workflow, asks for required inputs, preserves validator voice, and routes each report section to the appropriate drafting skill.

## When to Use

Use this skill when the user asks to:

- Update a periodic review report.
- Draft or refresh PR sections 2.1.1 through 2.1.8.
- Convert a prior PR report into a current-cycle PR report.
- Draft the final risk rating section 1.3.
- Use current-cycle ongoing monitoring, documentation, governance, control testing, or findings to update a PR report.

## Required Inputs

Before drafting, determine whether this is the first PR report for the model.

### If this is the first PR report

Request or confirm availability of:

1. A similar model's prior PR report to use as guidance.
2. Current model documentation.
3. Current-cycle 1LOD ongoing monitoring materials.
4. Current-cycle 2LOD ongoing monitoring assessment file, preferably named:
   `INV_XXXX_OGM_2LOD_Assessment.docx`
5. Current-cycle range.
6. Inventory number.
7. Model name.
8. Model tier.
9. Findings appendix or finding descriptions, if any.
10. Prior validation report, if available and useful.

### If this is not the first PR report

Request or confirm availability of:

1. The model's prior PR report to use as the drafting template.
2. Current-cycle range.
3. Current model documentation.
4. Current-cycle 1LOD ongoing monitoring materials.
5. Current-cycle 2LOD ongoing monitoring assessment file, preferably named:
   `INV_XXXX_OGM_2LOD_Assessment.docx`
6. Findings appendix or finding descriptions, if any.
7. Any management responses or remediation updates, if applicable.

## Master Workflow

Follow this workflow.

### Step 1: Intake

Ask the user to provide or confirm:

- Is this the first PR report for the model?
- Inventory number.
- Model name.
- Model tier.
- Current cycle period.
- Prior cycle period.
- Target report section to update first.
- Whether the report conclusion is expected to remain Approved, Conditionally Approved, or Rejected.
- Whether there are current-cycle findings.
- Whether any previous findings remain open, were closed, or are being repeated.

### Step 2: Load and summarize materials

For the prior PR report or similar model PR report:

- Identify the section structure.
- Identify the prior conclusion.
- Identify the validator tone and writing pattern.
- Identify reusable content.
- Identify cycle-specific language that must be refreshed.

For the model documentation:

- Identify model purpose and use.
- Identify model methodology/framework.
- Identify development data.
- Identify implementation data.
- Identify model assumptions and limitations.
- Identify controls and governance.

For 1LOD OGM materials:

- Identify required ongoing monitoring tests.
- Identify test period.
- Identify test results.
- Identify thresholds, breaches, exceptions, overrides, and adjustments.

For 2LOD OGM assessment:

- Identify 2LOD assessment conclusion by test.
- Identify key discussion points.
- Identify concerns, limitations, evidence gaps, or compensating controls.
- Identify which items belong in Section 2.1.6 and which items affect Section 1.3.

For findings:

- Identify finding number, title, severity, status, and related report sections.
- Identify exact language that should be incorporated.
- Do not overstate finding impact beyond evidence.

### Step 3: Update sections one by one

Use `pr_section_update` for Sections 2.1.1 through 2.1.5, 2.1.7, and 2.1.8.

Use `pr_ogm_assessment` for Section 2.1.6 and its subsections.

Use `pr_risk_rating` for Section 1.3 after Sections 2.1.1 through 2.1.8 have been updated.

### Step 4: Apply universal drafting rules

For every section:

- Ask what changed in the current cycle.
- Ask whether there are additional key discussion points beyond the prior PR report.
- Ask whether any finding is relevant.
- If no changes are identified, preserve the prior conclusion but rewrite the language.
- Refresh dates, periods, report references, inventory number, and current-cycle evidence.
- Avoid verbatim reuse while preserving structure, tone, and validator voice.
- Use current-cycle evidence only where applicable.
- Do not invent tests, findings, controls, or conclusions.
- Clearly distinguish unchanged items from newly reviewed current-cycle evidence.
- Maintain professional model-risk validation tone.

## Section Map

Use the following mapping.

### 2.1.1 Development Data

Focus on whether model development data remains representative of the current portfolio and macroeconomic environment, and appropriate for continued use.

### 2.1.2 Implementation Data

Focus on whether implementation data sources and feeds used by the model remain unchanged and appropriate.

### 2.1.3 Model Framework

Focus on whether there are changes requiring validation, expanded model scope, new model uses, or emerging academic/industry concerns.

### 2.1.4 Model Assumptions and Limitations

Focus on whether assumptions remain appropriate and limitations remain mitigated within risk appetite.

### 2.1.5 Mathematical Structure and Variables

Focus on whether mathematical structure, formulas, variables, transformations, segmentation, or calibration mechanics changed.

### 2.1.6 Ongoing Monitoring

Focus on whether the ongoing monitoring plan is documented, commensurate, compliant with standards, and whether performance remains appropriate. This section may require subsections such as:

- 2.1.6.1 Data ongoing monitoring
- 2.1.6.2 Backtesting or snapshot backtesting
- 2.1.6.3 Sensitivity testing
- 2.1.6.4 Benchmarking
- 2.1.6.5 Stability or population monitoring
- 2.1.6.6 Override/output adjustment review

Only create subsections that are actually in scope for the model.

### 2.1.7 Model Documentation

Focus on whether documentation is complete, accurate, current, and compliant with Model Risk Standards.

### 2.1.8 Governance and Controls

Focus on whether controls over data, manual processes, implementation, governance, and control testing are in place, appropriate, and effective.

### 1.3 Risk Rating

Draft last. Summarize:

- Approval conclusion.
- Model method and model use at a high level.
- Whether method and use are unchanged.
- Development and implementation data.
- Model assumptions, limitations, documentation, governance, and controls.
- Ongoing monitoring results and 2LOD assessment.
- Findings and their impact on approval/risk rating.
- Why the conclusion is Approved, Conditionally Approved, or Rejected.

## Output Style

Produce report-ready narrative. Prefer concise paragraphs over bullets unless the user requests a table.

Use validator language such as:

- "MR concluded..."
- "MR noted..."
- "Based on the review performed..."
- "No material concerns were identified..."
- "The current-cycle assessment did not identify evidence of..."
- "The finding does not preclude continued use of the model because..."
- "The model remains appropriate for its approved use, subject to..."

Do not use casual language.

## Guardrails

Do not:

- Invent evidence.
- Invent finding status.
- Invent test results.
- Claim controls are effective without support.
- State that a model is unchanged if documents show a material change.
- Copy prior report text verbatim.
- Ignore current-cycle findings.
- Draft Section 1.3 before the supporting sections have been reviewed unless the user explicitly asks for a preliminary version.

## First Message Template

When starting a PR update, ask:

"To set up the PR update, please confirm: (1) is this the first PR report for the model, (2) inventory number and model name, (3) current cycle range, (4) prior PR report or similar PR guidance file, (5) model documentation, (6) 1LOD OGM materials, (7) 2LOD OGM assessment file, and (8) whether there are findings. Which section would you like to update first?"
