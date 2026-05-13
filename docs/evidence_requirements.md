# Evidence Requirements

## Core Materials

For a non-first PR report, collect:

- Prior PR report.
- Current cycle range.
- Prior cycle range.
- Current model documentation.
- Current-cycle 1LOD ongoing monitoring materials.
- Current-cycle 2LOD ongoing monitoring assessment.
- Findings appendix or finding descriptions, if applicable.
- Management responses or remediation updates, if applicable.

For a first PR report, collect:

- Similar model's prior PR report for guidance.
- Current model documentation.
- Current-cycle 1LOD ongoing monitoring materials.
- Current-cycle 2LOD ongoing monitoring assessment.
- Current cycle range.
- Inventory number.
- Model name.
- Model tier.
- Findings appendix or finding descriptions, if applicable.
- Prior validation report, if available and useful.

## Recommended 2LOD File Name

Use this convention when possible:

```text
INV_XXXX_OGM_2LOD_Assessment.docx
```

Replace `XXXX` with the model inventory number.

## Section-Level Evidence

| Section | Evidence to Check |
| --- | --- |
| 2.1.1 Development Data | Development sample, recalibration data, auto-tuning data, portfolio representativeness, macroeconomic representativeness, data relevance, data accuracy, data completeness. |
| 2.1.2 Implementation Data | Production data sources, feeds, lineage, transformations, implementation files, manual inputs, source system changes, data quality controls. |
| 2.1.3 Model Framework | Model purpose, approved use, methodology, scope, new activities, emerging academic or industry concerns. |
| 2.1.4 Assumptions and Limitations | Core assumptions, known limitations, compensating controls, risk appetite, environmental or business changes. |
| 2.1.5 Mathematical Structure and Variables | Formulas, variables, transformations, segmentation, calibration mechanics, feature selection, parameter estimation. |
| 2.1.6 Ongoing Monitoring | Required tests, testing period, thresholds, results, breaches, exceptions, overrides, output adjustments, 1LOD conclusion, 2LOD assessment. |
| 2.1.7 Documentation | Current model documentation, methodology descriptions, data documentation, assumptions and limitations, monitoring documentation, change logs, governance evidence. |
| 2.1.8 Governance and Controls | Data controls, manual process controls, implementation controls, access controls, change management, review and approval controls, spreadsheet or EUC controls, control testing results. |

## Evidence Gap Handling

If evidence is missing:

1. Identify the missing item.
2. Ask the user whether it is available.
3. Avoid making unsupported conclusions.
4. If drafting must continue, mark the language as dependent on human confirmation.
