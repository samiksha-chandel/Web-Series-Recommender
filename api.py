import requests

headers = {
    "User -Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# OMDb API config
API_KEY = "eed0fed1"
OMDB_BASE_URL = "http://www.omdbapi.com/"

def search_omdb(name, max_results=5, content_type="Movie"):
    results = []
    for page in range(1, 6):
        params = {
            "apikey": API_KEY,
            "type": "series" if content_type == "Series" else "movie",
            "s": name,
            "page": page
        }
        print(f"Requesting: {params}")  # Debugging line
        try:
            response = requests.get(OMDB_BASE_URL, params=params)
            data = response.json()
            print(f"Response: {data}")  # Debugging line
            if data.get("Response") == "False":
                break

            for item in data.get("Search", []):
                # Check if the type matches the desired content type
                if item.get("Type") != content_type.lower():
                    continue

                imdb_id = item.get("imdbID")
                details_params = {
                    "apikey": API_KEY,
                    "i": imdb_id
                }
                details_resp = requests.get(OMDB_BASE_URL, params=details_params)
                movie = details_resp.json()

                # Check if the movie has a poster
                if movie.get("Poster") and movie["Poster"] != "N/A":
                    results.append(movie)

                if len(results) >= max_results:
                    break
        except Exception as e:
            print(f"Error: {e}")  # Debugging line
            continue
        if len(results) >= max_results:
            break

    results = [r for r in results if r.get("imdbRating") not in [None, "N/A"]]
    results = sorted(results, key=lambda x: float(x.get("imdbRating", 0) or 0), reverse=True)

    return results[:max_results]
