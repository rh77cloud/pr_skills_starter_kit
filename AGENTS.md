# AGENTS.md

## Project Purpose

This repository supports an AI-assisted Model Risk Management periodic review report drafting workflow. The project uses skills-style Markdown instructions to help an agent update PR report sections consistently, using prior reports, model documentation, ongoing monitoring materials, 2LOD assessments, and findings.

## Main Workflow

When helping with this repository, follow this sequence:

1. Use `skills/pr_report_orchestrator/SKILL.md` to understand the overall PR workflow.
2. Use `skills/pr_section_update/SKILL.md` for Sections 2.1.1 through 2.1.5, 2.1.7, and 2.1.8.
3. Use `skills/pr_ogm_assessment/SKILL.md` for Section 2.1.6 and ongoing monitoring subsections.
4. Use `skills/pr_risk_rating/SKILL.md` for Section 1.3 after the supporting sections are completed.

## Important Drafting Rules

- Do not invent facts, findings, test results, or conclusions.
- Ask for current-cycle changes before drafting a section unless already provided.
- Preserve prior report structure, tone, and validator voice.
- Refresh dates, cycle periods, evidence, and references.
- Avoid verbatim reuse from the prior report.
- Incorporate relevant findings in the section where they apply.
- Draft Section 1.3 after Sections 2.1.1 through 2.1.8 are updated.

## Expected Repository Structure

```text
pr_skills_starter_kit/
├── AGENTS.md
├── GEMINI.md
├── README.md
├── docs/
│   ├── project_definition.md
│   ├── workflow.md
│   ├── section_map.md
│   └── evidence_requirements.md
├── examples/
│   ├── sample_intake.md
│   └── sample_section_2_1_1_output.md
├── outputs/
│   └── .gitkeep
├── templates/
│   ├── intake_template.md
│   ├── section_update_prompt.md
│   ├── ogm_prompt.md
│   └── risk_rating_prompt.md
└── skills/
    ├── pr_report_orchestrator/
    │   └── SKILL.md
    ├── pr_section_update/
    │   └── SKILL.md
    ├── pr_ogm_assessment/
    │   └── SKILL.md
    └── pr_risk_rating/
        └── SKILL.md
```

## Codex Tasks That Are Appropriate

Codex can help with:

- Creating or editing skill Markdown files.
- Building a Streamlit intake form.
- Creating prompt templates.
- Creating a section generation script.
- Creating a report assembly workflow.
- Writing tests to check whether all required inputs are present.
- Creating examples and sample report outputs.

## Codex Tasks That Require Human Review

Human validator review is required for:

- Final report conclusions.
- Finding severity.
- Approval, conditional approval, or rejection decision.
- Whether a model change requires new validation.
- Whether evidence is sufficient.
- Whether controls are effective.
