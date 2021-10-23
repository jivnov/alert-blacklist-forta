from forta_agent import create_transaction_event
from agent import handle_transaction
from src.const import CONTRACT_ADDRESS


class TestAgent:
    def test_white_list(self):
        tx_event = create_transaction_event(
            {'transaction': {
                'from': "0xWHTLST",
                'to': CONTRACT_ADDRESS,
            }})

        findings = handle_transaction(tx_event)

        assert len(findings) == 0

    def test_black_list(self):
        tx_event = create_transaction_event(
            {'transaction': {
                'from': "0xBLCKLST1",
                'to': CONTRACT_ADDRESS,
            }})

        findings = handle_transaction(tx_event)

        assert len(findings) > 0
        finding = findings[0]
        assert finding.name == "Blacklisted address"
        assert finding.description == 'Blacklisted address 0xBLCKLST1 interacting with Compound Protocol'