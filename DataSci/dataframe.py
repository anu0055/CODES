import pandas as pd
data = {
    'calories': [470,350,400],
    'duration': [50,40,45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df, "\n")
print(df.loc["day1"], "\n")

#use a list of indexes:
print(df.loc[["day1", "day2"]])