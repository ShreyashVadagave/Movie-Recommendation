import streamlit as st
import pickle

# Load the model and data
movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation Function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Streamlit Web Interface
st.title("Movie Recommendation System")

selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for rec in recommendations:
        st.write(rec)
