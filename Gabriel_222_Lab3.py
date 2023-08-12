# -*- coding: utf-8 -*-
"""Write a function in Python with a string such that it accepts a parameter- “stringsplit”. This encoded string will contain your name, domain name and register number. You can separate the values in the string by any number of underscores. [The string should not contain any other underscore symbols in your name, domain name and register number]. The function should return a Python dictionary with your name, domain name and register number._
For example, if the input would be " Aaron___Googleplaystore____2347201”. Then the function should return the output as follows:
{ "name": " Aaron ",
"Domain_name": " Googleplaystore ",
"Regno": "2347201" }

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qC2xLCEEBxdNLZI3FWeIE4PzYa5aIuA5
"""

def string_split(stringsplit):
  name = ""
  domain_name = ""
  regno = ""

  split_string = stringsplit.split("___")
  for item in split_string:
    if item != "":
      if name == "":
        name = item
      elif domain_name == "":
        domain_name = item
      elif regno == "":
        regno = item

  dictionary = {"name": name, "domain_name": domain_name, "regno": regno}

  return dictionary

stringsplit = "Gabriel___StockManagement___2347222"

dictionary = string_split(stringsplit)

print(dictionary)