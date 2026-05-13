# PR Section Update Skill

## Purpose

Use this skill to update individual PR report Sections 2.1.1 through 2.1.5, 2.1.7, and 2.1.8. This skill refreshes prior-cycle language using current-cycle evidence while preserving report structure, validator tone, and conclusion logic.

Do not use this skill for Section 2.1.6 ongoing monitoring. Use `pr_ogm_assessment` instead.

Do not use this skill for Section 1.3 risk rating. Use `pr_risk_rating` instead.

## Applicable Sections

### 2.1.1 Development Data

Question to answer:
Does the model development data remain representative of both the current portfolio and the macroeconomic environment, and is it appropriate for continued use?

Review focus:

- Development sample.
- Recalibration or auto-tuning data.
- Portfolio representativeness.
- Macroeconomic representativeness.
- Data relevance, accuracy, and completeness.
- Whether changes require new validation.

### 2.1.2 Implementation Data

Question to answer:
Have implementation data sources, feeds, transformations, systems, or manual inputs changed?

Review focus:

- Production data sources.
- Data lineage.
- Data feeds.
- Implementation files.
- Manual adjustments.
- Source system changes.
- Data quality controls.

### 2.1.3 Model Framework

Question to answer:
Has the model framework changed in a way that requires validation, expanded scope, new uses, or renewed suitability review?

Review focus:

- Model purpose.
- Model use.
- Methodology.
- Approved model scope.
- New business applications.
- Emerging academic or industry concerns.
- Suitability of the model framework.

### 2.1.4 Model Assumptions and Limitations

Question to answer:
Do assumptions remain appropriate, and are limitations mitigated within risk appetite?

Review focus:

- Core model assumptions.
- Known limitations.
- Compensating controls.
- Risk appetite.
- Business/environmental changes that may weaken assumptions.
- Finding impact on assumptions or limitations.

### 2.1.5 Mathematical Structure and Variables

Question to answer:
Have mathematical formulas, model variables, transformations, segmentations, calibration mechanics, or analytical structures changed?

Review focus:

- Mathematical structure.
- Analytical formulas.
- Model variables.
- Transformations.
- Segmentation.
- Calibration method.
- Feature selection.
- Parameter estimation.
- Any change requiring validation.

### 2.1.7 Model Documentation

Question to answer:
Is model documentation complete, accurate, current, and compliant with Model Risk Standards?

Review focus:

- Model documentation completeness.
- Accuracy against current implementation.
- Methodology descriptions.
- Data documentation.
- Assumptions and limitations.
- Monitoring documentation.
- Change logs.
- Governance evidence.

### 2.1.8 Governance and Controls

Question to answer:
Are model controls over data, manual processes, implementation, governance, and control testing in place, appropriate, and effective?

Review focus:

- Data controls.
- Manual process controls.
- Implementation controls.
- Access controls.
- Change management.
- Review/approval controls.
- Spreadsheet or EUC controls.
- Control testing results.
- Governance appendix references.

## Required Inputs

For the selected section, obtain:

1. Prior PR section text or similar PR guidance text.
2. Current-cycle range.
3. Model name and inventory number.
4. Current-cycle evidence relevant to the section.
5. User-confirmed changes, if any.
6. Additional key discussion points, if any.
7. Relevant findings, if any.
8. Desired conclusion, if already known.

## Section Intake Questions

Before drafting each section, ask:

1. "What changed in this area during the current cycle?"
2. "Are there any additional key discussion points beyond what was included in the prior PR report?"
3. "Are there any relevant findings, observations, documentation gaps, or open issues that should be incorporated?"
4. "Should the conclusion remain the same as the prior PR report?"

If the user already provided these answers, do not ask again. Proceed using the available information.

## Drafting Logic

### If no changes and no relevant findings

- Use the prior PR section as the structural template.
- Preserve the prior conclusion.
- Refresh cycle dates and references.
- Rewrite the section to avoid verbatim reuse.
- Use phrases such as:
  - "No material changes were identified..."
  - "MR did not identify evidence indicating..."
  - "The prior conclusion remains appropriate..."
  - "The model remains appropriate for continued use with respect to..."

### If changes exist but no finding

- Describe the change clearly.
- Explain why it does or does not affect continued model use.
- Tie the conclusion to evidence.
- Avoid overstating impact.
- State whether validation is required or not, if supported.

### If relevant findings exist

- Identify finding number and theme.
- Explain how the finding relates to the section.
- Discuss whether the finding affects approval or continued use.
- Use balanced language:
  - "Although Finding X identified..., MR determined that..."
  - "The issue does not preclude continued use because..."
  - "The finding is incorporated into the overall risk rating discussion in Section 1.3."

## Required Output Format

Use this structure unless the user asks otherwise:

### [Section Number] [Section Title]

[Report-ready narrative paragraph or paragraphs.]

Conclusion sentence:
"Based on the review performed, MR concluded that [section-specific conclusion]."

## Style Rules

- Use formal validator voice.
- Prefer narrative paragraphs.
- Avoid bullets in report-ready output unless needed.
- Avoid saying "I".
- Avoid casual phrasing.
- Do not simply copy the prior report.
- Do not invent evidence or conclusions.
- Clearly connect evidence to conclusion.
- Mention current-cycle materials only if reviewed.
- Preserve structure, tone, and conclusion logic from prior PR where appropriate.

## Quality Checklist

Before finalizing, confirm the section:

- Uses current-cycle dates.
- Uses current inventory number and model name.
- Avoids verbatim reuse.
- Reflects any current-cycle changes.
- Reflects relevant findings.
- Maintains the appropriate conclusion.
- Does not make unsupported claims.
- Is consistent with Section 1.3 risk rating implications.
