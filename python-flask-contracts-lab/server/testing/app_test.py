import io
import sys

from app import app

class TestApp:
    '''Flask application in app.py'''

    def test_contract_route(self):
        '''has a resource available at "/contract/<id>".'''
        response = app.test_client().get('/contract/1')
        assert(response.status_code == 200)

    def test_contract_data(self):
        '''Returns correct contract_information data'''
        response = app.test_client().get('/contract/1')
        print(response.data)
        assert(response.data == b'This contract is for John and building a shed')

    def test_contract_failure(self):
        ''''/contract/<is> route is a 404 if contract does not exists'''

        response = app.test_client().get('/contract/100')
        assert(response.status_code == 404)

    def test_customer_route(self):
        '''has a resource available at "/customer/<customer_name>".'''
        response = app.test_client().get('/customer/bob')
        assert(response.status_code == 204)

    def test_customer_data(self):
        '''returns response body of "" for customer'''
        response = app.test_client().get('/customer/bob')
        assert(response.data == b"")
    
    def test_customer_failure(self):
        ''''/customer/<customer_name> route is a 404 if customer does not exists'''

        response = app.test_client().get('/customer/mario')
        assert(response.status_code == 404)
