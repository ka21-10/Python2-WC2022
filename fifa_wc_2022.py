from streamlit_extras.colored_header import colored_header
from annotated_text import annotated_text
import streamlit as st
from PIL import Image
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain
import matplotlib.pyplot as plt
import plotly.express as px

# Modified colored_header function
def custom_colored_header(label,description=None, color_name="blue"):
    st.markdown(
        f"""
        <div style="padding:5px;">
            <h2 style="color: blue; font-size: 30px; margin-bottom: 0;">{label}</h2>
            <hr style="border: 2px solid blue; margin-top: 5px; margin-bottom: 10px;">
            {'<p style="color: black; font-size: 20px; margin-top: 5px;">' + description + '</p>' if description else ''}
        </div>
        """,
        unsafe_allow_html=True
    )

def show_fifa_wc_2022():
    st.title(':blue[ABOUT FIFA WC 2022]')
    
    # Apply CSS to increase text size
    st.markdown(
        """
        <style>
        body {
            font-size: 50px;
        }
        .large-text {
            font-size: 25px;
        }
        .glossary-text {
            font-size: 25px;
        }
        .glossary-text ul {
            padding-left: 30px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    custom_colored_header(
        label="Overview of the Competition",
        color_name="lightblue",
        description="This overview contains some information about the overall competition and the World Cup 2022 in particular.",
    )   
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(
            '<p class="large-text">'
            "Dazzling spotlights, uprising roars echoing across the field, and hearts beating the same pulse - such is the glamour that every football enthusiast would die for. "
            '<span style="background-color: #8CC0DE;">Every four years ⏳</span> '
            "the world comes alive with an unparalleled love for football as fans from all over the globe gather to witness the "
            '<span style="background-color: #8CC0DE;">World Cup 🏆</span>. '
            "It is beyond dispute that to stand in that glorious position on the field. Every competition, "
            '<span style="background-color: #8CC0DE;">32 qualified football teams 🏃‍♂️🏃</span> '
            "need to take more measures than just what talent is capable of to reach the victory throne."    
            '</p>',
            unsafe_allow_html=True
        )
        wcbracket_url = "https://images2.thanhnien.vn/528068263637045248/2023/10/4/wolrd-cup-16964579592101478635490.jpeg"
        st.image(wcbracket_url, use_column_width=True)

    with right_column:
        st.markdown(
            '<p class="large-text">'
            "FIFA World Cup 2022 was held by the "
            '<span style="background-color: #8CC0DE;">host Qatar 🌟</span> '
            "from November 20th to December 18th, 2022. That was the first Middle East representative to host and also the first Asian country for the last 20 years. It was also unique for its first time ever taking place in the Winter due to harsh climate condition in Qatar. That year, FIFA World Cup was won by the "
            '<span style="background-color: #8CC0DE;">champions Argentina 🥇</span> '
            "after they dramatically beat France at the penalty shootout in the final. The championship also breaks the 'World Cup curse spell' for "
            '<span style="background-color: #8CC0DE;">Lionel Messi. LM🔟</span>'
            '</p>',
            unsafe_allow_html=True
        )
        argchamp_url = "https://leadership.ng/wp-content/uploads/2023/01/argentina-world-cup-win-jpg.webp"
        st.image(argchamp_url, use_column_width=True)
    
    custom_colored_header(
        label="Glossary for Football terms",
        description="This glossary contains all professional football terms ordered alphabetically",
        color_name="blue",
    )
       # Writing the glossary with larger text
    st.markdown("""
<style>
.large-text {
    font-size: 25px;  /* Increase this value to make the text larger */
}
.large-text strong {
    margin-bottom: 5px;  /* Add some space between terms */
}
</style>
<div class="large-text">
<strong>1. Assisted goals</strong>: The goals scored right after another player passes the ball.<br>
<strong>2. Attacking channels</strong>: Different zones on the football field from which teams launch their attacking plays, consisting of the left, left inside, centre, right inside and right channels.<br>
<strong>3. Cards</strong>: The disciplinary actions, which include red cards and yellow cards, are given by referees to players for serious or super serious fouls or misconduct or dangerous play.<br>
<strong>4. Conversion rate</strong>: The percentage of goals scored out of all shot attempts recorded by a team.<br>
<strong>5. Counter-attacking</strong>: How a football team quickly transitions from defense to offense, exploiting spaces left by the opponent players.<br>
<strong>6. Crossing accuracy</strong>: The percentage of successful crosses (long-range passes towards the opponent's field) out of the total crosses completed by a team's players during a match.<br>
<strong>7. FIFA</strong>: An abbreviation for Fédération Internationale de Football Association, an international self-regulatory organization governing association football.<br>
<strong>8. Finals</strong>: The ultimate matches of a tournament, usually from the quarter-finals to the semi-finals, and lastly, the final.<br>
<strong>9. Forced turnovers</strong>: The number of times a team is forced to lose possession of the ball through the opponents' interceptions, tackles, or other defensive actions.<br>
<strong>10. Fouls</strong>: The number of times a team's players conduct actions that break the law of football on opposing team players.<br>
<strong>11. Gameplay</strong>: The styles in which matches are played, including tactics and performances from individuals and teams.<br>
<strong>12. Goal difference</strong>: The numerical difference between the number of goals scored and the number of goals conceded by a team.<br>
<strong>13. Goals</strong>: The number of times the ball is over the goal line.<br>
<strong>14. Group stage</strong>: The initial phase of the World Cup, where 32 teams are divided into 8 groups and play against one another match by match.<br>
<strong>15. Individual goals</strong>: Goals scored by a player without assistance from another teammate, nor from the penalty spot, nor accidentally by an opponent player.<br>
<strong>16. Knockout stage</strong>: The stage in the World Cup where teams compete for only 1 slot for 2 teams in the match into the next round.<br>
<strong>17. Long passes</strong>: Passing the ball over a long distance.<br>
<strong>18. Matches played</strong>: The number of games in which a team participated during a football tournament.<br>
<strong>19. Opponents' own goals</strong>: The goals scored by the opposing team players into their own net.<br>
<strong>20. Passing accuracy</strong>: The percentage of successful passes out of the total passes completed by a team's players during a match.<br>
<strong>21. Penalty area</strong>: The 16.5-meter rectangular area in front of the goal.<br>
<strong>22. Penalty goals</strong>: The goals scored from the penalty kick, which was awarded to a team for the opponents committing a foul inside the penalty area.<br>
<strong>23. Possession</strong>: The percentage of how much a team controls the ball during a football match.<br>
<strong>24. Pressing</strong>: A tactic in football where a team applies high pressure to the opponent when they possess the ball to win back possession.<br>
<strong>25. Round of 16</strong>: The first knockout stage in the World Cup, where 16 teams remained after progressing from the group stage.<br>
<strong>26. Scoring locations</strong>: The areas on a football field where goals are scored, either inside or outside the penalty area.<br>
<strong>27. Semi-final</strong>: The penultimate stage of the World Cup, where the remaining 4 top teams compete in pairs for 2 slots into the Final.<br>
<strong>28. Short passes</strong>: Passing the ball over a short distance.<br>
<strong>29. Shot attempts</strong>: The number of times a team attempts to score by shooting, heading, and so on.<br>
<strong>30. Successful shot attempts</strong>: The number of shots taken by a team that result in a goal or a save by the opposition goalkeeper.<br>
<strong>31. Switches of play</strong>: The number of times a team changes the direction of their attack from one side of the field to the other, often through crosses or ball progression.<br>
<strong>32. Tactical mechanisms</strong>: The specific techniques of teams to achieve success in matches based on analysis of opponents' strengths and weaknesses.<br>
<strong>33. Tactical versatility</strong>: The team's ability to adapt and vary its tactics based on the opponents' weaknesses and real-time situation of a game.<br>
<strong>34. Tactics</strong>: The strategies of teams playing football during matches based on their strengths, weaknesses, objectives, and opponents.<br>
<strong>35. Technical ability</strong>: The proficiency in skills like passing, dribbling, and shooting of football players.<br>
<strong>36. Top-ranking nations</strong>: The national football clubs that were ranked high in the FIFA World Rankings 2022 during the World Cup.<br>
<strong>37. World Cup</strong>: The premier international football tournament organized by FIFA that is held every four years.<br>
<strong>38. World football ranking</strong>: The ranking system used to assess the performance of national football teams worldwide by points when they win or lose an official game considered by FIFA.<br>
</div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    show_fifa_wc_2022()