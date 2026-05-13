# PR Risk Rating Section Skill

## Purpose

Use this skill to draft or update PR Section 1.3 Risk Rating after Sections 2.1.1 through 2.1.8 have been updated. The risk rating section summarizes the overall periodic review conclusion and explains whether the model remains approved for continued use.

## When to Use

Use this skill when the user asks to draft or update:

- Section 1.3 Risk Rating.
- Overall PR conclusion.
- Approval conclusion.
- Approved / Conditionally Approved / Rejected language.
- Final model risk assessment narrative.

## Required Inputs

Before drafting, confirm:

1. Model name.
2. Inventory number.
3. Model tier.
4. Current cycle range.
5. Prior PR risk rating section.
6. Current conclusion:
   - Approved
   - Conditionally Approved
   - Rejected
7. Whether the conclusion is the same as the prior PR.
8. Summary of Sections 2.1.1 through 2.1.8.
9. Section 2.1.6 ongoing monitoring conclusion.
10. Findings, if any.
11. Finding severity and status.
12. Whether any findings preclude continued use.
13. Any compensating controls or remediation commitments.

## Initial Questions

Ask:

1. "Is the conclusion the same as the prior PR: Approved, Conditionally Approved, or Rejected?"
2. "Are there any current-cycle findings?"
3. "Do any findings affect continued model use or require conditional approval?"
4. "Should any prior findings be discussed as closed, repeated, or still open?"
5. "Is Section 2.1.6 complete and ready to summarize?"

If the user already provided the answers, proceed without asking again.

## Required Content

The risk rating section must cover:

1. Approval conclusion.
2. High-level model method.
3. High-level model use.
4. Whether method and use are unchanged.
5. Development data conclusion.
6. Implementation data conclusion.
7. Model framework conclusion.
8. Assumptions and limitations conclusion.
9. Mathematical structure and variables conclusion.
10. Ongoing monitoring results and 2LOD assessment.
11. Documentation conclusion.
12. Governance and controls conclusion.
13. Findings and their impact.
14. Final rationale for approval, conditional approval, or rejection.

## Drafting Logic

### If conclusion remains Approved and no findings

State that:

- The model remains appropriate for continued use.
- No material changes were identified in model use, framework, data, assumptions, mathematical structure, documentation, or controls.
- Ongoing monitoring results support continued performance.
- No material issues were identified that would preclude approval.

### If conclusion remains Approved with findings

State that:

- Findings were identified.
- Findings are described by severity and theme.
- Findings do not preclude continued use because of specific mitigating factors.
- Remediation should be tracked through standard governance.
- Approval remains appropriate.

### If conclusion is Conditionally Approved

State that:

- Continued use is permitted subject to remediation, controls, or limitations.
- Findings or evidence gaps are material enough to require conditions.
- Conditions must be specific and traceable.
- The section should clearly identify what must be remediated.

### If conclusion is Rejected

State that:

- MR does not support continued use.
- Reasons are evidence-based and tied to model risk standards.
- Material deficiencies are clearly identified.
- Required remediation or validation steps are described.

## Suggested Structure

### 1.3 Risk Rating

Opening paragraph:
- State the conclusion and current-cycle scope.

Model overview paragraph:
- Describe model method and use at a high level.
- State whether method and use are unchanged.

Data and framework paragraph:
- Summarize development data, implementation data, framework, assumptions, limitations, mathematical structure, and variables.

Ongoing monitoring paragraph:
- Summarize monitoring tests, current-cycle results, 2LOD assessment, breaches/exceptions, and output adjustments.

Documentation/governance paragraph:
- Summarize documentation, controls, governance, and control testing.

Findings paragraph:
- Incorporate relevant findings.
- Explain impact on approval conclusion.

Final conclusion paragraph:
- State why the final rating is appropriate.

## Style Rules

- Use polished, executive-level validator language.
- Keep the section concise but complete.
- Do not include excessive test-level detail; rely on Section 2.1.6 for detail.
- Do not introduce new evidence not discussed in supporting sections.
- Do not contradict Sections 2.1.1 through 2.1.8.
- Do not overstate approval if findings are material.
- Avoid copy-paste from prior PR.
- Preserve prior report tone and structure where appropriate.

## Useful Language

Approved with no material issues:

"Based on the periodic review performed, MR concluded that the model remains appropriate for continued use for its approved purpose. The review did not identify material changes in model use, development data, implementation data, framework, assumptions, mathematical structure, documentation, or governance and controls that would require a new validation or preclude continued use."

Approved with findings:

"Although MR identified [Finding X], the issue does not preclude continued model use because [specific rationale]. The finding is subject to remediation through standard model risk governance and has been considered in the overall risk rating conclusion."

Conditionally approved:

"MR conditionally approves continued use of the model subject to timely remediation of [specific issue]. The condition is necessary because [specific risk], but continued use remains supportable due to [compensating control/evidence]."

Rejected:

"MR does not approve continued use of the model because [specific material deficiency]. The deficiency limits MR's ability to conclude that the model remains appropriate for its approved use."

## Quality Checklist

Before finalizing, verify:

- The conclusion is explicit.
- Findings are incorporated.
- Section 2.1.6 is summarized accurately.
- Supporting sections are not contradicted.
- Risk rating language is proportionate to evidence.
- The final paragraph clearly supports Approved, Conditionally Approved, or Rejected.
