# Publication Artefacts

Generated `.docx` and `.pdf` files are intentionally not committed here. The authoritative source remains Markdown in the repository.

For the Version 1.0 release sequence:

1. build and verify the Release Candidate source and Markdown archives,
2. publish and practically review `1.0.0-rc.1`,
3. generate Word and PDF from the same selected source commit,
4. visually inspect navigation, tables, code blocks, page breaks and metadata,
5. publish final artefacts with SHA-256 checksums for `1.0.0`.

Release Candidate preview output is written below `artifacts/release-candidate/` and is excluded from Git.
