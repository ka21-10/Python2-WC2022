import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header

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

def show_our_dataset():
    st.title(':blue[ABOUT OUR DATASET]')
    # Apply CSS to increase text size
    st.markdown(
        """
        <style>
        title {
                font-size: 50px !important}
        .body {
            font-size: 25px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    custom_colored_header(
        label="Why and what to explore?",
        color_name="blue",
        description="This part reveals the reason and purpose of our analysis.")

    left_column, mid_column, right_column = st.columns(3)

    with left_column: 
        st.markdown("""
                    <div style = "font-size: 25px;">
                    <strong>What is in it:</strong> The dataset contains all the matches from the FIFA World Cup Qatar 2022, updated daily. Along with the scores and football teams, various statistics were provided for each game, including assists, possessions, crosses, the number of red and yellow cards, passes, fouls, attempts, switches of play, offsides, and the number of times a particular area of the pitch has been crossed.")
        </div>
                    """,unsafe_allow_html=True)
    with mid_column:
        st.markdown("""
                    <div style = "font-size: 25px;">
                    <strong>Why we chose this dataset:</strong> The World Cup is not just a tournament but a cultural phenomenon that unites people regardless of borders and barriers, captivating billions of fans. With that same fire in our hearts, we aspire to learn more about the latest trends, performances, and outcomes of the championship. While looking for datasets for this project, we came across Fifa World Cup 2022: Complete Dataset, which provides a wide range of detailed information. In particular, it includes divergent elements concerning the performance and gameplay stats of teams in the 2022 World Cup. This diversity and attentiveness are great features to support our analysis.")
        </div>
                    """,unsafe_allow_html=True)
    with right_column:
        st.markdown("""
                    <div style = "font-size: 25px;">
                    <strong>What we explored from it:</strong> Football and data will be significantly intertwined in this report as two completely unrelated fields that seem never to be encountered. Behind the spectacle of the matches lies a treasure trove of invaluable data. By delving into World Cup football datasets, we seek to uncover the fascinating knowledge within the numbers to explore intriguing questions. How have dominant football countries kept their position? Are there discernible patterns in the gameplay? What tactics and strategies are preferred across nations? By examining these questions, we mean to uncover beneficial insights into the intricacies of the 2022 World Cup.")
        </div>
                    """,unsafe_allow_html=True)
    custom_colored_header(
        label="Description of variables",
        description="Here are the explanation for all variables in our dataset.",
        color_name="blue")

    # Writing the variable descriptions
    st.markdown("""
                <div style = "font-size: 25px;">
<strong>1. team1</strong>: The name of the first team participating in the match.<br>
<strong>2. team2</strong>: The name of the second team participating in the match.<br>
<strong>3. possession team1 in percent</strong>: The percentage of time during the match that team 1 had control of the ball.<br>
<strong>4. possession team2 in percent</strong>: The percentage of time during the match that team 2 had control of the ball.<br>
<strong>5. number of goals team1</strong>: The total number of goals scored by team 1 during the match.<br>
<strong>6. number of goals team2</strong>: The total number of goals scored by team 2 during the match.<br>
<strong>7. date</strong>: The date on which the match took place.<br>
<strong>8. total attempts team1</strong>: The total number of attempts (the total number of tries or shots taken by each team to score goals during the match) made by team 1 to score goals.<br>
<strong>9. total attempts team2</strong>: The total number of attempts made by team 2 to score goals.<br>
<strong>10. goal inside the penalty area team1</strong>: The number of goals scored by team 1 from within the penalty area (the 16.5-meter rectangle in front of the goal).<br>
<strong>11. goal inside the penalty area team2</strong>: The number of goals scored by team 2 from within the penalty area.<br>
<strong>12. goal outside the penalty area team1</strong>: The number of goals scored by team 1 from outside the penalty area.<br>
<strong>13. goal outside the penalty area team2</strong>: The number of goals scored by team 2 from outside the penalty area.<br>
<strong>14. assists team1</strong>: The number of times players from team 1 provided assists (passes leading to goals).<br>
<strong>15. assists team2</strong>: The number of times players from team 2 provided assists.<br>
<strong>16. on target attempts team1</strong>: The number of attempts by team 1 that were on target (aimed towards the goal).<br>
<strong>17. on target attempts team2</strong>: The number of attempts by team 2 that were on target.<br>
<strong>18. attempts inside the penalty area team1</strong>: The number of attempts by team 1 made from within the penalty area.<br>
<strong>19. attempts inside the penalty area team2</strong>: The number of attempts by team 2 made from within the penalty area.<br>
<strong>20. attempts outside the penalty area team1</strong>: The number of attempts by team 1 made from outside the penalty area.<br>
<strong>21. attempts outside the penalty area team2</strong>: The number of attempts by team 2 made from outside the penalty area.<br>
<strong>22. left channel team1</strong>: The number of attacking actions by team 1 in the left side of the field.<br>
<strong>23. left channel team2</strong>: The number of attacking actions by team 2 in the left side of the field.<br>
<strong>24. left inside channel team1</strong>: The number of attacking actions by team 1 in the left inside channel (closer to the center).<br>
<strong>25. left inside channel team2</strong>: The number of attacking actions by team 2 in the left inside channel.<br>
<strong>26. central channel team1</strong>: The number of attacking actions by team 1 in the central area of the field.<br>
<strong>27. central channel team2</strong>: The number of attacking actions by team 2 in the central area of the field.<br>
<strong>28. right inside channel team1</strong>: The number of attacking actions by team 1 in the right inside channel.<br>
<strong>29. right inside channel team2</strong>: The number of attacking actions by team 2 in the right inside channel.<br>
<strong>30. right channel team1</strong>: The number of attacking actions by team 1 in the right side of the field.<br>
<strong>31. right channel team2</strong>: The number of attacking actions by team 2 in the right side of the field.<br>
<strong>32. attempted defensive line breaks team1</strong>: The number of attempts by team 1 to break through the opponent's defensive line.<br>
<strong>33. attempted defensive line breaks team2</strong>: The number of attempts by team 2 to break through the opponent's defensive line.<br>
<strong>34. yellow cards team1</strong>: The number of yellow cards received by players from team 1.<br>
<strong>35. yellow cards team2</strong>: The number of yellow cards received by players from team 2.<br>
<strong>36. red cards team1</strong>: The number of red cards (sending off) received by players from team 1.<br>
<strong>37. red cards team2</strong>: The number of red cards received by players from team 2.<br>
<strong>38. fouls against team1</strong>: The number of fouls committed against team 1.<br>
<strong>39. fouls against team2</strong>: The number of fouls committed against team 2.<br>
<strong>40. offsides team1</strong>: The number of times players from team 1 were caught in an offside position (illegal position).<br>
<strong>41. offsides team2</strong>: The number of times players from team 2 were caught in an offside position.<br>
<strong>42. passes team1</strong>: The total number of passes made by players from team 1.<br>
<strong>43. passes team2</strong>: The total number of passes made by players from team 2.<br>
<strong>44. passes completed team1</strong>: The number of passes successfully completed by players from team 1.<br>
<strong>45. passes completed team2</strong>: The number of passes successfully completed by players from team 2.<br>
<strong>46. crosses team1</strong>: The number of crosses (passes from wide positions into the penalty area) attempted by team 1.<br>
<strong>47. crosses team2</strong>: The number of crosses attempted by team 2.<br>
<strong>48. crosses completed team1</strong>: The number of crosses successfully completed by team 1.<br>
<strong>49. crosses completed team2</strong>: The number of crosses successfully completed by team 2.<br>
<strong>50. switches of play completed team1</strong>: The number of successful switches of play (changing the direction of attack from one side of the field to the other) by team 1.<br>
<strong>51. switches of play completed team2</strong>: The number of successful switches of play by team 2.<br>
<strong>52. penalties scored team1</strong>: The number of penalties scored by team 1.<br>
<strong>53. penalties scored team2</strong>: The number of penalties scored by team 2.<br>
<strong>54. own goals team1</strong>: The number of own-goals scored by players from team 1.<br>
<strong>55. own goals team2</strong>: The number of own-goals scored by players from team 2.<br>
<strong>56. forced turnovers team1</strong>: The number of times team 1 forced the opponent to lose possession of the ball.<br>
<strong>57. forced turnovers team2</strong>: The number of times team 2 forced the opponent to lose possession of the ball.<br>
            </div>
                        """,unsafe_allow_html=True)
    custom_colored_header(
        label="Where we visualized data from?",
        color_name="blue",
        description="This table shows the dataset and the link below to the original dataset.")
    # Load and display the dataset
    file_path = 'wc1.csv'
    wc = pd.read_csv(file_path, encoding='latin-1')
    url= "https://www.kaggle.com/datasets/die9origephit/fifa-world-cup-2022-complete-dataset"  
    st.dataframe(wc,width=500, height= 500, use_container_width=True)
    # Create a link with larger text size
    st.markdown(f'<a href="{url}" style="font-size:25px;">Or click here to see the original dataset</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    show_our_dataset()
