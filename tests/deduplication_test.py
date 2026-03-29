import pandas as pd

# Sample Data
df = pd.DataFrame({
    'id': [1, 2, 2, 3],
    'name': ['A', 'B', 'B', 'C']
})

# Remove duplicates
df_clean = df.drop_duplicates()
