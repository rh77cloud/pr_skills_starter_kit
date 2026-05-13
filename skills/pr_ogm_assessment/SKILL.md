# PR Ongoing Monitoring Assessment Skill

## Purpose

Use this skill to draft or update PR Section 2.1.6 and any ongoing monitoring subsections. This section evaluates whether the ongoing monitoring plan is formally documented, robust, commensurate with the model, compliant with Model Risk Standards, and whether model performance remains appropriate.

This skill should rely heavily on current-cycle 1LOD ongoing monitoring materials and the 2LOD assessment file.

If the 2LOD assessment file includes pasted graphs, charts, tables, screenshots, or reviewer notes, treat the reviewer's notes as the primary interpreted evidence for graph/table discussion. Do not independently infer the meaning of a visual exhibit unless the user explicitly asks. Use the reviewer's stated assessment, thresholds, breaches, explanations, and recommended PR language as the basis for report drafting.

## When to Use

Use this skill for:

- Section 2.1.6.
- Ongoing monitoring subsections.
- Backtesting assessment.
- Sensitivity testing assessment.
- Benchmarking assessment.
- Data monitoring assessment.
- Stability/population monitoring.
- Threshold breach assessment.
- Output adjustment review.
- Performance monitoring conclusion.

## Required Inputs

Confirm the following:

1. Model name.
2. Inventory number.
3. Current cycle range.
4. Prior PR Section 2.1.6 text.
5. 1LOD ongoing monitoring package.
6. 2LOD assessment file, preferably named:
   `INV_XXXX_OGM_2LOD_Assessment.docx`
7. List of required ongoing monitoring tests.
8. Test results and thresholds.
9. Breaches, exceptions, overrides, or adjustments.
10. Relevant findings or observations.
11. Whether the prior conclusion is expected to remain the same.
12. Graph/table notes for relevant OGM exhibits, if any.

## Initial Questions

Ask:

1. "What ongoing monitoring tests are required for this model in the current cycle?"
2. "Has the `INV_XXXX_OGM_2LOD_Assessment.docx` file been provided?"
3. "Are there any additional key discussion points beyond the prior PR report?"
4. "Were there any threshold breaches, exceptions, overrides, output adjustments, or missing tests?"
5. "Are there any relevant findings related to ongoing monitoring?"
6. "Does the 2LOD assessment include pasted graphs, tables, or reviewer notes that should be used to update PR graph/table discussion?"

If the user already provided the answers, proceed without asking again.

## Subsection Creation Rules

Create subsections only for tests that are actually in scope. Do not invent tests.

Possible subsections include:

- 2.1.6.1 Data Ongoing Monitoring
- 2.1.6.2 Snapshot Backtesting
- 2.1.6.3 Sensitivity Testing
- 2.1.6.4 Benchmarking
- 2.1.6.5 Stability Monitoring
- 2.1.6.6 Population Monitoring
- 2.1.6.7 Override or Output Adjustment Review
- 2.1.6.8 Other Model-Specific Monitoring

Use the naming convention from the prior PR report when available.

## Assessment Logic by Test

For each test, identify:

- Test name.
- Purpose.
- Testing period.
- Data used.
- Threshold or benchmark.
- Result.
- 1LOD conclusion.
- 2LOD assessment.
- MR conclusion.
- Any limitation, gap, or compensating control.
- Finding impact, if any.
- Relevant graph/table notes, if any.
- Whether any prior-report graph or table should be refreshed, replaced, removed, or discussed only in narrative.

## Graph and Table Discussion Logic

Use `templates/ogm_graph_table_notes_template.md` when graph/table notes need to be created or organized.

When graph/table notes are provided in the 2LOD assessment:

- Treat the notes as reviewer-interpreted evidence.
- Identify the relevant PR section and monitoring test.
- Use the stated metric, threshold, result, breach/exception status, management explanation, and 2LOD assessment.
- Update narrative discussion to reflect the current-cycle exhibit.
- If the prior PR report included a related graph/table, state whether the exhibit should be refreshed, replaced, removed, or discussed only in narrative when the user provided that direction.
- Do not claim a trend, improvement, deterioration, pass, failure, breach, or exception unless supported by the notes or underlying evidence.
- Do not include visual formatting instructions unless the user asks for report production support.

## Drafting Logic

### If all tests passed and no material issues

Draft language stating that:

- The monitoring plan remains documented and commensurate.
- Required tests were performed.
- Current-cycle evidence supports continued model performance.
- No material concerns were identified.
- Any immaterial observations do not preclude continued use.

### If there are exceptions or breaches

Draft language stating:

- What breach or exception occurred.
- Whether it is isolated or recurring.
- Whether management provided reasonable explanation.
- Whether remediation or escalation is required.
- Whether this affects continued model use.
- Whether a finding is warranted or already issued.

### If a required test is missing

Draft language stating:

- Which test was not provided or not performed.
- Whether the omission affects MR's ability to conclude.
- Whether compensating evidence exists.
- Whether a finding or conditional approval is needed.

### If output adjustments exist

Draft language stating:

- What adjustment was made.
- Why it was made.
- Whether it was approved and documented.
- Whether the adjustment is reasonable.
- Whether it affects performance interpretation.

## Required Output Format

Use this structure:

### 2.1.6 Ongoing Monitoring

[Opening paragraph summarizing monitoring plan, required tests, current-cycle materials reviewed, and overall conclusion.]

#### 2.1.6.x [Test Name]

[Report-ready assessment of the test.]

Conclusion sentence:
"Based on the current-cycle monitoring evidence reviewed, MR concluded that [test-specific conclusion]."

Final Section 2.1.6 conclusion:
"Overall, MR concluded that the ongoing monitoring plan remains [documented/commensurate/appropriate], and the current-cycle monitoring results [support/do not fully support] continued model performance."

## Style Rules

- Use validator voice.
- Be evidence-based.
- Do not overstate test strength.
- Do not invent thresholds.
- Do not claim tests passed unless supported.
- Incorporate both 1LOD results and 2LOD assessment.
- Connect findings to the final monitoring conclusion.
- Keep testing details concise but sufficient.
- Use current-cycle evidence rather than prior-cycle evidence unless comparing trends.

## Quality Checklist

Before finalizing, verify:

- All required OGM tests are covered.
- The 2LOD assessment file is referenced if provided.
- All breaches/exceptions are discussed.
- All relevant findings are incorporated.
- Section conclusion aligns with Section 1.3 risk rating.
- No unsupported pass/fail language is used.
