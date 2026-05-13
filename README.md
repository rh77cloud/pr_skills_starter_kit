# PR Skills Starter Kit

This starter kit contains Markdown skills for automating periodic review report drafting for Model Risk Management reports.

## Included Skills

- `pr_report_orchestrator`: Controls the full PR update workflow.
- `pr_section_update`: Updates Sections 2.1.1 through 2.1.5, 2.1.7, and 2.1.8.
- `pr_ogm_assessment`: Updates Section 2.1.6 and ongoing monitoring subsections.
- `pr_risk_rating`: Updates Section 1.3 Risk Rating.

## Recommended Use

1. Place the `skills/` folder in your project repository.
2. Add `AGENTS.md` to the repository root.
3. In Codex, open the repository folder.
4. Ask Codex to read `AGENTS.md`.
5. Then ask Codex to use the relevant skill file for the section you are drafting.

## Example Codex Prompt

```text
Read AGENTS.md and use skills/pr_report_orchestrator/SKILL.md. I am updating a Tier II PR report. First ask me for the required intake information, then help me update Section 2.1.1 using skills/pr_section_update/SKILL.md.
```

## Recommended Next Build Step

After the skills are in place, build a simple intake form that captures:

- Inventory number
- Model name
- Model tier
- Current cycle range
- Whether this is the first PR
- Prior PR report path
- Model documentation path
- 1LOD OGM materials path
- 2LOD OGM assessment path
- Findings appendix path
- Section to update
- Current-cycle changes
- Additional discussion points
- Relevant findings
