import pickle
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Fetch movie posters and details from TMDb API
def fetch_movie_details(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get('poster_path', None)
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else "https://via.placeholder.com/500"
        title = data.get('title', 'N/A')
        overview = data.get('overview', 'No overview available')
        release_date = data.get('release_date', 'Unknown release date')
        rating = data.get('vote_average', 'N/A')
        return full_path, title, overview, release_date, rating
    except:
        return "https://via.placeholder.com/500", 'N/A', 'No overview available', 'Unknown', 'N/A'

# Movie recommendation function
def recommend(movie, num_recommendations):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:num_recommendations+1]:  # Fetch number of movies based on user input
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(fetch_movie_details(movie_id))
    return recommended_movies

# Streamlit app settings
st.set_page_config(page_title="Movie Recommender", layout="wide")

# App Header
st.title("🎬 Movie Recommendation System")
st.subheader("Get recommendations based on your favorite movies!")

# Load movies data and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Sidebar settings
st.sidebar.header("Customize Your Recommendations")
movie_list = movies['title'].values
selected_movie = st.sidebar.selectbox("Choose a movie", movie_list)

num_recommendations = st.sidebar.slider("Number of recommendations", 1, 10, 5)

# Show recommendations button
if st.sidebar.button("Show Recommendations"):
    with st.spinner("Fetching recommendations..."):
        recommended_movies = recommend(selected_movie, num_recommendations)
        
    if recommended_movies:
        st.success(f"Top {num_recommendations} movie recommendations for '{selected_movie}':")
        
        # Display recommendations in a card-like layout
        for movie in recommended_movies:
            poster, title, overview, release_date, rating = movie
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(poster, use_column_width=True)
            with col2:
                st.subheader(f"{title} ({release_date})")
                st.markdown(f"**Rating**: {rating}/10")
                st.write(f"**Overview**: {overview}")
            st.markdown("---")  # Divider between movie cards
    else:
        st.error("Sorry, no recommendations found.")
else:
    st.info("Select a movie and press 'Show Recommendations' to start.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.write("Powered by TMDb API")
