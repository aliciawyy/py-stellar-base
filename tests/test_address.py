from unittest import TestCase
import mock

from stellar_base.keypair import Keypair
from stellar_base import address as adr


class AddressTest(TestCase):
    def setUp(self):
        patcher = mock.patch(adr.__name__ + ".Horizon")
        self.mock_horizon = patcher.start()
        self.addCleanup(patcher.stop)
        self.key_pair = Keypair.deterministic(
            'illness spike retreat truth genius clock brain pass '
            'fit cave bargain toe'
        )
        self.address = adr.Address(self.key_pair.address_str)

    def test_from_secret(self):
        address1 = adr.Address(self.key_pair.address_str)
        address2 = adr.Address.from_secret(self.key_pair.seed())
        assert address1.address == address2.address

    def test_network(self):
        address = adr.Address(self.key_pair.address_str)
        assert "TESTNET" == address.network
        address2 = adr.Address(self.key_pair.address_str, "public")
        assert "PUBLIC" == address2.network
