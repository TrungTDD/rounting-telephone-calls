from helper.utils import is_digit
from typing import Optional


class Node:
    def __init__(self):
        self.children = {}
        self.price = None


class Operator:
    def __init__(self, name: str, prefix_prices: dict) -> None:
        self.name = name
        self._root = Node()
        self._build_tree(prefix_prices)

    def search_longest_match_prefix_price(
        self, phone_number: str
    ) -> Optional[tuple[str, float]]:
        if not is_digit(phone_number):
            raise Exception("Error format phone number")

        # get longest matching prefix by iterating from left to right
        matching_prefix = None
        matching_price = None

        for i in range(1, len(phone_number) + 1):
            prefix = phone_number[:i]
            node = self._search(prefix)
            if node is None:
                break
            elif node.price is not None:
                matching_prefix = prefix
                matching_price = node.price

        return (matching_prefix, matching_price)

    def _build_tree(self, prefix_prices: dict) -> None:
        for prefix, price in prefix_prices.items():
            self._insert_node(prefix, price)

    def _insert_node(self, prefix: str, price: float) -> None:
        curr = self._root
        for p in prefix:
            if p not in curr.children:
                curr.children[p] = Node()
            curr = curr.children[p]

        curr.price = price

    def _search(self, prefix: str) -> Optional[Node]:
        curr = self._root
        for p in prefix:
            if p not in curr.children:
                return None
            curr = curr.children[p]

        return curr
