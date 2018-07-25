
import unittest
import os
import json
from api import app
from flask import jsonify

class Test_api(unittest.TestCase):

    def setUp(self):
       """Initialise Tests"""

       self.app = app.test_client()

    def tearDown(self):
        print('tearDown\n')



    def test_returnAll(self):
        response = self.app.get('/api/v1/mydiary/allmassages', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_returnOne(self):
        self.app.post('/api/v1/mydiary/allmassages/', data={'Date': '20/Jan/2018','Title': 'A Fire Upon the Deep','Msg': 'The coldsleep itself was dreamless.With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.'})
        response = self.app.get('/api/v1/mydiary/allmassages/0')
        self.assertEqual(response.status_code, 200)