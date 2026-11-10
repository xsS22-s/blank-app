import streamlit as st

st.title("GameCast Match Predictor")
st.write(
    "This project predicts match outcomes based on previous results"
)
st.selectbox("Home Team", ["Arsenal","Chelsea","Liverpool","Manchester United"])
home_team = st.selectbox(result)

st.write(f"Home team: {home_team}")