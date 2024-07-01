"""
Q4. Calculate the average delivery time (in timedelta) for Australian shipments.
    Delivery time = interval between collected_at and returned_at columns.
    Assign the final average delivery time to the variable `td`
"""

import pandas as pd

df = pd.read_csv(
    'data/shipments.csv',
    parse_dates=['created_at', 'collected_at', 'returned_at']
    )

# Filter for returned shipments ('status' == 40) and Australian shipments ('country' == 'AU')
filter = (df['status'] == 40) & (df['country'] == 'AU')
au_df = df[filter].copy()

au_df['delivery_time'] = au_df['returned_at'] - au_df['collected_at']

td = au_df['delivery_time'].mean()