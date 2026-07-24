#!/usr/bin/env python3
"""Validate reference-pilot manifests, evidence states and documentation."""
from __future__ import annotations
import hashlib, json, re, subprocess, sys
from pathlib import Path
VALID_STATUSES={"Candidate","Selected","Baseline Assessed","Wave Planned","In Execution","Wave Validated","Pilot Closed"}
VALID_LEVELS={"Minimum","Recommended","Production"}
VALID_IMPL={"Not Started","Artifact Prepared","Committed","Verified"}
VALID_VERIFY={"Pending","Partial","Passed","Failed"}
REQUIRED_KEYS={"schema_version","pilot_id","title","target_repository","category","project_size","quality_level","profiles","status","baseline_date","standard_documents","execution_statement","documents"}
REQUIRED_DOCUMENT_KEYS={"charter","classification","baseline","gaps","migration_plan","wave_01","evidence","decisions","review"}
V11_KEYS={"implementation_state","verification_state","current_wave","target_commit","implementation_artifact"}
V11_DOCUMENTS={"implementation_review","verification_plan","interim_retrospective"}
PILOT_ID_RE=re.compile(r"^SASD-PILOT-\d{3}$")
GAP_ID_RE=re.compile(r"^\|\s*P\d{2}-GAP-\d{3}\s*\|",re.M)
DECISION_ID_RE=re.compile(r"^\|\s*P\d{2}-DEC-\d{3}\s*\|",re.M)
SHA_RE=re.compile(r"^[0-9a-f]{64}$")

def main()->int:
    repo=Path(__file__).resolve().parents[1]; base=repo/'docs/50-reference-implementations'; manifests=sorted(base.glob('pilot-*/pilot.json')); failures=0; ids=set()
    if not manifests: print('FAIL no pilot manifests found'); return 1
    for manifest in manifests:
        rel=manifest.relative_to(repo); errors=[]
        try: data=json.loads(manifest.read_text(encoding='utf-8'))
        except Exception as exc: print(f'FAIL {rel}: invalid JSON: {exc}'); failures+=1; continue
        missing=sorted(REQUIRED_KEYS-data.keys())
        if missing: errors.append('missing keys: '+', '.join(missing))
        pid=data.get('pilot_id','')
        if not PILOT_ID_RE.match(pid): errors.append(f'invalid pilot_id: {pid!r}')
        elif pid in ids: errors.append(f'duplicate pilot_id: {pid}')
        ids.add(pid)
        if data.get('status') not in VALID_STATUSES: errors.append(f'invalid status: {data.get("status")!r}')
        if data.get('quality_level') not in VALID_LEVELS: errors.append(f'invalid quality level: {data.get("quality_level")!r}')
        if not isinstance(data.get('profiles'),list) or 'Core' not in data.get('profiles',[]): errors.append('profiles must be a list containing Core')
        docs=data.get('documents',{})
        if not isinstance(docs,dict): errors.append('documents must be an object'); docs={}
        required_docs=set(REQUIRED_DOCUMENT_KEYS)
        if data.get('schema_version')=='1.1':
            missing_v11=sorted(V11_KEYS-data.keys())
            if missing_v11: errors.append('missing schema 1.1 keys: '+', '.join(missing_v11))
            required_docs |= V11_DOCUMENTS
            if data.get('implementation_state') not in VALID_IMPL: errors.append('invalid implementation_state')
            if data.get('verification_state') not in VALID_VERIFY: errors.append('invalid verification_state')
            artifact=data.get('implementation_artifact')
            if not isinstance(artifact,dict): errors.append('implementation_artifact must be an object')
            else:
                if not SHA_RE.match(str(artifact.get('sha256',''))): errors.append('invalid artifact sha256')
                if not isinstance(artifact.get('file_count'),int) or artifact.get('file_count',0)<1: errors.append('invalid artifact file_count')
            if data.get('implementation_state')=='Verified' and data.get('verification_state')!='Passed': errors.append('Verified implementation requires Passed verification')
            if data.get('status')=='Wave Validated' and data.get('verification_state')!='Passed': errors.append('Wave Validated requires Passed verification')
        missing_docs=sorted(required_docs-docs.keys())
        if missing_docs: errors.append('missing document mappings: '+', '.join(missing_docs))
        for key,filename in docs.items():
            if not (manifest.parent/filename).is_file(): errors.append(f'missing mapped document {key}: {filename}')
        gap=manifest.parent/docs.get('gaps','')
        if gap.is_file() and not GAP_ID_RE.search(gap.read_text(encoding='utf-8')): errors.append('gap register has no pilot gap IDs')
        dec=manifest.parent/docs.get('decisions','')
        if dec.is_file() and not DECISION_ID_RE.search(dec.read_text(encoding='utf-8')): errors.append('decision log has no pilot decision IDs')
        if errors:
            failures+=1; print(f'FAIL {rel}'); [print('  - '+e) for e in errors]
        else: print(f'OK   {rel}: {pid} ({data["status"]}; {data.get("implementation_state","—")}/{data.get("verification_state","—")})')
    for script in ['generate-pilot-portfolio.py','generate-pilot-feedback-summary.py']:
        result=subprocess.run([sys.executable,str(repo/'tooling'/script),'--check'],cwd=repo,text=True,capture_output=True)
        print(result.stdout.strip())
        if result.returncode: failures+=1
    print(f'Validated {len(manifests)} pilot manifests; failures: {failures}')
    return 1 if failures else 0
if __name__=='__main__': sys.exit(main())
