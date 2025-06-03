# 🎬 Movie Recommendation System

A content-based movie recommendation system built with Python and Flask, designed to suggest movies similar to a selected title. It leverages machine learning techniques to analyze movie features and recommend related content.


## 🚀 Features

- ✅ Content-Based Filtering using movie metadata
- ✅ Web UI built with Flask (lightweight and responsive)
- ✅ Real-time recommendations
- ✅ Searchable movie titles
- ✅ Scalable for future integration (e.g., collaborative filtering, deep learning)


## 🧠 How It Works

1. **Data Source**: The system uses a dataset (e.g., from Kaggle or TMDb) containing movie metadata like title, genres, overview, cast, and crew.
2. **Feature Extraction**: It combines important features (like keywords, genres, director) into a single string.
3. **Vectorization**: Uses `CountVectorizer` or `TF-IDF` to convert text to numerical vectors.
4. **Similarity Measurement**: Applies **cosine similarity** to find movies with similar features.
5. **Flask Web App**: Provides a clean web interface to input a movie and get recommendations.


## 🗂️ Project Structure


## 📦 Installation & Setup

1. **Clone this repo**
```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
cd Movie-Recommendation-System
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
python app.py
```

Or use Flask CLI:

```bash
flask --app app.py run
```

4. **Open in browser**

```
http://127.0.0.1:5000/
```


## 💡 Example Usage

* Visit the homepage
* Type "Inception" into the search bar
* Click **Recommend**
* Get 5–10 similar movie titles instantly



## 🛠️ Tech Stack

* **Backend**: Flask, Python
* **ML Libraries**: scikit-learn, pandas, numpy
* **Frontend**: HTML5, CSS3 (Bootstrap optional)
* **NLP**: CountVectorizer / TfidfVectorizer, Cosine Similarity


## 📈 Future Improvements

* 🎯 Add **collaborative filtering**
* 🧠 Integrate with **deep learning models** (e.g., BERT for movie descriptions)
* 🌐 Deploy on **Heroku or Render**
* 💬 Add **user authentication** & rating system


## 📚 Dataset Info

You can use datasets like:

* [TMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* [IMDb Dataset](https://www.imdb.com/interfaces/)


