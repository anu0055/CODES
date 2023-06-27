import pandas as pd
file = open("C:/Users/ANUBHAV UTKARSH/OneDrive/Desktop/CODES/DataSci/data.csv")
df = pd.read_csv(file)

print(df)

print(df.to_string())
print(pd.options.display.max_rows)