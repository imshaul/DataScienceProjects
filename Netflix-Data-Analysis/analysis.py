import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
print(df.head())
print(df.tail())
print(df.columns)

print(df.info())
print("Missing values: ")

df.drop_duplicates(inplace=True)
df["director"]=df["director"].fillna("Unknown")
df["cast"]=df["cast"].fillna("Unknown")
df["country"]=df["country"].fillna("Unknown")
df["date_added"]=df["date_added"].fillna("Unknown")
df["rating"]=df["rating"].fillna("Unknown")
print(df.isnull().sum())

print(df["type"].value_counts())
df["type"].value_counts().plot(kind="bar")
plt.title("Movies vs Show")
plt.ylabel("Count")
plt.show()

df["country"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries")
plt.show()



genres = df["listed_in"].str.split(", ")
print(genres.head())
all_genres = genres.explode()
all_genres.value_counts().head(10).plot(kind="bar")
plt.title("Top Genres on Netflix")
plt.ylabel("number of titles")
plt.show()

df["release_year"].value_counts().sort_index().plot()
plt.title("Netflix Content Over Time")
plt.xlabel("Year")
plt.ylabel("Number of titles")
plt.show()

print("Content Ratings")
print(df["rating"].value_counts().head())
df["rating"].value_counts().plot(kind="bar")
plt.title("Ratings")
plt.show()