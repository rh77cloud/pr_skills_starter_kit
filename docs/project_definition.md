# Project Definition

## Purpose

This repository provides reusable instructions, templates, and examples for AI-assisted drafting of Model Risk Management periodic review (PR) reports.

The primary goal is to help a reviewer update a prior PR report into a current-cycle PR report by using current evidence while preserving validator voice, prior report structure, and conclusion logic.

## Target User

The target user is a model risk reviewer or validator who needs to update Tier I, Tier II, or Tier III PR report sections using:

- Prior PR report language.
- Current model documentation.
- Current-cycle 1LOD ongoing monitoring materials.
- Current-cycle 2LOD ongoing monitoring assessment materials.
- Current-cycle findings, observations, or remediation updates.

## Target Environment

The intended work environment is:

- VS Code.
- Gemini Code Assist or Gemini CLI.
- A cloned copy of this repository.
- Local access to confidential model evidence stored outside the repository or in ignored local folders.

## Repository Boundaries

This repository should contain reusable workflow assets only:

- Agent instructions.
- Gemini context.
- Skills.
- Documentation.
- Prompt templates.
- Sanitized examples.
- Output folder scaffolding.
- Safe local input folder examples.
- Lightweight helper scripts.

Do not commit confidential model reports, production data, finding appendices, model documentation, or bank/internal evidence.

## Standard Section Map

Use this section map:

| Section | Title |
| --- | --- |
| 2.1.1 | Development Data |
| 2.1.2 | Implementation Data |
| 2.1.3 | Model Framework |
| 2.1.4 | Model Assumptions and Limitations |
| 2.1.5 | Mathematical Structure and Variables |
| 2.1.6 | Ongoing Monitoring |
| 2.1.7 | Model Documentation |
| 2.1.8 | Governance and Controls |
| 1.3 | Risk Rating |

## Success Criteria

The repository is ready for work use when a user can:

1. Clone the repository.
2. Open it in VS Code.
3. Ask Gemini to read `GEMINI.md` and `AGENTS.md`.
4. Fill out `templates/intake_template.md`.
5. Provide local paths to current-cycle evidence.
6. Update Sections 2.1.1 through 2.1.8 one section at a time.
7. Draft Section 1.3 after supporting sections are complete.
8. Review and finalize the output with human validator judgment.

## Local Confidential Evidence

Use `local_inputs.example/` as the committed structure template. Copy it to `local_inputs/` on the work machine:

```bash
cp -R local_inputs.example local_inputs
```

The real `local_inputs/` folder is ignored by git.
