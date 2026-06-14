# The Legibility Field Kit (open core)

"A human approved it" is a location, not a control.

An open-source auditor for AI-touched systems. It flags the defects that
turn governance into theater: changes with no named human owner,
irreversible actions with no gate, and missing OTW receipts (Owner, Time,
Witness).

## Try it in sixty seconds
    git clone https://github.com/forgedculture/legibility-field-kit
    cd legibility-field-kit
    python3 legibility_kit.py audit demo_system

    FINDING [owner] enable feature flag: no named human owner (got 'the team')
    FINDING [reverse] enable feature flag: reversible but time-to-reverse not recorded
    FINDING [otw] enable feature flag: OTW incomplete: no witness
    FINDING [owner] purge old records: no named human owner (got '')
    FINDING [gate] purge old records: irreversible action; needs a delegation gate, not an approval
    FINDING [otw] purge old records: OTW incomplete: no witness
    scanned 3 changes: 6 findings

## What the core checks
- Changes with no named human owner (a team or committee is illegible).
- Irreversible actions with no delegation gate.
- Reversible changes with no recorded time-to-reverse.
- Missing OTW receipts (Owner, Time, Witness).

## Scaffold and score your own system
    python3 legibility_kit.py init ./mysystem     # base governance files
    python3 legibility_kit.py audit ./mysystem    # check the decision record
    python3 legibility_kit.py score ./mysystem    # the three tests, 0 to 6

Zero dependencies, Python 3.8+.

## License
Apache 2.0. See LICENSE.

---

Maintained by Forged Culture. Background reading: The Illegibility Crisis
and the AAAI 2026 paper Echo Systems and the Consequence Boundary. A
commercial kit (AI assistant adapters, a workbook, and templates) is
available at forgedculture.com.
