import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_invalid(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), None)

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(8), 50)
       
    def test_teenage_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(18), 100)
        
    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(40), 150)

    def test_grans_price(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)

if __name__ == '__main__':
    unittest.main()