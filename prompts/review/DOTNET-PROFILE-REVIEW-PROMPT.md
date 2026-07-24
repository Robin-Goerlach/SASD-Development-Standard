# C#/.NET Profile Review Prompt

Review the supplied C#/.NET repository against the SASD Development Standard Core and the Proposed C#/.NET Profile.

## Required context

- repository tree,
- project and solution files,
- `global.json`, `Directory.Build.props`, `Directory.Packages.props`, `.editorconfig`,
- README and architecture documents,
- selected quality level,
- build/test output,
- relevant configuration, logging, persistence and test code.

## Review tasks

1. Determine applicable profile requirements.
2. Separate satisfied, not applicable, exception, open and not assessed requirements.
3. Identify build reproducibility, support, package and analyzer risks.
4. Review project boundaries and dependency directions.
5. Review nullable, async, disposal, error and logging practices.
6. Review configuration, secrets, paths, persistence and migrations.
7. Review test isolation, provider realism, CI and packaging.
8. Prioritize findings by risk and migration effort.
9. Do not recommend extra projects, abstractions or frameworks without a concrete benefit.
10. Produce a practical phased migration plan for a solo developer or small team.

## Output

- executive summary,
- selected applicability assumptions,
- critical findings,
- requirement assessment table with evidence,
- quick wins,
- phased migration plan,
- proposed exceptions,
- validation commands.
