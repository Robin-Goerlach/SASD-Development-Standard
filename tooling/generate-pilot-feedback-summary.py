#!/usr/bin/env python3
"""Generate a compact pilot feedback summary from PILOT-FEEDBACK-LOG.md."""
from __future__ import annotations
import argparse, re, sys
from collections import Counter
from pathlib import Path
DATE="2026-07-24"; VERSION="0.8.0"
ROW=re.compile(r"^\| (SASD-PFB-\d{3}) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| (Candidate|Accepted|Deferred|Rejected|Confirmed) \|$", re.M)

def render(repo:Path)->str:
    source=(repo/'docs/50-reference-implementations/PILOT-FEEDBACK-LOG.md').read_text(encoding='utf-8')
    rows=ROW.findall(source); counts=Counter(r[5] for r in rows)
    out=['---','title: "Pilotfeedback-Zusammenfassung"','document-id: SASD-REF-PILOT-005','document-type: informative','status: Draft',f'version: {VERSION}','standard-version: "1.0"','language: de','authoritative: false','owner: SASD Development Standard Maintainer',f'last-updated: {DATE}','applies-to-quality-levels: [Minimum, Recommended, Production]','applies-to-profiles: [Core, DotNet, Desktop]','depends-on: [SASD-REF-PILOT-004]','---','','# Pilotfeedback-Zusammenfassung','','Diese Datei wird aus `PILOT-FEEDBACK-LOG.md` erzeugt.','',f'- Feedbackeinträge: **{len(rows)}**']
    for key in ['Accepted','Confirmed','Candidate','Deferred','Rejected']:
        out.append(f'- {key}: **{counts.get(key,0)}**')
    out += ['', '| Feedback-ID | Pilot | Bereich | Status |', '|---|---|---|---|']
    for fid,pilot,obs,area,decision,status in rows:
        out.append(f'| {fid} | {pilot.strip()} | {area.strip()} | {status} |')
    out.append('')
    return '\n'.join(out)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); args=ap.parse_args(); repo=Path(__file__).resolve().parents[1]; target=repo/'docs/50-reference-implementations/PILOT-FEEDBACK-SUMMARY.md'; generated=render(repo)
    if args.check:
        if not target.exists() or target.read_text(encoding='utf-8') != generated: print('FAIL pilot feedback summary is not current'); return 1
        print('OK   pilot feedback summary is current'); return 0
    target.write_text(generated,encoding='utf-8',newline='\n'); print(f'Wrote {target.relative_to(repo)}'); return 0
if __name__=='__main__': sys.exit(main())
