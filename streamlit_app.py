import streamlit as st

st.title("GameCast Match Predictor")
st.write(
    "This project predicts match outcomes based on previous results"
)
home_team=st.selectbox("Home Team", ["Arsenal","Chelsea","Liverpool","Manchester United"], filter_mode=None)


st.write(f"Home team: {home_team}")
away_team=st.selectbox("Away Team", ["Arsenal", "Chelsea","Liverpool","Manchester United"], filter_mode=None)
st.write(f"Away team: {away_team}")