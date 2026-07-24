# Contributing

Thank you for considering a contribution to the SASD Development Standard.

## Current development phase

The repository is currently in the pre-1.0 foundation phase. Structural changes are expected, but proposals should remain traceable and focused.

## Contribution principles

Contributions should:

- solve a concrete and documented problem,
- remain practical for solo developers and small teams,
- distinguish mandatory rules from recommendations,
- avoid unnecessary bureaucracy,
- include rationale and consequences,
- preserve reproducibility and long-term maintainability.

## Proposing a change

1. Search existing issues and decision records.
2. Open a proposal issue using the standard-change template.
3. Describe the problem, proposed rule, alternatives, and expected consequences.
4. Use an Architecture Decision Record when the proposal affects the structure or governance of the standard.
5. Update affected documentation and checklists together.

## Document conventions

- Markdown is the source of truth.
- Use clear headings and short sections.
- Use **MUST**, **SHOULD**, and **MAY** only in normative documents.
- Explain the reason behind important requirements.
- Avoid copying the same rule into multiple normative documents.
## Verification before submission

Run the same dependency-free checks used by repository CI:

```bash
python tooling/run-quality-gates.py
```

Windows users may also run:

```powershell
.\scripts\validate-repository.ps1
```

A successful local run does not replace the GitHub Actions result for the committed revision. Changes to workflows, tooling, Foundation, or Governance require particular review because these paths are covered by CODEOWNERS.

After the `main` ruleset is activated, changes should be pushed to a working branch and merged through a pull request after `SASD merge gate` succeeds. The activation procedure and evidence rules are documented under `docs/50-reference-implementations/repository-self-hosting/`.

