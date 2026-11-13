import streamlit as st

st.title("GameCast Match Predictor")
st.write(
    "This project predicts match outcomes based on previous results"
)
home_team=st.selectbox("Home Team", ["Arsenal","Chelsea","Liverpool","Manchester United"])


st.write(f"Home team: {home_team}")