"""Generate the movie similarity matrix used by app.py.

The notebook fits CountVectorizer(max_features=5000, stop_words="english")
and then calls cosine_similarity(vectors). It creates vectors before stemming
the tags, while movie_list.pkl contains the later, stemmed tags. The source
CSV files needed to recreate the notebook's pre-stemming vectors are not in
this project directory, so this script applies the notebook's exact
vectorizer/cosine steps to the serialized tags, in movie_list.pkl row order.
"""

import pickle
from pathlib import Path

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


PROJECT_DIR = Path(__file__).resolve().parent
MOVIES_PATH = PROJECT_DIR / "movie_list.pkl"
SIMILARITY_PATH = PROJECT_DIR / "similarity.pkl"


def main():
    with MOVIES_PATH.open("rb") as movie_file:
        movies = pickle.load(movie_file)

    if not {"title", "tags"}.issubset(movies.columns):
        raise ValueError("movie_list.pkl must contain 'title' and 'tags' columns")

    # Tags are already assembled, lowercased, and stemmed in movie_list.pkl.
    tags = movies["tags"].fillna("").astype(str)
    vectorizer = CountVectorizer(max_features=5000, stop_words="english")
    vectors = vectorizer.fit_transform(tags).toarray()
    similarity = cosine_similarity(vectors)

    expected_shape = (len(movies), len(movies))
    if similarity.shape != expected_shape:
        raise ValueError(
            f"Generated matrix has shape {similarity.shape}; expected {expected_shape}"
        )

    with SIMILARITY_PATH.open("wb") as similarity_file:
        pickle.dump(similarity, similarity_file, protocol=pickle.HIGHEST_PROTOCOL)

    size_bytes = SIMILARITY_PATH.stat().st_size
    print(f"Saved: {SIMILARITY_PATH}")
    print(f"Movies: {len(movies)}")
    print(f"Vocabulary features: {vectors.shape[1]}")
    print(f"Similarity matrix shape: {similarity.shape}")
    print(f"File size: {size_bytes:,} bytes ({size_bytes / (1024 ** 2):.2f} MiB)")


if __name__ == "__main__":
    main()
