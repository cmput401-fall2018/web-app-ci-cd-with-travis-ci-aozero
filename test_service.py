from unittest import TestCase
from unittest.mock import patch
from service import Service

class TestService(unittest.TestCase):

    def setUp(self):
        self.serv = Service()
    
    @patch('service.Service.bad_random', return_value=10)
    def test_bad_random(self):
        self.assertEqual(self.serv.badrandom(), 10)

    # Test this
    def test_divide(self, y):
        return self.bad_random() / y

    # Test this
    def test_abs_plus(self):
        self.assertEqual(self.serv.abs_plus(1), 2)
        self.assertEqual(self.serv.abs_plus(0), 1)
        self.assertEqual(self.serv.abs_plus(-1), 2)

    # Test this
    def test_complicated_function(self, x):
        return self.divide(x), self.bad_random() % 2
