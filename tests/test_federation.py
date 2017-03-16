# coding:utf-8

from nose.tools import raises
import mock
from stellar_base.federation import *


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code
        def json(self):
            import json
            return json.loads(self.text)
    if args[0] == 'https://www.fed-domain.com/federation'and \
       kwargs['params'] == {'q': 'fed*fed-domain.com', 'type': 'name'}:
        return MockResponse('{"account_id": "GBTCBCWLE6YVTR5Y5RRZC36Z37OH22G773HECWEIZTZJSN4WTG3CSOES",  \
                              "memo_type": "text", "memo": "AIHHklPLdS9w3CcTH0fMI1Fq8fuW", \
                              "stellar_address": "1CqDFDxR9Tv696j86PwtyxhA5p9ev1EviJ*naobtc.com"}',  \
                              200)
    if args[0] == 'https://fed-domain.com/.well-known/stellar.toml':
        return MockResponse('FEDERATION_SERVER="https://www.fed-domain.com/federation"\n  \
                             [[CURRENCIES]]  \n   code="BTC"     \n\
                             issuer="GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH"', \
                             200)

    return MockResponse({}, 404)

class TestFederation(object):

    @raises(FederationError)
    def test_federation_false_address_1(self):
        federation('false_address')

    @raises(FederationError)
    def test_federation_false_address_2(self):
        federation('false_address*')

    @raises(FederationError)
    def test_federation_false_address_3(self):
        federation('false*address')

    @raises(FederationError)
    @mock.patch('stellar_base.federation.get_federation_service')
    def test_federation_none_service(self,get_service):
        get_service.return_value = None
        federation('fed*stellar.org')

    @mock.patch('stellar_base.federation.requests.get', side_effect=mocked_requests_get)
    @mock.patch('stellar_base.federation.get_federation_service')
    def test_federation_normal_service(self, mock_service, mock_get):
        mock_service.return_value = 'https://www.fed-domain.com/federation'
        response =  federation('fed*fed-domain.com')
        assert response.get('account_id') == 'GBTCBCWLE6YVTR5Y5RRZC36Z37OH22G773HECWEIZTZJSN4WTG3CSOES'


    @mock.patch('stellar_base.federation.requests.get', side_effect=mocked_requests_get)
    def test_get_toml(self,get_toml):
        response = get_stellar_toml('fed-domain.com')
        assert response.get('FEDERATION_SERVER') == "https://www.fed-domain.com/federation"

    @mock.patch('stellar_base.federation.requests.get', side_effect=mocked_requests_get)
    def test_get_fed_service(self,get_toml):
        response = get_federation_service('fed-domain.com')
        assert response == "https://www.fed-domain.com/federation"

    @mock.patch('stellar_base.federation.requests.get', side_effect=mocked_requests_get)
    def test_get_auth_server(self,get_toml):
        response = get_auth_server('fed-domain.com')
        assert response == None
