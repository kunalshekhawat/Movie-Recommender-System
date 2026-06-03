# 🎬 Movie Recommender System

A content-based movie recommendation system that suggests movies similar to a user's selected movie. The recommendation engine uses movie metadata such as genres, keywords, cast, crew, and overview to compute similarity between movies and generate personalized recommendations.

---

## 🚀 Features

* Recommend movies based on a selected movie
* Content-based filtering using movie metadata
* Fast similarity search using cosine similarity
* Interactive web interface built with Streamlit
* Displays movie posters using TMDB API
* Simple and user-friendly UI

---

## 📸 Demo

### Input

Select a movie from the dropdown menu.

### Output

The system recommends 5 similar movies along with their posters.

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-Learn**
* **NLTK**
* **Streamlit**
* **TMDB API**

---

## 📂 Project Structure

```bash
Movie-Recommender-System/
│
├── app.py                     # Streamlit application
├── movie_dict.pkl             # Processed movie dataset
├── similarity.pkl             # Cosine similarity matrix
├── notebooks/
│   └── Movie Recommender.ipynb
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

### 1. Data Collection

The project uses the TMDB movie dataset containing information such as:

* Movie title
* Genres
* Keywords
* Cast
* Crew
* Overview

### 2. Data Preprocessing

The following preprocessing steps are performed:

* Handle missing values
* Extract relevant features
* Merge multiple features into a single text representation
* Remove spaces from multi-word names
* Apply stemming to normalize words

### 3. Feature Engineering

A new **tags** column is created by combining:

* Genres
* Keywords
* Cast
* Crew
* Overview

This combined text is used to represent each movie.

### 4. Vectorization

The text data is converted into numerical vectors using:

```python
CountVectorizer(max_features=5000, stop_words='english')
```

### 5. Similarity Calculation

Cosine similarity is computed between movie vectors:

```python
cosine_similarity(movie_vectors)
```

Movies with the highest similarity scores are recommended to the user.

---

## ▶️ Installation & Setup

### Clone the repository

```bash
git clone https://github.com/kunalshekhawat/Movie-Recommender-System.git
cd Movie-Recommender-System
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

```bash
http://localhost:8501
```

---

## 📊 Recommendation Algorithm

This project uses **Content-Based Filtering**.

Instead of recommending movies based on user ratings, the system recommends movies that have similar content and characteristics to the selected movie.

### Example

If the user selects:

```text
Avatar
```

The system may recommend:

* Aliens
* Guardians of the Galaxy
* John Carter
* Star Trek
* The Fifth Element

because they share similar themes, genres, and keywords.

---

## 🔮 Future Improvements

* Collaborative filtering recommendations
* Hybrid recommendation system
* User authentication
* Personalized watchlists
* Improved recommendation quality using embeddings
* Deployment on cloud platforms

---

## 📚 Learning Outcomes

Through this project, I gained hands-on experience with:

* Data preprocessing
* Feature engineering
* Natural Language Processing (NLP)
* Vectorization techniques
* Cosine similarity
* Recommendation systems
* Streamlit deployment

---

## 👨‍💻 Author

**Kunal Singh Shekhawat**

GitHub: https://github.com/kunalshekhawat

---
