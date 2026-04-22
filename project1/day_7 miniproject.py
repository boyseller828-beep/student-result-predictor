import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

# Math bar chart
plt.bar(df["Name"], df["Math"])
plt.title("Math Marks")
plt.show()

# Science bar chart ✅
plt.bar(df["Name"], df["Science"])
plt.title("Science Marks")
plt.show()

# English bar chart ✅
plt.bar(df["Name"], df["English"])
plt.title("English Marks")
plt.show()
plt.scatter(df["Math"], df["Science"])
plt.xlabel("Math")
plt.ylabel("Science")
plt.title("Math vs Science")
plt.show()

# Average line chart
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

plt.plot(df["Name"], df["Average"])
plt.title("Average Marks")
plt.show()








