import pandas as pd
df = pd.read_csv("C:/Users/ANUBHAV UTKARSH/OneDrive/Desktop/CODES/DataSci/data.csv")
'''print(df.duplicated()) To detect the duplicated value'''
df.drop_duplicates(inplace = True)
print(df.to_string()) #Now the data is clean

