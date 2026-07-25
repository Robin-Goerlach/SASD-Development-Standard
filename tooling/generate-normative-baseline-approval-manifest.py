#!/usr/bin/env python3
"""Generate or verify the SHA-256 manifest for the Approved 0.9.0 normative baseline."""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
from normative_baseline_common import BUNDLE_NAME, BUNDLE_VERSION, bundle_documents, sha256

OUTPUT = "docs/40-governance/NORMATIVE-BASELINE-APPROVAL-MANIFEST-0.9.0.md"

def build(repo: Path) -> str:
    docs=bundle_documents(repo)
    rows=[]
    for doc in docs:
        rows.append(f"| `{doc.document_id}` | `{doc.relative_path}` | `{doc.metadata.get('version')}` | `{doc.metadata.get('status')}` | `{sha256(doc.path)}` |")
    return "\n".join([
        "---",
        'title: "Normative Baseline Approval Manifest 0.9.0"',
        "document-id: SASD-REF-BASELINE-008",
        "document-type: informative",
        "status: Approved",
        "version: 0.9.0",
        'standard-version: "1.0"',
        "language: de",
        "authoritative: false",
        "owner: SASD Development Standard Maintainer",
        "last-updated: 2026-07-24",
        "approved-on: 2026-07-24",
        "approval-record: SASD-REF-BASELINE-007",
        "applies-to-quality-levels: [Minimum, Recommended, Production]",
        "applies-to-profiles: [Core, DotNet, Desktop]",
        "depends-on: [SASD-REF-BASELINE-007]",
        "normative-keywords: []",
        "---", "", "# Normative Baseline Approval Manifest 0.9.0", "",
        "Dieses Manifest identifiziert die 32 als `Approved 0.9.0` freigegebenen normativen Dokumente durch SHA-256-Prüfsummen.", "",
        f"- Approval bundle: `{BUNDLE_NAME}`",
        f"- Document version: `{BUNDLE_VERSION}`",
        f"- Documents: `{len(docs)}`", "",
        "| Dokument-ID | Pfad | Version | Status | SHA-256 |",
        "|---|---|---:|---|---|", *rows, "",
        "Die Prüfsummen beziehen sich auf die vollständigen Markdown-Dateien einschließlich Front Matter.", ""
    ])

def main()->int:
    p=argparse.ArgumentParser()
    p.add_argument('--check',action='store_true')
    args=p.parse_args()
    repo=Path(__file__).resolve().parents[1]
    out=repo/OUTPUT
    expected=build(repo)
    if args.check:
        if not out.exists() or out.read_text(encoding='utf-8')!=expected:
            print(f"FAIL stale approval manifest: {OUTPUT}")
            return 1
        print(f"OK   approval manifest is current: {OUTPUT}")
        return 0
    out.write_text(expected,encoding='utf-8')
    print(f"Wrote {OUTPUT}")
    return 0
if __name__=='__main__':
    sys.exit(main())
