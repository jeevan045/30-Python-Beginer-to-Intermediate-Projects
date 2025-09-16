import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

df = pd.read_csv("IMDB-Movie-Data.csv")
print("Dataset Loaded!")
print(df.head())
print(df.info())

df = df.dropna(subset=['Rating', 'Genre'])
df['Rating'] = df['Rating'].astype(float)
df['Genre'] = df['Genre'].str.split(',')

print("\nTop 10 Movies by Rating:")
print(df.sort_values(by='Rating', ascending=False).head(10))

all_genres = [g.strip() for sublist in df['Genre'] for g in sublist]
genre_count = Counter(all_genres)
print("\nTop 10 Genres:")
print(genre_count.most_common(10))

director_avg = df.groupby('Director').agg({'Rating': ['mean', 'count']})
director_avg.columns = ['AverageRating', 'MovieCount']
director_avg = director_avg[director_avg['MovieCount'] >= 5]
top_directors = director_avg.sort_values(by='AverageRating', ascending=False).head(5)
print("\nTop 5 Directors by Average Rating (min 5 movies):")
print(top_directors)

if 'Votes' in df.columns:
    df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')
    print("\nCorrelation between Votes and Rating:", df['Votes'].corr(df['Rating']))

plt.figure(figsize=(8,5))
sns.histplot(df['Rating'], bins=10, kde=True, color='skyblue')
plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

top_genres = genre_count.most_common(10)
plt.figure(figsize=(10,5))
sns.barplot(x=[g[0] for g in top_genres], y=[g[1] for g in top_genres], palette='viridis')
plt.title("Top 10 Movie Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

if 'Votes' in df.columns:
    plt.figure(figsize=(8,5))
    sns.scatterplot(x='Votes', y='Rating', data=df, alpha=0.6)
    plt.title("Votes vs Rating")
    plt.xlabel("Votes")
    plt.ylabel("Rating")
    plt.show()

if 'Year' in df.columns:
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    year_avg = df.groupby('Year')['Rating'].mean().dropna()
    plt.figure(figsize=(10,5))
    sns.lineplot(x=year_avg.index, y=year_avg.values)
    plt.title("Average Movie Rating Over Years")
    plt.xlabel("Year")
    plt.ylabel("Average Rating")
    plt.show()

def recommend_movies(genre_name, top_n=5):
    genre_name = genre_name.strip()
    filtered = df[df['Genre'].apply(lambda x: genre_name in x)]
    recommendations = filtered.sort_values(by='Rating', ascending=False).head(top_n)
    return recommendations[['Title', 'Rating', 'Director']]

print("\nSample Recommendations for Genre 'Action':")
print(recommend_movies('Action'))
