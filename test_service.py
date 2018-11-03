import unittest
from unittest.mock import patch
from service import Service

class TestService(unittest.TestCase):

    def setUp(self):
        self.serv = Service()
    
    @patch('service.Service.bad_random', return_value=10)
    def test_bad_random(self, args):
        self.assertEqual(self.serv.bad_random(), 10)

    @patch('service.Service.bad_random', return_value=10)
    def test_divide(self, args):
        self.assertEqual(self.serv.divide(5), 2)
        self.assertEqual(self.serv.divide(-5), -2)
        self.assertEqual(self.serv.divide(1), 10)

    def test_abs_plus(self):
        self.assertEqual(self.serv.abs_plus(1), 2)
        self.assertEqual(self.serv.abs_plus(0), 1)
        self.assertEqual(self.serv.abs_plus(-1), 2)

    @patch('service.Service.bad_random', return_value=10)
    def test_complicated_function(self, args):
        self.assertEqual(self.serv.complicated_function(5), (2, self.serv.bad_random()%2))
