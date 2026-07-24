# C#/.NET Profile Adoption Checklist

## Classification

- [ ] Core quality level selected.
- [ ] C#/.NET profile version recorded.
- [ ] Additional profile such as Desktop selected if applicable.
- [ ] Target frameworks and supported platforms documented.
- [ ] Runtime deployment model documented.

## Build baseline

- [ ] Supported .NET SDK selected.
- [ ] LTS versus STS decision documented.
- [ ] `global.json` decision made.
- [ ] Restore, build, test and publish commands documented.
- [ ] `Directory.Build.props` reviewed.
- [ ] Central package management decision made.
- [ ] Package sources documented and trusted.

## Code quality

- [ ] Nullable enabled or migration plan recorded.
- [ ] `.editorconfig` present.
- [ ] Analyzer and warning policy defined.
- [ ] XML documentation scope defined.
- [ ] Error and logging boundaries defined.

## Architecture

- [ ] Small, maintained or complex structure selected.
- [ ] Project roles and dependency direction documented.
- [ ] Composition Root identified.
- [ ] Persistence and configuration boundaries identified.
- [ ] Test project structure created.

## Verification

- [ ] Local clean restore/build/test succeeds.
- [ ] Profile validators succeed.
- [ ] Initial profile assessment created.
