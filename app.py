import streamlit as st
from recommender import (
    handle_recommendation_by_genre
)
import streamlit.components.v1 as components

# --- Page Configuration ---
st.set_page_config(page_title="Movie/TV Recommender", layout="wide")

# --- Content Type ---
content_type = st.sidebar.selectbox("Select Content Type", ["Movie", "Series"])

# --- Main Heading ---
st.markdown("<h1 style='text-align: center;'>Movie/TV Series Recommender 🍿</h1>", unsafe_allow_html=True)
st.markdown("---")

input = st.text_input("Enter a genre/title:")
if st.button("Get Recommendations"):
    with st.spinner("Fetching recommendations..."):
        result_html = handle_recommendation_by_genre(input, content_type, 12)
        components.html(result_html, height=2500)  # Set height to 0 for dynamic content
