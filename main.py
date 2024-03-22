from models.operator import Operator
from controllers.routing import RoutingSystem
import os
import argparse


def init_operators():
    data_folder = os.path.join(os.getcwd(), "data")
    operators = []
    for f in os.listdir(data_folder):
        prices = {}
        full_file_path = os.path.join(data_folder, f)

        with open(full_file_path, "r") as file:
            while True:
                data = file.readline()
                if not data:
                    break
                prefix, price = data.strip().split(",")
                prices[prefix] = float(price)

        operator_name = f.split(".")[0]
        operator = Operator(operator_name, prices)
        operators.append(operator)

    return operators


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('phone_number', type=str, help="Input phone number to get the cheapest operator")
    args = parser.parse_args()
    phone_number = args.phone_number

    operators = init_operators()
    routing = RoutingSystem(operators)
    cheapest_operators, cheapest_price = routing.get_cheapest_operators(phone_number)
    
    if cheapest_operators and cheapest_price is not None:
        print(f"Cheapest operator(s): {', '.join(cheapest_operators)} with price {cheapest_price}$")
    else:
        print("There are no operator provides the prefix number")
