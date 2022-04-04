"""
Q2. Write a function to add `n` days to each element in a `list` that is in a specific `year` and `month`.
Test this function with the arguments n=5, list=date_list, year=2021, month=12
"""

from data.objects import date_list

def add_days(n, list, y, m):
    """Adds `n` number of days to each date element of `list`,
    where the date is in the specified `year` and `month`.

    Returns the original list with dates changed
    """
    # WRITE CODE HERE
    
    return list


output = add_days(5, date_list, 2021, 12)

# Uncomment the line below to test your solution
# from data.tests import test_q2; test_q2(output)