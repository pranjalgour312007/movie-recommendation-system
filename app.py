import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    api_key = st.secrets["TMDB_API_KEY"]
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id, api_key)
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    indices = similarity_indices[movie_index]
    movies_list = [int(i) for i in indices if int(i) != movie_index][:5]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i].movie_id
        recommended_movies.append(movies.iloc[i].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
movie_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movie_dict)
similarity_indices, similarity_scores = pickle.load(open('similarity_small.pkl', 'rb'))
st.title("Movie Recommender System")
option=st.selectbox("Select Movie",movies['title'].values)
if st.button('Recommend'):
    names,posters=recommend(option)
    import streamlit as st

    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
