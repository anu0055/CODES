import pandas as pd
df = pd.read_csv("C:/Users/ANUBHAV UTKARSH/OneDrive/Desktop/CODES/DataSci/data.csv")
new_df = df.dropna() #This creates a new dataframe
print(new_df.to_string())

# To change the original dataframe :
'''
df.dropna(inplace = True)
print(df.to_string())'''

#To fill the null data:
'''
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)'''