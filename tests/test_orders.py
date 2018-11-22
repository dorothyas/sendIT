"""
    Module for making tests on the app for sign up
"""
import unittest
import json
from run import APP
from api.models.db import Connection


class TestViews(unittest.TestCase):
    """"
        Class for making tests on sign up
    """

    def setUp(self):
        """
           Method for making the client object
        """
        self.client = APP.test_client


    def test_get_post_orders(self):
        result = self.client().post('/api/v1/parcels')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 401)
        self.assertIn('msg', respond)
        self.assertIsInstance(respond, dict)
        
    def test_get_all_orders(self):
        result = self.client().get('/api/v1/parcels')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 401)
        self.assertIn('msg', respond)
        self.assertIsInstance(respond, dict)

    def test_one_order(self):
  
        result = self.client().get('/api/v1/parcels/1')
        result2 = self.client().get('/api/v1/parcels/q')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 401)
        self.assertEqual(result2.status_code, 404)
        self.assertIsInstance(respond, dict)

    def test_update_status(self):
        result = self.client().put('/api/v1/parcels/<int:order_id>/status')
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('msg', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 401)
        self.assertTrue(result.json["msg"])

    def test_update_present_location(self):
        """
            Method for testing the update function to update location
        """
        result = self.client().put('/api/v1/parcels/<int:order_id>/location')
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('msg', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 401)
        self.assertTrue(result.json["msg"])
       

    