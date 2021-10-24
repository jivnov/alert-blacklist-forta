from forta_agent import Finding, FindingSeverity, FindingType
from src.const import CONTRACT_ADDRESS, BLACKLISTED_ADDRESSES


def handle_transaction(transaction_event):
    findings = []
    address_from = transaction_event.from_
    address_to = transaction_event.to
    if address_to != CONTRACT_ADDRESS:
        return findings
    if address_from in BLACKLISTED_ADDRESSES:
        findings.append(Finding({
            'name': 'Blacklisted address',
            'description': f'Blacklisted address {address_from} interacting with Compound Protocol',
            'alert_id': 'FORTA-BLACKLISTED-ADDRESS',
            'type': FindingType.Suspicious,
            'severity': FindingSeverity.Critical,
            'metadata': {
                'address': address_from
            }
        }))

    return findings
