# Release Artifact Verification Checklist

- [ ] Download or copy artifacts into an empty directory.
- [ ] Verify `SHA256SUMS.txt` before extracting archives.
- [ ] Run `python tooling/verify-release-candidate.py --directory <path>`.
- [ ] Confirm both archives pass ZIP integrity checks.
- [ ] Confirm every member is below the intended root directory.
- [ ] Confirm no absolute paths or `..` traversal members exist.
- [ ] Confirm manifest version and source commit match the Release Record.
- [ ] Confirm source and Markdown archives contain the expected root documents.
- [ ] Confirm no `.git`, `artifacts`, caches, secrets or local IDE files are present.
- [ ] Confirm hashes match a second independent build from the same commit.
- [ ] Record verifier output in the Release Record.
