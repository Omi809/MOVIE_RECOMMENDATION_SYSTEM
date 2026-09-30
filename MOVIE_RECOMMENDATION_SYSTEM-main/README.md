# 🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System built using **Python, Pandas, Scikit-learn, NLTK, and Streamlit**. The application recommends five similar movies for a selected movie using **Content-Based Filtering** and **Cosine Similarity**.

## 🚀 Features

- 🎥 Recommend 5 similar movies
- 🔍 Select movies from an interactive dropdown
- ⚡ Fast recommendations using Cosine Similarity
- 💻 Interactive Streamlit web interface
- 📊 NLP-based text feature processing
- 🧠 Precomputed similarity matrix for fast inference

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Pickle

## 🧠 Machine Learning Workflow

1. Prepare movie metadata and credits.
2. Select relevant movie features.
3. Handle missing values.
4. Extract genres, keywords, cast, and director information.
5. Combine relevant information into a `tags` feature.
6. Apply text preprocessing and stemming.
7. Convert movie tags into numerical vectors using `CountVectorizer`.
8. Calculate movie-to-movie similarity using Cosine Similarity.
9. Save the processed movie data and similarity matrix using Pickle.
10. Use the saved files in the Streamlit application.

## 📁 Project Structure

```text
MOVIE_RECOMMENDATION_SYSTEM/
│
├── app.py
├── generate_similarity.py
├── movie_list.pkl
├── similarity.pkl
├── movierecommender.ipynb
├── requirements.txt
└── README.md
```

### Generated Model Files

- `movie_list.pkl` — serialized movie dataframe used by the application.
- `similarity.pkl` — precomputed movie similarity matrix.
- `generate_similarity.py` — script used to generate and validate `similarity.pkl`.

> `similarity.pkl` is a large binary file and is intended to be stored using **Git LFS** when it exceeds GitHub's normal web-upload limit.

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Omi809/MOVIE_RECOMMENDATION_SYSTEM.git
```

Move into the project directory:

```bash
cd MOVIE_RECOMMENDATION_SYSTEM
```

Create and activate a virtual environment:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```powershell
python -m streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

## 🔧 Regenerate the Similarity Matrix

If `similarity.pkl` needs to be regenerated:

```powershell
.\.venv\Scripts\python.exe generate_similarity.py
```

The generated matrix is validated against the movie list before it is used by the application.

## ☁️ Deployment

This application can be deployed using **Streamlit Community Cloud**.

Deployment requirements:

- GitHub repository
- `app.py`
- `movie_list.pkl`
- `similarity.pkl`
- `requirements.txt`

After deployment, the application can be accessed through its public Streamlit URL without keeping the development laptop running.

## 📸 Application Usage

1. Open the Streamlit application.
2. Select a movie from the dropdown.
3. Click **Recommend**.
4. The application displays five similar movie recommendations.

## 📚 Libraries Used

```text
pandas
numpy
streamlit
scikit-learn
nltk
pickle
```

## 🎯 Future Improvements

- Add movie posters
- Display movie overview
- Show IMDb/TMDB ratings
- Filter recommendations by genre
- Add search suggestions
- Improve the UI with custom CSS
- Deploy and maintain the application on Streamlit Community Cloud

## 👨‍💻 Author

**Omii / Omi809**

Engineering Student | Python | Machine Learning | Web Development

## ⭐ Project

If you find this project useful, consider starring the repository and contributing improvements.
