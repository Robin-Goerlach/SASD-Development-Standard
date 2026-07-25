#!/usr/bin/env python3
"""Validate formal approval of the SASD normative baseline 0.9.0."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path
from normative_baseline_common import (
    BUNDLE_NAME, BUNDLE_VERSION, EXPECTED_DOCUMENT_COUNT, EXPECTED_REQUIREMENT_COUNT,
    bundle_documents, extract_requirements, load_documents, topological_order,
)

APPROVAL_ID="SASD-REF-BASELINE-007"
APPROVED_ON="2026-07-24"
FILES=(
 "docs/40-governance/NORMATIVE-BASELINE-APPROVAL-0.9.0.md",
 "docs/40-governance/NORMATIVE-BASELINE-APPROVAL-MANIFEST-0.9.0.md",
 "docs/40-governance/NORMATIVE-BASELINE-APPROVAL-CHECKLIST-0.9.0.md",
 "docs/40-governance/NORMATIVE-BASELINE-APPROVAL-UPDATE-MANIFEST-0.9.0.md",
)

def main()->int:
    repo=Path(__file__).resolve().parents[1]
    all_docs=load_documents(repo)
    bundle=bundle_documents(repo)
    ids={d.document_id for d in bundle}
    failures=[]
    req_count=0
    if len(bundle)!=EXPECTED_DOCUMENT_COUNT:
        failures.append(f"expected {EXPECTED_DOCUMENT_COUNT} documents, found {len(bundle)}")
    for d in bundle:
        m=d.metadata
        if m.get('status')!='Approved': failures.append(f"{d.document_id}: status is not Approved")
        if m.get('version')!=BUNDLE_VERSION: failures.append(f"{d.document_id}: version is not {BUNDLE_VERSION}")
        if m.get('approval-review-state')!='approved': failures.append(f"{d.document_id}: approval-review-state is not approved")
        if m.get('approved-on')!=APPROVED_ON: failures.append(f"{d.document_id}: approved-on is not {APPROVED_ON}")
        if m.get('approval-record')!=APPROVAL_ID: failures.append(f"{d.document_id}: approval-record is not {APPROVAL_ID}")
        req_count += len(extract_requirements(d))
        for dep in d.dependencies:
            target=all_docs.get(dep)
            if target is None: failures.append(f"{d.document_id}: unknown dependency {dep}")
            elif dep not in ids and target.metadata.get('status')!='Approved':
                failures.append(f"{d.document_id}: external dependency {dep} is not Approved")
    if req_count!=EXPECTED_REQUIREMENT_COUNT:
        failures.append(f"expected {EXPECTED_REQUIREMENT_COUNT} requirements, found {req_count}")
    _order, cycles=topological_order(bundle)
    for cycle in cycles: failures.append('dependency cycle: '+' -> '.join(cycle))
    for rel in FILES:
        if not (repo/rel).is_file(): failures.append(f"missing approval evidence: {rel}")
    register_path = repo / "docs/40-governance/NORMATIVE-BASELINE-STATUS-REGISTER-0.9.0.md"
    if not register_path.is_file():
        failures.append("missing normative baseline status register")
    else:
        register = register_path.read_text(encoding="utf-8")
        for marker in ["Core Standard | 13 | 545", "C#/.NET-Profil | 8 | 277", "Desktopprofil | 4 | 215", "Operative Prozesse | 7 | 308", "Approved"]:
            if marker not in register:
                failures.append(f"status register missing marker: {marker}")
    approval=(repo/FILES[0]).read_text(encoding='utf-8') if (repo/FILES[0]).exists() else ''
    for marker in ["Approved with documented release conditions", "Robin Görlach", "1.345", "TaskHost Local Wave 01"]:
        if marker not in approval: failures.append(f"approval record missing marker: {marker}")
    result=subprocess.run([sys.executable,str(repo/'tooling/generate-normative-baseline-approval-manifest.py'),'--check'],cwd=repo,check=False)
    if result.returncode: failures.append('approval manifest is stale')
    if failures:
        for f in failures: print('FAIL '+f)
    else:
        print(f"OK   approval bundle: {BUNDLE_NAME}")
        print(f"OK   Approved documents: {len(bundle)}")
        print(f"OK   normative requirements: {req_count}")
        print("OK   approval metadata and evidence are complete")
        print("OK   dependency graph is acyclic and external dependencies are Approved")
    print(f"\nNormative baseline approval failures: {len(failures)}")
    return 1 if failures else 0
if __name__=='__main__':
    sys.exit(main())
