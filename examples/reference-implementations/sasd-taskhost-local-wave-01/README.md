# SASD TaskHost Local – Wave 01 Target Layout

Dieses Beispiel zeigt die in Wave 01 erwarteten Ergänzungen im Ziel-Repository. Es ist kein bereits ausgeführter Patch.

```text
SASD-TaskHost-Local/
├── .github/
│   └── workflows/
│       └── build.yml
├── TaskHostLocal.Tests/
├── docs/
│   └── standards/
│       ├── SASD-ALIGNMENT.md
│       ├── SASD-GAP-REGISTER.md
│       └── WAVE-01-REVIEW.md
├── .editorconfig
├── Directory.Build.props
├── global.json
├── LICENSE
└── SECURITY.md
```

Die vorhandene `TaskHostLocal.WinForms`-Struktur bleibt bestehen. Der Pilot verlangt keine Verschiebung nach `src/` und keine Aufteilung in zusätzliche Produktionsassemblies.
