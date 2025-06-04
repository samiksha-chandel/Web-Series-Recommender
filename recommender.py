import pandas as pd
import re
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load and preprocess dataset
df = pd.read_csv('imdb_tvshows.csv', encoding='utf-8')

def extract_start_year(year_str):
    if isinstance(year_str, str):
        match = re.search(r'\d{4}', year_str)
        if match:
            return int(match.group())
    return None

df['Years'] = df['Years'].apply(extract_start_year)
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df = df.dropna(subset=['Rating', 'Title', 'Years']).reset_index(drop=True)
df['Years'] = df['Years'].astype(int)
df['Title'] = df['Title'].str.lower().str.strip()

# TF-IDF vectorizer & KNN fit
tfidf_title = TfidfVectorizer(stop_words='english')
tfidf_matrix_title = tfidf_title.fit_transform(df['Title'])
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(tfidf_matrix_title)

def recommend_by_title(title, k=5):
    title_clean = title.lower().strip()
    close = difflib.get_close_matches(title_clean, df['Title'].values, n=3)
    if title_clean not in df['Title'].values:
        return f"'{title}' not found. Did you mean: {', '.join(close)}?", None
    
    idx = df[df['Title'] == title_clean].index[0]
    distances, indices = knn.kneighbors(tfidf_matrix_title[idx], n_neighbors=15)

    similar_shows = []
    for i in range(1, len(indices[0])):
        rec = df.iloc[indices[0][i]]
        if rec['Title'].lower() == title_clean:
            continue
        similar_shows.append(rec)

    top_recs = sorted(similar_shows, key=lambda x: x['Rating'], reverse=True)[:k]

    results = []
    for rec in top_recs:
        results.append({
            'Title': rec['Title'].title(),
            'Genres': rec['Genres'],
            'Years': rec['Years'],
            'Rating': round(rec['Rating'], 2)
        })

    return None, results

def recommend_by_genre(genre, k=5):
    matches = df[df['Genres'].str.contains(genre, case=False, na=False)]
    if matches.empty:
        return f"No shows found in genre '{genre}'.", None

    top = matches.sort_values(by='Rating', ascending=False).head(k)

    results = []
    for _, row in top.iterrows():
        results.append({
            'Title': row['Title'].title(),
            'Genres': row['Genres'],
            'Years': row['Years'],
            'Rating': round(row['Rating'], 2)
        })

    return None, results

def recommend_by_year(start, end, k=5):
    matches = df[(df['Years'] >= start) & (df['Years'] <= end)]
    if matches.empty:
        return f"No shows found from {start} to {end}.", None

    top = matches.sort_values(by='Rating', ascending=False).head(k)

    results = []
    for _, row in top.iterrows():
        results.append({
            'Title': row['Title'].title(),
            'Genres': row['Genres'],
            'Years': row['Years'],
            'Rating': round(row['Rating'], 2)
        })

    return None, results
