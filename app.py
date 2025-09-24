import streamlit as st
import pickle
import requests


def get_info(movie):
    movie_id = movies_list[movies_list['title'] == movie].movie_id.iloc[0]
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=7d9b56217734a636a1a0ff5c386bd840"
    response = requests.get(url)

    data = response.json()
    overview1 = data['overview']
    release_date1 = data['release_date']
    runtime1 = data['runtime']
    user_rating1 = data['vote_average']
    genres1 = []
    mid = data['genres']
    for i in mid:
        genres1.append(i['name'])
    return overview1,  release_date1, runtime1, user_rating1, genres1


def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=7d9b56217734a636a1a0ff5c386bd840"
        response = requests.get(url)

        data = response.json()

        poster_path = data['poster_path']
        alt_poster_path = data['backdrop_path']

        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            # Return a placeholder if no poster is available
            return "https://via.placeholder.com/500x750.png?text=No+Poster+Available"

    except Exception as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750.png?text=Error"


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list2 = sorted(list(enumerate(distances)), reverse=True, key=lambda x1: x1[1])[1: 6]
    recommended_movie = []
    recommended_movie_poster = []
    for i in movies_list2:

        movie_id = movies_list.iloc[i[0]].movie_id

        recommended_movie.append(movies_list.iloc[i[0]].title)

        recommended_movie_poster.append(fetch_poster(movie_id))

    return recommended_movie, recommended_movie_poster


similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list1 = movies_list['title'].values
st.title('Movies Recommender System')

selected_movie_name = st.selectbox(
    "Select the movie:",
    movies_list1,
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    tab1, tab2, tab3, tab4, tab5 = st.tabs([names[0], names[1], names[2], names[3], names[4]])

    with tab1:
        with st.container(horizontal=True):
            st.image(posters[0], width=200)
            with st.container():
                st.header(names[0])
                overview0, release_date0, runtime0, user_rating0, genres0 = get_info(names[0])
                st.write("Release Date:", release_date0)
                with st.container(horizontal=True):
                    st.write("Genre:")
                    for x in genres0:
                        st.write(x)
                st.write("Length:", runtime0, "minutes")
                st.write("User Rating:", user_rating0)
                st.write("Overview:", overview0)

    with tab2:
        with st.container(horizontal=True):
            st.image(posters[1], width=200)
            with st.container():
                st.header(names[1])
                overview00, release_date00, runtime00, user_rating00, genres00 = get_info(names[1])
                st.write("Release Date:", release_date00)
                with st.container(horizontal=True):
                    st.write("Genre:")
                    for x in genres00:
                        st.write(x)
                st.write("Length:", runtime00, "minutes")
                st.write("User Rating:", user_rating00)
                st.write("Overview:", overview00)

    with tab3:
        with st.container(horizontal=True):
            st.image(posters[2], width=200)
            with st.container():
                st.header(names[2])
                overview2, release_date2, runtime2, user_rating2, genres2 = get_info(names[2])
                st.write("Release Date:", release_date2)
                with st.container(horizontal=True):
                    st.write("Genre:")
                    for x in genres2:
                        st.write(x)
                st.write("Length:", runtime2, "minutes")
                st.write("User Rating:", user_rating2)
                st.write("Overview:", overview2)

    with tab4:
        with st.container(horizontal=True):
            st.image(posters[3], width=200)
            with st.container():
                st.header(names[3])
                overview3, release_date3, runtime3, user_rating3, genres3 = get_info(names[3])
                st.write("Release Date:", release_date3)
                with st.container(horizontal=True):
                    st.write("Genre:")
                    for x in genres3:
                        st.write(x)
                st.write("Length:", runtime3, "minutes")
                st.write("User Rating:", user_rating3)
                st.write("Overview:", overview3)

    with tab5:
        with st.container(horizontal=True):
            st.image(posters[4], width=200)
            with st.container():
                st.header(names[4])
                overview4, release_date4, runtime4, user_rating4, genres4 = get_info(names[4])
                st.write("Release Date:", release_date4)
                with st.container(horizontal=True):
                    st.write("Genre:")
                    for x in genres4:
                        st.write(x)
                st.write("Length:", runtime4, "minutes")
                st.write("User Rating:", user_rating4)
                st.write("Overview:", overview4)
