import io
import sys

from app import app

class TestApp:
    '''Flask application in app.py'''

    def test_index_route(self):
        '''has a resource available at "/".'''
        response = app.test_client().get('/')
        assert(response.status_code == 200)

    def test_index_text(self):
        '''displays "Welcome to Flatiron Cars" in for '/' route in browser.'''
        response = app.test_client().get('/')
        assert(response.data.decode() == 'Welcome to Flatiron Cars')

    def test_model_route(self):
        '''has a resource available at "/<model>".'''
        response = app.test_client().get('/Beedle')
        assert(response.status_code == 200)

    def test_model_text(self):
        '''displays text of '/<model> route in browser.'''
        response = app.test_client().get('/Crossroads')
        assert(response.data.decode() == 'Flatiron Crossroads is in our fleet!')
    
    def test_model_failure_text(self):
        '''displays failure text of '/<model> route in browser.'''

        response = app.test_client().get('/realCar')
        assert(response.data.decode() == 'No models called realCar exists in our catalog')
