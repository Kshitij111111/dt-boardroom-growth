import pandas as pd

# Load CSV, ignore comment lines starting with #
df = pd.read_csv("data/mock_funnel.csv", comment='#')

# Print the first few rows to test
print(df.head())
