import streamlit as st
import pickle

# Load the movies list and similarity matrix
movies_df = pickle.load(open("model/movie_list.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))

# Extract movie titles for the dropdown 
movies_list = movies_df['title'].values

def recommend(movie):
    # Find the index of the selected movie
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    
    # Get similarity scores for that movie and sort them
    distances = sorted(list(enumerate(similarity[movie_index])), key=lambda x: x[1], reverse=True)
    
    recommended_movies = []
    for i in distances[1:6]:  # Only take top 5 recommendations after the selected movie
        try:
            recommended_movies.append(movies_df.iloc[i[0]].title)
        except IndexError:  # Handle missing data
            continue
    
    return recommended_movies

# Streamlit app layout
st.title("Movie Recommendation System")

# Dropdown for movie selection
selected_movie_name = st.selectbox("Choose a movie from the list below", movies_list)
st.write("You have selected:", selected_movie_name)

# Recommend button and display
if st.button("Recommend"):
    recommended_movies = recommend(selected_movie_name)
    st.write(f"If you like {selected_movie_name}, you might also enjoy:")
    
    # Display recommendations
    for movie in recommended_movies:
        st.write("- " + movie)
