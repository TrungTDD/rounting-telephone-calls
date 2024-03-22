# 1. Implementation

In order to implement the solution for the coding assignment, I will use Trie (Prefix Tree).In here, the reason I don't want to use HashMap, because by using Trie, we can quickly eliminate the prefix that is not belong the price list. So that it can increase the performance.

The implementation will have two main classes:
 - `Operator`: The class reflects for each operator that existing in the system, this class will construct the Trie base on the input price list, and also contains the function to look for the price from input phone number
 - `RoutingSystem`: That is the controller of the system, where will take in charge of handling the main logic to get the operator which has the cheapest price

*NOTE*: In case, there are multiple operators which have the same cheapest price, we will return all operators.

# 2. Setup environment

For this application, we will manage the environment by using `virtualenv`, so first please ensure you already installed `virtualenv`, if not run the following command:
```
pip install virtualenv
```

Then, start to run the commands below to setup environment:

```python
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

# 3. Setup data

To initialize the operator's price list, we will create file for each operator that we want to input. The name of the operator is also the name of the txt file, and followed by format: `operator_<operator_name>.txt` and the data must be placed in `data` folder.
In the data file, the price will be separated by line, and for each line, the record is formatted by: `<number_prefix>,<price>`

For example: Operator A - `operator_a.txt`

```
1,0.9
268,5.1
46,0.17
4620,0.0
468,0.15
4631,0.15
4673,0.9
46732,1.1
```

# 4. Run application
In order to run application, use the command: 
```python
python main.py <phone_number>
```

# 5. Tests

In order to run application, use the command: 
```python
pytest
```