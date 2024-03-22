from models.operator import Operator
import unittest

class OperatorTest(unittest.TestCase):

    def test_no_prefix_match(self):
        operator = self._create_data()
        prefix, price = operator.search_longest_match_prefix_price("325819462")
        self.assertIsNone(prefix)
        self.assertIsNone(price)


    def test_only_match_one_prefix(self):
        operator = self._create_data()
        prefix, price = operator.search_longest_match_prefix_price("268141613")
        self.assertEqual(prefix, "268")
        self.assertEqual(price, 5.1)

    def test_match_multiple_prefixes(self):
        operator = self._create_data()
        prefix, price = operator.search_longest_match_prefix_price("467341324")
        self.assertEqual(prefix, "4673")
        self.assertEqual(price, 0.9)

    
    def _create_data(self):
        operator_prices = {
            "1": 0.9,
            "268": 5.1,
            "46": 0.17,
            "4620": 0.0,
            "468": 0.15,
            "4631": 0.15,
            "4673": 0.9,
            "46732": 1.1,
        }

        operator = Operator("operator_a", operator_prices)
        return operator
