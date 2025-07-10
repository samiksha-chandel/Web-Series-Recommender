# 🎬 Movie & TV Series Recommender

An interactive web app built with **Streamlit** that recommends Movies or TV Series based on a user’s input — either genre or title. It uses the **OMDb API** to fetch real-time data like poster, plot, genre, rating, release year, and more.

---

## 🌟 Features

- 📺 Search by genre or show title
- 🍿 Get up to 12 top-rated recommendations
- 🌐 Real-time data via OMDb API (IMDb-based)
- 🖼️ Shows posters, rating, genre, year & description
- 🎨 Stylish Netflix-style UI using pure HTML/CSS inside Streamlit

---

## 🛠 Tech Stack

| Tool       | Use |
|------------|-----|
| **Streamlit** | For building the web app UI |
| **Requests**  | For calling the OMDb API |
| **OMDb API**  | To fetch movie & series metadata (poster, rating, genre, etc.) |

---

## 🔧 Setup Instructions

### 1. **Install dependencies**
Make sure you have Python 3.9+ installed.

```bash
pip install -r requirements.txt
```
### 2. **Run the app**

```bash
streamlit run app.py
```

This will open the app in your browser at http://localhost:8501

---

### **🔐 API Key Setup**
This app uses the free OMDb API

- Go to: https://www.omdbapi.com/apikey.aspx
- Sign up and get your free API key
- Replace the placeholder key in api.py:

```bash
API_KEY = "your_omdb_api_key_here"
```

---

# 📁 File Structure

```bash
omdb-recommender/
├── app.py             # Streamlit app entrypoint
├── api.py             # OMDb API request logic
├── recommender.py     # Recommendation formatting & logic
├── requirements.txt   # Required Python libraries
└── README.md          # You’re reading it :)
```

---

# 🚀 Deployment
You can deploy this app to Streamlit Cloud for free:

- Push code to GitHub
- Go to https://streamlit.io/cloud
- Connect your repo
- Set app.py as the main file
- BOOM. You’re live 🚀

---

# 🧠 How It Works
When a user enters a title or genre, it:

- Hits the OMDb API’s search endpoint
- Loops through multiple pages (up to 5)
- For each valid IMDb ID, it fetches full details
- Filters results based on type (movie or series) and rating
- Sorts by IMDb rating and shows the top n matches

Each card shows:
- Poster image
- Title + year
- IMDb rating
- Genre
- Plot (trimmed)
- Link to IMDb page

---
