"""
Q4. Calculate the average delivery time (in timedelta) for Australian shipments.
    Delivery time = interval between collected_at and returned_at columns.
    Assign the final average delivery time to the variable `td`
"""

import pandas as pd

df = pd.read_csv(
    'data/shipments.csv',
    # ADD ANY ADDITIONAL ARGS 
    )

# Filter for returned shipments ('status' == 40) and Australian shipments ('country' == 'AU')
# WRITE CODE HERE

# Assign your answer to the following variable
# td = 

# Uncomment the line below to test your solution
# from data.tests import test_q4; test_q4(td)