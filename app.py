import streamlit as st
from recommender import recommend_by_title, recommend_by_genre, recommend_by_year

st.set_page_config(page_title="🎬 Web Series Recommender", layout="centered")
st.title("🎬 Web Series Recommender")
st.markdown("Find your next binge-worthy show based on what you already liked!")

# Sidebar mode selection
st.sidebar.title("Choose Recommendation Mode")
mode = st.sidebar.radio("Recommendation based on:", ["series", "genre", "year"])

# SERIES TITLE
if mode == "series":
    series_name = st.text_input("Enter a series name you liked:")
    if st.button("Recommend"):
        if not series_name:
            st.warning("Please enter a series name.")
        else:
            error, results = recommend_by_title(series_name)
            if error:
                st.error(error)
            else:
                st.success(f"Recommendations based on **{series_name.title()}**:")
                for i, rec in enumerate(results, 1):
                    st.markdown(f"**{i}. {rec['Title']}**")
                    st.write(f"Genres: {rec['Genres']}")
                    st.write(f"Year: {rec['Years']} | ⭐ Rating: {rec['Rating']}")
                    st.markdown("---")

# GENRE
elif mode == "genre":
    genre_input = st.text_input("Enter a genre (e.g., Drama, Comedy, Crime):")
    if st.button("Find Genre Shows"):
        if not genre_input:
            st.warning("Please enter a genre.")
        else:
            error, results = recommend_by_genre(genre_input)
            if error:
                st.error(error)
            else:
                st.success(f"Top shows in genre: **{genre_input.title()}**")
                for i, rec in enumerate(results, 1):
                    st.markdown(f"**{i}. {rec['Title']}**")
                    st.write(f"Genres: {rec['Genres']}")
                    st.write(f"Year: {rec['Years']} | ⭐ Rating: {rec['Rating']}")
                    st.markdown("---")

# YEAR RANGE
elif mode == "year":
    start_year = st.number_input("Start Year", min_value=1900, max_value=2100, step=1)
    end_year = st.number_input("End Year", min_value=1900, max_value=2100, step=1)
    if st.button("Search by Year"):
        if start_year > end_year:
            st.error("Start year must be less than or equal to end year.")
        else:
            error, results = recommend_by_year(start_year, end_year)
            if error:
                st.error(error)
            else:
                st.success(f"Top shows from **{int(start_year)} to {int(end_year)}**")
                for i, rec in enumerate(results, 1):
                    st.markdown(f"**{i}. {rec['Title']}**")
                    st.write(f"Genres: {rec['Genres']}")
                    st.write(f"Year: {rec['Years']} | ⭐ Rating: {rec['Rating']}")
                    st.markdown("---")