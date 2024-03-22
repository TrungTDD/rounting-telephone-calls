from controllers.routing import RoutingSystem
from models.operator import Operator
import unittest

class RoutingOperatorTest(unittest.TestCase):
    
    def test_no_cheapest_operator(self):
        routing = self._create_data()
        cheapest_operators, cheapest_price = routing.get_cheapest_operators("969174613")
        self.assertEqual(cheapest_operators, [])
        self.assertIsNone(cheapest_price)

    def test_get_single_cheapest_operator(self):
        routing = self._create_data()
        cheapest_operators, cheapest_price = routing.get_cheapest_operators("4613123671")
        self.assertEqual(cheapest_operators, ["operator_a"])
        self.assertEqual(cheapest_price, 0.17)

    def test_get_multiple_cheapest_operators(self):
        routing = self._create_data()
        cheapest_operators, cheapest_price = routing.get_cheapest_operators("2681645123")
        self.assertEqual(cheapest_operators, ["operator_a", "operator_b"])
        self.assertEqual(cheapest_price, 5.1)

    def _create_data(self):
        operator_a_prices = {
            "1": 0.9,
            "268": 5.1,
            "46": 0.17,
            "4620": 0.0,
            "468": 0.15,
            "4631": 0.15,
            "4673": 0.9,
            "46732": 1.1,
        }

        operator_a = Operator("operator_a", operator_a_prices)

        operator_b_prices = {
            "1": 0.92,
            "44": 0.5,
            "46": 0.2,
            "467": 1.0,
            "48": 1.2,
            "26": 5.1,
        }

        operator_b = Operator("operator_b", operator_b_prices)

        routing = RoutingSystem([operator_a, operator_b])
        return routing
