from flask import Flask, render_template, request, flash
from utils import get_movie_details, recommend, get_movies_list

app = Flask(__name__)
app.secret_key = 'some_secret_key'  # Required for flashing messages

# Get list of all movies
movies_list = get_movies_list()

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    selected_movie_details = None
    if request.method == "POST":
        selected_movie = request.form.get("movie")
        if not selected_movie:
            flash("Please select a movie")
            return render_template("index.html", movies=movies_list)
            
        selected_movie_details = get_movie_details(selected_movie)
        if not selected_movie_details:
            flash("Movie not found")
            return render_template("index.html", movies=movies_list)
            
        recommendations = recommend(selected_movie)
        if not recommendations:
            flash("No recommendations found for this movie")
            
    return render_template(
        "index.html", 
        movies=movies_list, 
        selected_movie=selected_movie_details, 
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)
