# Core Standard

Der Core Standard enthält die technologieunabhängigen Anforderungen des SASD Development Standard. Er gilt gemeinsam mit einer Qualitätsstufe und den ausgewählten Profilen.

## Status

Alle 13 Core-Dokumente liegen nach dem Konsistenz- und Proportionalitätsreview als **Proposed 0.3.0** vor. Sie sind Freigabekandidaten, aber noch keine verbindlichen Anforderungen einer veröffentlichten Version 1.0.

Die Reviewentscheidung und verbleibenden offenen Punkte sind in [Core Standard Review 0.3.0](CORE-STANDARD-REVIEW-0.3.0.md) dokumentiert.

## Empfohlene Lesereihenfolge

1. [Qualitätsstufen und Anwendbarkeit](QUALITY-LEVELS.md)
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

Ergänzende Hilfen:

- [Verantwortungsmatrix](CORE-RESPONSIBILITY-MAP.md)
- [Leitfaden für Einzelentwickler](SOLO-DEVELOPER-GUIDE.md)
- [Anforderungsindex](CORE-REQUIREMENTS-INDEX.md)
- [Qualitätsstufenmatrix](CORE-QUALITY-LEVEL-MATRIX.md)

## Anwendung

Ein Projekt wendet den Core Standard in sechs Schritten an:

1. Projekt klassifizieren und primäre Qualitätsstufe wählen.
2. Risikobereiche gegebenenfalls höher einstufen.
3. Anwendbare Core-Anforderungen und Bedingungen bewerten.
4. Technologie- und Projektprofile ergänzen.
5. Nachweise, offene Lücken und Ausnahmen dokumentieren.
6. Anwendung zu Meilensteinen, Releases und wesentlichen Änderungen erneut prüfen.

Die [Core-Standard-Adoptionscheckliste](../../checklists/project-initiation/CORE-STANDARD-ADOPTION-CHECKLIST.md) und die [Selbstreview-Checkliste](../../checklists/development/CORE-STANDARD-SELF-REVIEW-CHECKLIST.md) unterstützen diesen Ablauf.

## Interpretation der Anforderungen

- Die Schlüsselwörter MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT und KANN werden nach der [Normativen Sprache](../40-governance/NORMATIVE-LANGUAGE.md) interpretiert.
- Bedingungen und Qualitätsstufen werden nach [QUALITY-LEVELS.md](QUALITY-LEVELS.md) ausgewertet.
- Dokumenteigene Qualitätsmatrizen präzisieren die Tiefe einzelner Maßnahmen.
- `Not Applicable` benötigt bei Pflichtanforderungen eine überprüfbare Begründung.
- Profile dürfen Core-Regeln konkretisieren oder verschärfen, aber nicht stillschweigend abschwächen.
- Nur Approved-Dokumente einer veröffentlichten Standardversion können Grundlage einer formalen Alignment-Aussage sein.

## Requirement IDs

Normative Anforderungen besitzen stabile IDs nach Bereichen:

| Präfix | Bereich |
|---|---|
| `SASD-QL` | Qualitätsstufen und Anwendbarkeit |
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

IDs werden für Alignment, Ausnahmen, Reviews und Toolunterstützung verwendet. Sie dürfen nach Veröffentlichung nicht ohne Migrationshinweis neu vergeben werden.

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

## Nächster Reifeschritt

Der nächste Schritt ist die Pilotierung an kleinen, mittleren und komplexeren Projekten. Die Ergebnisse entscheiden, welche Proposed-Anforderungen vor `Approved` angepasst werden müssen.
