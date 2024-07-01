"""
Q3. Inspect `shipments.csv` as a pandas DataFrame. 
    Assign the shop ID with the highest number of faulty products to `shop`, 
    and the number of faulty products for this shop to `products`.
"""

import pandas as pd
import json

# Load dataframes
shipments = pd.read_csv('data/shipments.csv', parse_dates=['created_at', 'collected_at', 'returned_at'])
reasons = pd.json_normalize(shipments.notes.apply(json.loads))

# Merge dataframes
merged = pd.concat([shipments, reasons], axis=1)

# Determine shop with highest number of faulty products
pivoted = merged.groupby('shop_id')['reason'].value_counts()
max_index = pivoted.iloc[pivoted.index.get_level_values('reason') == 'Faulty'].idxmax()
products = pivoted.loc[max_index]
shop, category = max_index