import pandas as pd
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def run_mba(file):
    df = pd.read_csv(file)

    # Ensure proper column names
    df.columns = ["Invoice", "Item", "Quantity"]


    # Create Basket Format
    basket = (df.groupby(['Invoice', 'Item'])['Item']
                .count()
                .unstack()
                .fillna(0)
                .applymap(lambda x: 1 if x >= 1 else 0))

    # Apriori Algorithm
    frequent_items = apriori(basket, min_support=0.01, use_colnames=True)

    # Generate Rules
    rules = association_rules(frequent_items, metric="lift", min_threshold=1)

    return rules
