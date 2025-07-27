import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")


df = pd.merge(ratings, movies, on="movieId")
movie_stats = df.groupby("title")["rating"].agg(["mean", "count"])
top_film = movie_stats[movie_stats["count"] >= 50].sort_values("mean", ascending=False).head(10).reset_index()

plt.figure(figsize=(15, 10))
sns.barplot(x="mean", y="title", hue="title", data=top_film, palette="viridis", legend=False)
plt.title("Top 10 Highest Rated Movies (min 50 ratings)")
plt.xlabel("Average Rating")
plt.ylabel("Movie Title")
plt.tight_layout()
plt.show()

#########################################################

famous_movies = movie_stats.sort_values("count", ascending=False).head(10).reset_index()

plt.figure(figsize=(15, 10))
sns.barplot(x="count", y="title", data=famous_movies, palette="magma")
plt.title("Top 10 Most Rated Movies")
plt.xlabel("Number of Ratings")
plt.ylabel("Movie Title")
plt.tight_layout()
plt.show()

#########################################################

df_explode = df.copy()
df_explode["genres"] = df_explode["genres"].str.split("|")
df_explode = df_explode.explode("genres")
rating_genre = df_explode.groupby("genres")["rating"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(15, 10))
sns.barplot(x=rating_genre.values, y=rating_genre.index, palette="coolwarm")
plt.title("Top 10 Genres by Average Rating")
plt.xlabel("Average Rating")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()

#########################################################

count_genre = df_explode["genres"].value_counts().head(20)

plt.figure(figsize=(15, 10))
sns.barplot(x=count_genre.values, y=count_genre.index, palette="cubehelix")
plt.title("Most Rated Genres")
plt.xlabel("Number of Ratings")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()

######################################################### 

plt.figure(figsize=(15, 10))
sns.histplot(df["rating"], bins=10, kde=True, color="skyblue")
plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

#########################################################

df["year"] = df["title"].str.extract(r"\((\d{4})\)")
df["year"] = pd.to_numeric(df["year"], errors="coerce")
yearly_avg = df.groupby("year")["rating"].mean().dropna()

plt.figure(figsize=(15, 10))
sns.lineplot(x=yearly_avg.index, y=yearly_avg.values, color="green")
plt.title("Average Rating Over the Years")
plt.xlabel("Release Year")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()