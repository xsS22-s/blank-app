import streamlit as st

st.title("GameCast Match Predictor")
st.write(
    "This project predicts match outcomes based on previous results"
)
home_team=st.selectbox("Home Team", ["Arsenal","Chelsea","Liverpool","Manchester United"], filter_mode=None)


away_team=st.selectbox("Away Team", ["Arsenal", "Chelsea","Liverpool","Manchester United"], filter_mode=None)


if home_team == away_team:
    st.warning("Please pick two different teams!")
else:
    st.success(f"Valid Matchup: {home_team} vs {away_team}")
if home_team != away_team and st.button("Predict Match", disabled= home_team==away_team):
    st.write("Prediction Successful!")