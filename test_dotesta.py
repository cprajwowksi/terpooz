import unittest
import dotesta

class TestDotesta(unittest.TestCase):

    def test_suma3(self):
        result = suma3.add(10, 2, 3)
        self.assertEqual(result, 15)
