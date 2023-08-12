stocks = ["stock_name", "stock_symbol", "stock_price"]

stocks.append("stock_exchange")
stocks.append("stock_date")

stocks.insert(1, "stock_id")
stocks.insert(3, "stock_value")

stocks.extend((1, 2, 3))

stocks.extend({"apple", "microsoft", "google"})

"""The resulting list is:


['stock_name', 'stock_id', 'stock_symbol', 'stock_value', 'stock_price', 'stock_exchange', 'stock_date', 1, 2, 3, 'microsoft', 'google', 'apple']

**Create a list with numeric and perform the following operations.**
"""

numbers = [1, 2, 3, 4, 5]

first_element = numbers[0]
last_element = numbers[-1]
numbers[0] = last_element
numbers[-1] = first_element

sum_of_digits = 0
for number in numbers:
    sum_of_digits += sum(int(digit) for digit in str(number))

smallest_element = min(numbers)

"""The resulting list is:

```
[5, 2, 3, 4, 1]
```

The sum of the digits in the list is:

```
15
```

The smallest element in the list is:

```
1
```

* **Write a program to swap the first and last elements in a list.**
"""

def swap_first_last_elements(list):
    first_element = list[0]
    last_element = list[-1]
    list[0] = last_element
    list[-1] = first_element

    return list


print(swap_first_last_elements([1, 2, 3, 4, 5]))

"""This code will print the following output:

```
[5, 2, 3, 4, 1]
```

* **Write a program to find the sum of the digits in a list.**
"""

def sum_of_digits(list):
    sum_of_digits = 0
    for number in list:
        sum_of_digits += sum(int(digit) for digit in str(number))

    return sum_of_digits


print(sum_of_digits([1, 2, 3, 4, 5]))

"""This code will print the following output:

```
15
```

* **Write a program to find the smallest element in a list.**
"""

def smallest_element(list):
    smallest_element = min(list)

    return smallest_element


print(smallest_element([1, 2, 3, 4, 5]))

"""This code will print the following output:

```
1
```
"""
