import json
import os
import unittest

import psycopg2

from run import APP


class TestUsers(unittest.TestCase):
    """"
        Class for making tests on sign up
    """

    def setUp(self):
        """
           Method for making the client object
        """
        self.client = APP.test_client
        
    def test_signup(self):
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="dorothy", user_email="dora@gmail.com",
                                                         user_password="asiimwe", admin=True)))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Message', respond)
        self.assertIsInstance(respond, dict)
        # self.assertEqual(result.status_code, 201)
    def test_signup_with_wrong_user_name_type(self):
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name='', user_email="dora@gmail.com",
                                                         user_password="asiimwe",contact="02002002020", admin=False)))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)

    def test_signup_with_wrong_user_type(self):
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="", user_email="dora@gmail.com",
                                                         user_password="asiimwe",contact="02002002020", admin=False)))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
    
    def test_signup_with_without_password(self):
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name='', user_email="dora@gmail.com",
                                                         user_password="",contact="02002002020", admin=False)))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        
    def test_signup_two_times(self):
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="dorothy", user_email="dorothy@gmail.com",
                                                         user_password="asiimwe",contact="02002002020", admin=False)))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 201)

    def test_signup_with_field(self):
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(euser_mail="dorothy@gmail.com",
                                                         user_password="asiimwe",contact="02002002020", admin=False)))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)

    def test_signup_wrong_email(self):
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="dorothy", user_email="dorothygmail.com",
                                                         user_password="asiimwe",contact="02002002020", admin=False)))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)

    def test_login(self):
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="asiimwe", password="dora")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Message', respond)
        self.assertIsInstance(respond, dict)
    
    
    def test_login_with_no_password(self):
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="asiimwe", password="")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Message', respond)
        self.assertIsInstance(respond, dict)
    
    def test_login_with_field(self):
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(password="dora")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Message', respond)
        self.assertIsInstance(respond, dict)

    
       
    
    def test_login2(self):
        """
            Method for tesing the post function which logins in a user
        """
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(email="jgo@gmail.com", password="18181818")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
       

    def test_login3(self):
        """
            Method for tesing the post function which logins in a user
        """
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(email="", password="18181818")))
        self.assertEqual(result.status_code, 400)

    def test_login4(self):
        """
            Method for tesing the post function which logins in a user
        """
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(email="", password="18181818")))

        self.assertEqual(result.status_code, 400)
