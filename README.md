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

## Optional self-service kit

The auditor above is free. The [Legibility Field Kit ($49)](https://forgedculture.com/b/kf65n)
adds a field workbook, OTW templates and AI assistant setup instructions
for teams that want to run their own assessment.
The same kit is available through the [Heron shop](https://shop.theherongroupllc.com/products/legibility-field-kit?utm_source=github&utm_medium=referral&utm_campaign=legibility_field_kit_cli). The paid files are licensed
for internal use. They do not certify compliance or replace a professional audit.

## Independent action-path review for release teams

The free auditor and $49 kit support your own assessments. If an AI agent is
about to spend money, change a customer account, or invoke privileged tools,
a separate specialist review can help document whether one nonproduction
action path actually obeys its stated authority and escalation rules.

Forged Culture offers a fixed-scope [Agent Action Assurance Sprint](https://shop.theherongroupllc.com/pages/agent-action-assurance-sprint?utm_source=github&utm_medium=referral&utm_campaign=agent_assurance_service)
for this release decision. Engagements require an agreed SOW and evidence
boundary before payment. This is not a penetration test, compliance
certification, or production-safety guarantee.

## License
Apache 2.0. See LICENSE.

---

Maintained by Forged Culture. Background reading: [The Illegibility Crisis](https://leanpub.com/illegibility_crisis)
and the AAAI 2026 paper Echo Systems and the Consequence Boundary. A
commercial kit (AI assistant adapters, a workbook, and templates) is
available at forgedculture.com.
