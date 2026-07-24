# Desktop Application Profile

**Normative status:** Proposed 0.5.0
**Primary scope:** C#/.NET desktop applications on Windows, especially WinForms and WPF

The Desktop Application Profile adds UI, UX, accessibility, lifecycle, packaging and support requirements to the technology-independent Core and the C#/.NET Profile.

## Normative documents

1. [Desktop Profile](DESKTOP-PROFILE.md)
2. [UI Architecture](UI-ARCHITECTURE.md)
3. [User Experience](USER-EXPERIENCE.md)
4. [Application Lifecycle](APPLICATION-LIFECYCLE.md)

## Informative guidance

- [Desktop Reference Baseline](DESKTOP-REFERENCE-BASELINE.md)
- [Windows Forms Guidance](WINDOWS-FORMS-GUIDANCE.md)
- [WPF Guidance](WPF-GUIDANCE.md)
- [Desktop Project Sizing Guide](DESKTOP-PROJECT-SIZING-GUIDE.md)
- [Desktop Quality Level Matrix](DESKTOP-QUALITY-LEVEL-MATRIX.md)
- [Desktop Requirements Index](DESKTOP-REQUIREMENTS-INDEX.md)
- [Desktop Profile Review 0.5.0](DESKTOP-PROFILE-REVIEW-0.5.0.md)

## Adoption path

1. Select the Core quality level.
2. Apply the C#/.NET Profile.
3. Document UI technology and supported Windows matrix.
4. Select a proportional project size model.
5. Complete the Desktop adoption checklist.
6. Review UI architecture, UX, accessibility and lifecycle evidence.
7. Run the Desktop profile validator.

## Tooling

```bash
python tooling/validate-desktop-profile.py
python tooling/generate-desktop-requirements-index.py --check
```
