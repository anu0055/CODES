import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/ANUBHAV UTKARSH/OneDrive/Desktop/CODES/DataSci/data.csv")
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()