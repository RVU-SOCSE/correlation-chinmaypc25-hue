import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df2 = pd.read_csv(r""C:\Users\chinm\Desktop\Python\4laptops.csv"")
sns.heatmap(df2.corr(numeric_only=True),annot=True)
