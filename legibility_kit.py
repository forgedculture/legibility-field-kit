#!/usr/bin/env python3
"""Legibility Field Kit - open-source core auditor (Apache 2.0).

Audits a system definition for legibility defects: changes with no named
human owner, irreversible actions with no gate, missing OTW receipts
(Owner, Time, Witness). The field form of The Illegibility Crisis and the
AAAI paper Echo Systems and the Consequence Boundary. forgedculture.com
"""
import csv, os, sys

BANNED_OWNERS = {"", "team", "the team", "committee", "the committee",
                 "platform", "the platform", "everyone", "nobody", "tbd", "n/a", "-"}

DECISIONS_HEADER = "change,owner,reversible,time_to_reverse,witness,consequence\n"
OTW_HEADER = "decision,system_area,owner,time_or_sla,witness,reversible,consequence\n"
TESTS_TXT = ("# The Three Tests - score each 0, 1, or 2 (see GOVERNANCE.md)\n"
             "explain: 0\nreverse: 0\nowner: 0\n")
GATE_MD = ("# Consequence-Boundary Delegation Gate\n\n"
           "below (reversible, cheap): agents act freely, logged\n"
           "at (costly / hard to reverse): human holds keys; explain first; approval SLA: ____\n"
           "above (irreversible): no delegation, ever\n")
READOUT_MD = ("# Leadership Readout\n\nsystem reviewed:\nlegibility score (0-6):\n"
              "what is governed:\nwhat is theater:\ntop 3 fixes:\n"
              "decision needed from leadership: agree ship/slow/freeze rules now\n")
GOVERNANCE_MD = ("# Legibility governance (base)\n\n"
                 "Run `legibility_kit.py audit .` after every change to the critical system.\n"
                 "Every change needs OTW: a named human Owner, a Time/SLA, a Witness.\n"
                 "Irreversible actions need a gate, not an approval. forgedculture.com\n")
BASE_FILES = {"decisions.csv": DECISIONS_HEADER, "otw_map.csv": OTW_HEADER,
              "tests.txt": TESTS_TXT, "gate.md": GATE_MD, "readout.md": READOUT_MD,
              "GOVERNANCE.md": GOVERNANCE_MD}

def _rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def audit(target):
    dec = os.path.join(target, "decisions.csv")
    if not os.path.isdir(target) or not os.path.exists(dec):
        print("no decisions.csv in %s (run: legibility_kit.py init %s)" % (target, target)); return 2
    rows = _rows(dec); findings = []
    for i, r in enumerate(rows, 2):
        cid = (r.get("change") or ("row %d" % i)).strip()
        owner = (r.get("owner") or "").strip().lower()
        rev = (r.get("reversible") or "").strip().lower()
        ttr = (r.get("time_to_reverse") or "").strip()
        wit = (r.get("witness") or "").strip()
        if owner in BANNED_OWNERS:
            findings.append(("owner", cid, "no named human owner (got %r)" % (r.get("owner") or "")))
        if rev in ("", "unknown", "?"):
            findings.append(("reverse", cid, "reversibility unknown"))
        elif rev in ("yes", "y", "true") and not ttr:
            findings.append(("reverse", cid, "reversible but time-to-reverse not recorded"))
        elif rev in ("no", "n", "false"):
            findings.append(("gate", cid, "irreversible action; needs a delegation gate, not an approval"))
        if not wit:
            findings.append(("otw", cid, "OTW incomplete: no witness"))
    for kind, cid, msg in findings:
        print("FINDING [%s] %s: %s" % (kind, cid, msg))
    print("scanned %d changes: %d findings" % (len(rows), len(findings)))
    return 1 if findings else 0

def score(target):
    path = target if os.path.isfile(target) else os.path.join(target, "tests.txt")
    if not os.path.exists(path):
        print("no tests.txt found"); return 2
    vals = {}
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        try: vals[k.strip().lower()] = int(v.strip())
        except ValueError: pass
    total = sum(vals.get(k, 0) for k in ("explain", "reverse", "owner"))
    if total >= 5: verdict = "legible - keep it that way"
    elif total >= 3: verdict = "drifting - fix before the next incident"
    else: verdict = "illegible - the dashboard is lying to you; start now"
    print("legibility score: %d of 6 -> %s" % (total, verdict))
    return 0

def init(target, engine=None):
    if engine is not None:
        print("the --engine adapters (Claude skill, ChatGPT setup, AGENTS.md) are part of the paid kit.")
        print("the open core scaffolds the base only. get the kit: forgedculture.com")
        return 2
    os.makedirs(target, exist_ok=True)
    for name, body in BASE_FILES.items():
        with open(os.path.join(target, name), "w", encoding="utf-8") as f:
            f.write(body)
    print("scaffolded base legibility kit in %s" % target)
    return 0

def _parse(argv):
    engine = None
    if "--engine" in argv:
        i = argv.index("--engine"); engine = argv[i + 1] if i + 1 < len(argv) else "all"
        argv = argv[:i] + argv[i + 2:]
    cmd = argv[0] if argv else "help"
    target = argv[1] if len(argv) > 1 else "."
    return cmd, target, engine

def main(argv):
    cmd, target, engine = _parse(argv)
    if cmd == "audit": return audit(target)
    if cmd == "score": return score(target)
    if cmd == "init": return init(target, engine)
    print("legibility_kit.py - open-source legibility auditor (Apache 2.0)\n"
          "  audit <dir>   check decisions.csv for legibility defects\n"
          "  score <dir>   run the Three Tests from tests.txt\n"
          "  init  <dir>   scaffold the base governance files\n"
          "the paid kit adds AI adapters and the workbook. forgedculture.com")
    return 0
# === end of core (kit extension appends below this marker) ===
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
