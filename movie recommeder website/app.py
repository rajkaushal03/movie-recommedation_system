import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=1594d8dae5584cdf335117ae5c130e62&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w780/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies.title == movie ].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommend_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id   
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api tmdb.org
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommend_movies_posters




similarity = pickle.load(open('similarity.pkl','rb'))
movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies =  pd.DataFrame(movie_dict)

st.title('Movie Recommender System')

selected_movie = st.selectbox(
'Write the Movie Name for recommendation',movies['title'].values
)

       
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        