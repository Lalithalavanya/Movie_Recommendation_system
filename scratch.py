import pickle
import streamlit as st
import requests
import pandas as pd
import bz2
import _pickle as cPickle
st.set_page_config(layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
# with open('main.js') as f:
#     st.markdown(f'<script>{f.reaśd()}</script>',unsafe_allow_html=True)
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=b0aa0a1b1d496d238c8917554ee42356&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def decompress_pickle(file):
    data = bz2.BZ2File(file, "rb")
    data = cPickle.load(data)
    return data
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[0:12]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters
data = decompress_pickle('similarity.pbz2')
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=data
st.title('Movie Recommender System')
selected_movie=st.selectbox('Name a Movie',movies['title'].values)

recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image(recommended_movie_posters[0])
    st.text(recommended_movie_names[0])
with col2:
    st.image(recommended_movie_posters[1])
    st.text(recommended_movie_names[1])
with col3:
    st.image(recommended_movie_posters[2])
    st.text(recommended_movie_names[2])
with col4:
    st.image(recommended_movie_posters[3])
    st.text(recommended_movie_names[3])
col5, col6, col7, col8 = st.columns(4)
with col5:
    st.image(recommended_movie_posters[4])
    st.text(recommended_movie_names[4])
with col6:
    st.image(recommended_movie_posters[5])
    st.text(recommended_movie_names[5])
with col7:
    st.image(recommended_movie_posters[6])
    st.text(recommended_movie_names[6])
with col8:
    st.image(recommended_movie_posters[7])
    st.text(recommended_movie_names[7])
col9, col10, col11, col12 = st.columns(4)
with col9:
    st.image(recommended_movie_posters[8])
    st.text(recommended_movie_names[8])
with col10:
    st.image(recommended_movie_posters[9])
    st.text(recommended_movie_names[9])
with col11:
    st.image(recommended_movie_posters[10])
    st.text(recommended_movie_names[10])
with col12:
    st.image(recommended_movie_posters[11])
    st.text(recommended_movie_names[11])
