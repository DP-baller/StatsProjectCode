import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

y = pd.read_csv('SoftDrink.csv')

plt.pie(y['Brand Purchased'].value_counts(), labels =y['Brand Purchased'].unique(), autopct='%1.1f%%')
plt.show() 