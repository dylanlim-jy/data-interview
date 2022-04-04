"""
Q1a. Extract the 'characters' in `json_str` into a list of dictionaries
Q1b. For each dictionary in the list:
        i) Split the 'name' values into 'fname' and 'lname'
        ii) Add 10 to the age of characters who are younger than 40 years old
        iii) Convert the list of dictionaries into three lists, `fname`, `lname`, and `ages`
"""

from data.objects import json_str
print(json_str)

# Initialize lists - these will be used to store your solution
fname, lname, age = ([] for _ in range(3))


# WRITE CODE HERE

# Uncomment the line below to test your solution
# from data.tests import test_q1; test_q1(fname, lname, age)