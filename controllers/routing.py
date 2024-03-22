from models.operator import Operator
from collections import defaultdict

class RoutingSystem:
    def __init__(self, operators: list[Operator]) -> None:
        self._operators = operators

    def get_cheapest_operators(self, phone_number: str) -> tuple[list, float]:
        price_operators = defaultdict(list)
        cheapest_price = float("inf")

        for op in self._operators:
            prefix, price = op.search_longest_match_prefix_price(phone_number)
            if prefix is not None and price is not None:
                print(f"Found matching prefix '{prefix}' in '{op.name}' with price '{price}$'")
                price_operators[price].append(op.name)
                if price <= cheapest_price:
                    cheapest_price = price
            else:
                print(f"Can not find any matching prefix in {op.name}")

        cheapest_operators = price_operators[cheapest_price]
        cheapest_price = None if cheapest_price == float("inf") else cheapest_price
        
        return (cheapest_operators, cheapest_price)
