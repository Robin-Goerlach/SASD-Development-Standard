# Update Package Routing Checklist

Use this checklist before applying a ZIP, patch, generated overlay, or migration package.

## Target identity

- [ ] The canonical target repository is named explicitly.
- [ ] The local `origin` remote matches the package target.
- [ ] Required repository marker files are present.
- [ ] The package does not target a similarly named sibling repository.

## Package content

- [ ] Added, changed, and removed paths are listed separately.
- [ ] The package states whether direct extraction is sufficient.
- [ ] Deletions are performed by a reviewed script or patch, not assumed from ZIP extraction.
- [ ] The package SHA-256 matches the supplied checksum.
- [ ] Existing uncommitted work has been reviewed or backed up.

## Application and evidence

- [ ] The application command is executed from the intended repository root.
- [ ] `git status --short` is reviewed before commit.
- [ ] Repository-specific validation passes.
- [ ] Generated manifests are refreshed after deletions.
- [ ] CI evidence is linked only after the committed revision has run.
