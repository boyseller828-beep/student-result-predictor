import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Math": [80, None, 90, 70],
    "Science": [70, 85, None, 60],
    "English": [90, 80, 92, None]
}

df = pd.DataFrame(data)

df.fillna(df.mean(numeric_only=True), inplace=True)
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

print(df)






