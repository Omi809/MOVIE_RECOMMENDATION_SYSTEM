# 🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**. The application recommends five similar movies based on the selected movie using **Content-Based Filtering** and **Cosine Similarity**.

---

## 🚀 Features

- 🎥 Recommend 5 similar movies
- 🔍 Search movies from a dropdown
- ⚡ Fast recommendations using Cosine Similarity
- 💻 Simple and interactive Streamlit interface
- 📊 Built using NLP techniques

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Pickle

---

## 📂 Dataset

This project uses the **TMDB 5000 Movies Dataset**.

Files used:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

---

## 🧠 Machine Learning Workflow

1. Load movie and credits datasets
2. Merge datasets
3. Select important features
4. Handle missing values
5. Convert JSON-like columns using `ast.literal_eval()`
6. Extract:
   - Genres
   - Keywords
   - Cast (Top 3)
   - Director
7. Combine features into a single **tags** column
8. Apply text preprocessing and stemming
9. Convert text into vectors using **CountVectorizer**
10. Calculate similarity using **Cosine Similarity**
11. Save processed data using Pickle
12. Build an interactive Streamlit application

---

## 📁 Project Structure

```
Movie-Recommendation-System/
│
├── app.py
├── movie_list.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
└── README.md
```

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
```

Move into the project directory

```bash
cd movie-recommendation-system
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Application Preview

- Select a movie from the dropdown.
- Click the **Recommend** button.
- Get five similar movie recommendations instantly.

---

## 📚 Libraries Used

```python
pandas
numpy
streamlit
scikit-learn
nltk
pickle
ast
```

---

## 🎯 Future Improvements

- Add movie posters
- Display movie overview
- Show IMDb/TMDB ratings
- Filter recommendations by genre
- Deploy on Streamlit Community Cloud
- Add search suggestions
- Improve UI with custom CSS

---

## 👨‍💻 Author

**Swapnil**

Engineering Student | Python | Machine Learning | Web Development

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub and feel free to contribute or share your suggestions.
