# SASD Prompt Packages

Dieser Bereich enthält versionierte, prüfbare Prompts als unterstützende Artefakte des SASD Development Standard.

## Kanonisches Paket

- Paket-ID: `sasd-development-standard-v1`
- Version: `0.13.0`
- Status: `Candidate`
- Sprache: Deutsch
- Prompts: **39**
- Kategorien: **9**

Das Paket deckt Projektinitialisierung, Recherche, Anforderungen, Architektur, Entwicklung, Debugging, Reviews, Dokumentation und Releases ab.

## Wichtige Abgrenzung

Die Dateien bilden ein stabiles SASD-Austauschformat. Sie sind **nicht** als ungeprüfte Kopie des internen Datenformats einer bestimmten Prompt-Manager-Version zu verstehen. Ein Importadapter darf erst als kompatibel bezeichnet werden, wenn Export, Import, Variablen, IDs und Roundtrip gegen einen exakten Prompt-Manager-Commit geprüft wurden.

## Verwendung

```bash
python tooling/validate-prompt-packages.py
python tooling/generate-prompt-catalog.py --check
python tooling/build-prompt-package.py --output-dir artifacts/prompt-packages
python tooling/verify-prompt-package.py --directory artifacts/prompt-packages
```

Weitere Informationen:

- [Paketspezifikation](PACKAGE-SPECIFICATION.md)
- [Qualitätsleitfaden](QUALITY-GUIDE.md)
- [Sicherheitsleitfaden](SECURITY-GUIDE.md)
- [Variablenmodell](VARIABLES.md)
- [Prompt-Manager-Importadapter-Plan](PROMPT-MANAGER-IMPORT-ADAPTER-PLAN.md)
- [Paketübersicht](packages/sasd-development-standard-v1/README.md)
