import pickle
from API_response import Generate_Response


# Load movies and similarity data
movies_df = pickle.load(open("model/movie_list.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))
genres = pickle.load(open("model/movie_genre.pkl", "rb"))
cast = pickle.load(open("model/cast.pkl", "rb"))
keywords = pickle.load(open("model/keywords.pkl", "rb"))

def get_summary(text):
    """Get a summarized version of the text using Gemini API."""
    try:
        prompt = f"Summarize this movie overview in an engaging way (max 50 words): {text}"
        summary = Generate_Response(prompt)
        
        if summary:
            summary = summary.strip()
            # Basic validation of the summary
            if not summary or len(summary.split()) > 60:  # Allow slightly more words for flexibility
                return text
            return summary
        return text
        
    except Exception as e:
        print(f"Error in text summarization: {str(e)}")
        return text

def get_movie_details(movie_title):
    """Get detailed information about a specific movie."""
    try:
        movie = movies_df[movies_df['title'] == movie_title].iloc[0]
        movie_index = movie.name  # Get the index of the movie
        
        # Get genres for the movie
        movie_genres = genres.iloc[movie_index] if movie_index in genres.index else []
        
        # Convert to list if it's a string
        if isinstance(movie_genres, str):
            movie_genres = [genre.strip() for genre in movie_genres.split(',')]
        elif not isinstance(movie_genres, list):
            movie_genres = []

        # Get cast for the movie
        movie_cast = cast.iloc[movie_index] if movie_index in cast.index else []
        
        # Get overview and summarize it
        overview = movie.get('tags', '')
        if not overview:  # Fallback to overview if tags is empty
            overview = movie.get('overview', 'No description available.')
        
        summarized_overview = get_summary(overview)
        
        return {
            'title': movie['title'],
            'overview': summarized_overview,
            'original_overview': overview,  # Keep the original overview
            'genres': movie_genres[:3],  # Limit to top 3 genres
            'cast': movie_cast[:5] if isinstance(movie_cast, list) else []  # Limit to top 5 cast members
        }
    except (IndexError, KeyError) as e:
        print(f"Error getting movie details for {movie_title}: {str(e)}")
        return None

def recommend(movie):
    """Get movie recommendations based on similarity."""
    try:
        # Find the index of the movie
        movie_index = movies_df[movies_df['title'] == movie].index[0]
        
        # Get similarity scores for that movie
        similarity_scores = list(enumerate(similarity[movie_index]))
        
        # Sort movies based on similarity score
        sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:7]
        
        # Get movie details for each recommendation
        recommended_movies = []
        for i in sorted_scores:
            movie_title = movies_df.iloc[i[0]].title
            movie_details = get_movie_details(movie_title)
            if movie_details:
                recommended_movies.append(movie_details)
        
        return recommended_movies
    except Exception as e:
        print(f"Error in recommend function: {e}")
        return []

def get_movies_list():
    """Get list of all available movies."""
    return movies_df['title'].values.tolist()