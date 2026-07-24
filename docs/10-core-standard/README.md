# Core Standard

Der Core Standard enthält die technologieunabhängigen Anforderungen des SASD Development Standard. Er gilt gemeinsam mit einer Qualitätsstufe und den ausgewählten Profilen.

## Status

Alle Core-Dokumente liegen derzeit als **Draft 0.2.0** vor. Sie sind inhaltlich ausgearbeitet, aber noch nicht als verbindliche Version 1.0 freigegeben.

## Empfohlene Lesereihenfolge

1. [Qualitätsstufen](QUALITY-LEVELS.md)
2. [Projektlebenszyklus](PROJECT-LIFECYCLE.md)
3. [Anforderungsmanagement](REQUIREMENTS.md)
4. [Architekturstandard](ARCHITECTURE.md)
5. [Dokumentationsstandard](DOCUMENTATION.md)
6. [Repository- und GitHub-Standard](REPOSITORY.md)
7. [Qualitätsstandard](QUALITY.md)
8. [Sicherheitsstandard](SECURITY.md)
9. [Teststandard](TESTING.md)
10. [Release-Standard](RELEASES.md)
11. [Wartungsstandard](MAINTENANCE.md)
12. [Wissensmanagement](KNOWLEDGE-MANAGEMENT.md)
13. [KI-gestützte Entwicklung](AI-ASSISTED-DEVELOPMENT.md)

## Anwendung

Ein Projekt wendet den Core Standard in fünf Schritten an:

1. Projekt klassifizieren und Qualitätsstufe wählen.
2. Anwendbare Core-Anforderungen identifizieren.
3. Technologie- und Projektprofile ergänzen.
4. Nachweise, offene Lücken und Abweichungen dokumentieren.
5. Die Anwendung zu Meilensteinen und Releases erneut prüfen.

Die [Core-Standard-Adoptionscheckliste](../../checklists/project-initiation/CORE-STANDARD-ADOPTION-CHECKLIST.md) unterstützt diesen Ablauf.

## Requirement IDs

Normative Anforderungen besitzen stabile IDs nach Bereichen:

| Präfix | Bereich |
|---|---|
| `SASD-QL` | Qualitätsstufen |
| `SASD-LC` | Projektlebenszyklus |
| `SASD-REQ` | Anforderungen |
| `SASD-ARCH` | Architektur |
| `SASD-DOC` | Dokumentation |
| `SASD-REP` | Repository und Git |
| `SASD-QUAL` | Qualität |
| `SASD-SEC` | Sicherheit |
| `SASD-TEST` | Tests |
| `SASD-REL` | Releases |
| `SASD-MNT` | Wartung |
| `SASD-KM` | Wissensmanagement |
| `SASD-AI` | KI-gestützte Entwicklung |

IDs werden für Compliance, Abweichungen, Reviews und spätere Toolunterstützung verwendet. Sie dürfen nach Veröffentlichung nicht ohne Migrationshinweis neu vergeben werden.

## Externe Orientierung

Der Core Standard ist eine eigenständige SASD-Spezifikation. Er orientiert sich in einzelnen Themen an anerkannten öffentlichen Quellen, ohne derzeit eine formale Konformität zu diesen Spezifikationen zu behaupten:

- [RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119.html)
- [RFC 8174 — Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174.html)
- [NIST SP 800-218 — Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
- [OWASP Software Assurance Maturity Model](https://owasp.org/www-project-samm/)
- [Semantic Versioning 2.0.0](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [SLSA Specification](https://slsa.dev/spec/)
- [SPDX](https://spdx.dev/)
- [CycloneDX](https://cyclonedx.org/)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)

## Reviewziel

Der nächste Reifeschritt ist die Überführung von `Draft` nach `Proposed`. Dafür müssen insbesondere folgende Fragen geprüft werden:

- Sind alle MUSS-Anforderungen verständlich und prüfbar?
- Ist der Aufwand für Minimum angemessen?
- Deckt Recommended die normalen SASD-Projekte ab?
- Sind Production-Anforderungen stark genug, ohne unerfüllbare Scheinsicherheit zu erzeugen?
- Gibt es Widersprüche oder unnötige Duplikate zwischen den Core-Dokumenten?
- Lassen sich die Anforderungen auf kleine, mittlere und komplexere Pilotprojekte anwenden?
