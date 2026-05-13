# Local Inputs Example

Copy this folder to `local_inputs/` on your work machine and place model evidence in the appropriate folders.

```bash
cp -R local_inputs.example local_inputs
```

The real `local_inputs/` folder is ignored by git so confidential evidence is not committed.

## Folder Purpose

- `prior_pr_report/`: Prior PR report or similar model PR guidance report.
- `model_documentation/`: Current model documentation and supporting model materials.
- `ogm_1lod/`: Current-cycle 1LOD ongoing monitoring packages and results.
- `ogm_2lod/`: Current-cycle 2LOD ongoing monitoring assessment, preferably named `INV_XXXX_OGM_2LOD_Assessment.docx`.
- `findings/`: Findings appendix or finding descriptions.
- `management_responses/`: Management responses, remediation updates, or closure evidence.
- `prior_validation/`: Prior validation report, if useful.

Do not place confidential files in `local_inputs.example/`; it is committed as a structure example only.
