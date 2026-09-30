import streamlit as st
import pickle
from pathlib import Path

# -----------------------------
# Load Data
# -----------------------------
PROJECT_DIR = Path(__file__).resolve().parent
with (PROJECT_DIR / "movie_list.pkl").open("rb") as movie_file:
    movies = pickle.load(movie_file)
with (PROJECT_DIR / "similarity.pkl").open("rb") as similarity_file:
    similarity = pickle.load(similarity_file)

if similarity.shape != (len(movies), len(movies)):
    raise ValueError(
        "similarity.pkl dimensions do not match movie_list.pkl; "
        "run generate_similarity.py to rebuild it."
    )

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(movie):
    matches = movies[movies["title"].str.casefold() == movie.strip().casefold()]
    if matches.empty:
        return None
    # Matrix rows follow dataframe row order; saved dataframe labels may have gaps.
    movie_index = movies.index.get_loc(matches.index[0])

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="CineMatch | Movie Discovery",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root { --ink: #f4f3f7; --muted: #a5a2b3; --accent: #ff5a5f; }
.stApp { background: radial-gradient(ellipse at 50% 0%, #29243d 0%, #15141d 42%, #101015 100%); color: var(--ink); }
.block-container { max-width: 1100px; padding-top: 3rem; padding-bottom: 4rem; }
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; letter-spacing: -0.04em; }
.hero { text-align: center; padding: 2.5rem 1rem 2rem; }
.eyebrow { display: inline-block; color: #ff8589; background: #ff5a5f1c; border: 1px solid #ff5a5f45; border-radius: 999px; padding: .38rem .8rem; font-size: .78rem; font-weight: 700; letter-spacing: .11em; text-transform: uppercase; }
.hero h1 { color: var(--ink); font-size: clamp(2.5rem, 6vw, 4.4rem); line-height: 1.05; margin: 1.1rem 0 .8rem; }
.hero p { max-width: 560px; margin: 0 auto; color: var(--muted); font-size: 1.08rem; line-height: 1.7; }
[data-testid="stForm"] { max-width: 760px; margin: 1.2rem auto 2.2rem; padding: 1.5rem 1.6rem .7rem; border: 1px solid #ffffff18; border-radius: 22px; background: #ffffff08; box-shadow: 0 22px 65px #00000030; }
.stTextInput label { color: #e8e6ef !important; font-weight: 600 !important; }
.stTextInput input { background: #17161f !important; color: #fff !important; border: 1px solid #ffffff24 !important; border-radius: 12px !important; min-height: 3.1rem; }
.stTextInput input:focus { border-color: #ff5a5f !important; box-shadow: 0 0 0 1px #ff5a5f !important; }
.stFormSubmitButton button { margin-top: 1.85rem; width: 100%; min-height: 3.1rem; border: 0; border-radius: 12px; background: linear-gradient(135deg, #ff696d, #ed3f56); color: white; font-weight: 700; transition: transform .15s ease, filter .15s ease; }
.stFormSubmitButton button:hover { filter: brightness(1.08); transform: translateY(-1px); color: white; }
.result-heading { margin: 2.6rem 0 1rem; }
.result-heading p { color: var(--muted); margin-top: -.5rem; }
.movie-card { height: 100%; min-height: 145px; padding: 1.15rem; border: 1px solid #ffffff16; border-radius: 18px; background: linear-gradient(150deg, #24222e, #191820); box-shadow: 0 12px 28px #00000020; }
.movie-number { color: #ff777b; font: 700 .78rem 'DM Sans', sans-serif; letter-spacing: .12em; }
.movie-title { color: #f6f4fa; font: 600 1.08rem 'Space Grotesk', sans-serif; line-height: 1.35; margin-top: 1.1rem; overflow-wrap: anywhere; }
[data-testid="stAlert"] { border-radius: 12px; }
@media (max-width: 700px) { .block-container { padding-top: 1.2rem; } .hero { padding-top: 1.4rem; } [data-testid="stForm"] { padding: 1.2rem 1rem .4rem; } .stFormSubmitButton button { margin-top: .2rem; } }
</style>
<div class="hero">
  <span class="eyebrow">Your next favorite film</span>
  <h1>Find your <span style="color:#ff696d">next watch.</span></h1>
  <p>Tell us a movie you love. We’ll find five picks with a similar feel, using story, genres, and cast.</p>
</div>
""", unsafe_allow_html=True)

with st.container():
    with st.form("movie_search"):
        search_col, button_col = st.columns([4, 1.25], vertical_alignment="bottom")
        with search_col:
            selected_movie = st.text_input("Movie title", placeholder="Try The Dark Knight…", label_visibility="visible")
        with button_col:
            submitted = st.form_submit_button("Find movies  →")

if submitted:
    if not selected_movie.strip():
        st.warning("Enter a movie title to get started.")
    else:
        recommendations = recommend(selected_movie)
        if recommendations is None:
            st.error("We couldn't find that title. Try the exact movie name, such as “Spider-Man 3”.")
        else:
            st.markdown('<div class="result-heading"><h2>Picked for you</h2><p>Five movies that share something with your pick.</p></div>', unsafe_allow_html=True)
            columns = st.columns(5, gap="medium")
            for index, (column, title) in enumerate(zip(columns, recommendations), start=1):
                with column:
                    st.markdown(f'<div class="movie-card"><div class="movie-number">PICK 0{index}</div><div class="movie-title">{title}</div></div>', unsafe_allow_html=True)

