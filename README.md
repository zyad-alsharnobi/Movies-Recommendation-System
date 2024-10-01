# Movie Recommendation System using Content-Based Filtering

This is a Movie Recommendation System built using Content-Based Filtering. The application takes advantage of the TMDB dataset to provide movie suggestions based on the input movie, giving users a personalized recommendation list. It is built using Python, Streamlit for the user interface, and scikit-learn for Natural Language Processing (NLP).


## Live Demo

Check out the live demo of our Movie Recommendation System:

[Movie Recommender Live Demo](https://movies-recommendation-system-tntbig25mrmsjvwqx2tnk2.streamlit.app/)

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Modeling](#modeling)
- [Streamlit App](#streamlit-app)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
This system recommends movies to users based on their preferences and past interactions using collaborative filtering and content-based techniques.

## Technologies Used
- **Python**: Core programming language
- **Pandas & NumPy**: Data manipulation
- **Scikit-learn**: For model training
- **Streamlit**: For app deployment
- **Jupyter Notebook**: Development environment

## Dataset
The dataset contains movie ratings, genres, and metadata, used for both collaborative filtering and content-based recommendations.

## Modeling
The model uses both collaborative filtering (user-item interaction) and content-based filtering (movie metadata) to generate recommendations.

## Streamlit App
The Streamlit app provides an interactive interface where users can input their preferences and get movie recommendations.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/zyad-alsharnobi/Movie-Recommendation-System.git
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the Streamlit app:
   ```bash
   streamlit run app.py

## License
This project is licensed under the MIT License.

