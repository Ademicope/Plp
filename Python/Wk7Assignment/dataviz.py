import matplotlib.pyplot as plt
import pandas as pd

# Task 1
df = pd.read_csv('winequality-white.csv', sep=';')

pd.set_option('display.max_columns', None)
sampled_df = df.sample(frac=0.1, random_state=42)
s_df = sampled_df
#print(df.head())

# Task 2
#print(df.describe())

# Task 3
plt.scatter(s_df.index, s_df['citric acid'], color='orange', label='Citric Acid', alpha=0.5)
plt.scatter(s_df.index, s_df['residual sugar'], color='blue', label='Residual Sugar', alpha=0.5)
plt.title('Citric acid and Residual sugar')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.legend()
plt.show()