# Tooling

This directory contains small tools and reusable configuration files that support the SASD Development Standard.

## Document metadata validator

Run from the repository root:

```bash
python tooling/validate-document-metadata.py
```

The script checks standard documents for:

- YAML front matter,
- required metadata fields,
- known document types and lifecycle states,
- valid document IDs,
- duplicate document IDs,
- ISO-formatted update dates.

The validator has no external Python dependencies. It intentionally validates only the simple top-level metadata format used by this repository.

Automated GitHub workflows will be added only after the corresponding rules are approved.


## Markdown link validator

Run from the repository root:

```bash
python tooling/validate-markdown-links.py
```

The script checks relative Markdown links and reports missing files or links that leave the repository. External URLs and page anchors are intentionally ignored.
