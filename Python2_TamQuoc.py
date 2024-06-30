import streamlit as st
import pandas as pd
import plotly.express as px
import re
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import os

tamquoc = (os.path.join('images', "TAm quoc.jpg"))
vgu = (os.path.join('images', "VGU python.png"))

st.set_page_config(page_title="FIFA WC 2022 ANALYSIS",page_icon="⚽",layout="wide")

page_bg_img = """
        <style>
        [data-testid="stAppViewContainer"] > .main {
            background-image: url("https://img.freepik.com/premium-vector/banner-background-theme-world-championship-qatar-2022_561465-247.jpg?w=826");
            background-size: 103%;
            background-position: left;
            background-repeat: no-repeat;
            background-attachment: local;
                }
                </style>
                """
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load FIFA World Cup 2022 data
wc = pd.read_csv('wc1.csv') 

# Define the function Goal types
def Goal_type(Country_name):
    Country1 = wc[wc['team1'] == Country_name]
    Goal_type1 = Country1[['date', 'team1', 'assists team1', 
                'number of goals team1', 'own goals team2', 
                'penalties scored team1']]
    Goal_type1 = Goal_type1.rename(columns={'team1': 'Team', 
                'assists team1': 'Assisted goals', 
                'number of goals team1': 'Total goals'})
    Goal_type1['Individual goals'] = Goal_type1['Total goals'] - Goal_type1['Assisted goals'] - Goal_type1['own goals team2'] - Goal_type1['penalties scored team1']
    Goal_type1['Opponents own goals'] = Goal_type1['own goals team2']
    Goal_type1['Penalty goals'] = Goal_type1['penalties scored team1']
   
    Country2 = wc[wc['team2'] == Country_name]
    Goal_type2 = Country2[['date', 'team2', 'assists team2', 
              'number of goals team2', 'own goals team1', 
              'penalties scored team2']]
    Goal_type2 = Goal_type2.rename(columns={'team2': 'Team', 
              'assists team2': 'Assisted goals', 
              'number of goals team2': 'Total goals'})
    Goal_type2['Individual goals'] = Goal_type2['Total goals'] - Goal_type2['Assisted goals'] - Goal_type2['own goals team1'] - Goal_type2['penalties scored team2']
    Goal_type2['Opponents own goals'] = Goal_type2['own goals team1']
    Goal_type2['Penalty goals'] = Goal_type2['penalties scored team2']
 
    Goal_type12 = pd.concat([Goal_type1, Goal_type2], ignore_index=True)
   
    Goal_type = Goal_type12.groupby('Team').agg({
        'Assisted goals': 'sum',
        'Total goals': 'sum',
        'Individual goals': 'sum',
        'Opponents own goals': 'sum',
        'Penalty goals': 'sum'
    }).reset_index()
   
    Goal_type['Assisted goals percent'] = round(Goal_type['Assisted goals'] * 100 / Goal_type['Total goals'], 1)
    Goal_type['Individual goals percent'] = round(Goal_type['Individual goals'] * 100 / Goal_type['Total goals'], 1)
    Goal_type['Opponents own goals percent'] = round(Goal_type['Opponents own goals'] * 100 / Goal_type['Total goals'], 1)
    Goal_type['Penalty goals percent'] = round(Goal_type['Penalty goals'] * 100 / Goal_type['Total goals'], 1)
   
    return Goal_type[['Team', 'Assisted goals percent', 
             'Individual goals percent', 'Opponents own goals percent', 
             'Penalty goals percent']]

# Define the Fair_play function
def Fair_play(country_name, wc):
    # Filter matches where country_name is team1 or team2
    Country1 = wc[wc['team1'] == country_name]
    Fair1 = Country1[['date', 'team1', 'red cards team1', 
          'yellow cards team1', 'fouls against team1']].copy()
    Fair1.columns = ['date', 'Team', 'Red cards', 'Yellow cards', 'Fouls']
   
    Country2 = wc[wc['team2'] == country_name]
    Fair2 = Country2[['date', 'team2', 'red cards team2', 
          'yellow cards team2', 'fouls against team2']].copy()
    Fair2.columns = ['date', 'Team', 'Red cards', 'Yellow cards', 'Fouls']
   
    # Combine the data for both scenarios
    Fair_play = pd.concat([Fair1, Fair2])
 
    # Calculate mean values for each type of infraction and goals
    Fair_play_summary = Fair_play.groupby('Team').mean(numeric_only=True).round(2).reset_index()
    Fair_play_summary.columns = ['Team', 'Red cards per match', 
                        'Yellow cards per match', 'Fouls per match']


    return Fair_play_summary

# Define the Possession function
def Possession(country_name, wc):
    Country1 = wc[wc['team1'] == country_name]
    Possession1 = Country1[['date', 'team1', 
           'possession team1 in percent']].rename(columns={
           'possession team1 in percent': 'Possession percent',
           'team1': 'Team'})
   
    Country2 = wc[wc['team2'] == country_name]
    Possession2 = Country2[['date', 'team2', 
                 'possession team2 in percent']].rename(columns={
                 'possession team2 in percent': 'Possession percent',
                 'team2': 'Team'})
    Possession = pd.concat([Possession1, Possession2])
    return Possession

# Define the pressing function
def pressing(country_name, wc):
    country1 = wc[wc['team1'] == country_name]
    pressing1 = country1[['date', 'team1']].copy()
    pressing1['Switches of play'] = country1[
              'switches of play completed team1'].mean()
    pressing1['Forced turnovers'] = country1[
              'forced turnovers team2'].mean()
    pressing1.rename(columns={'team1': 'Team'}, inplace=True)


    country2 = wc[wc['team2'] == country_name]
    pressing2 = country2[['date', 'team2']].copy()
    pressing2['Switches of play'] = country2[
              'switches of play completed team2'].mean()
    pressing2['Forced turnovers'] = country2[
              'forced turnovers team1'].mean()
    pressing2.rename(columns={'team2': 'Team'}, inplace=True)


    pressing_all = pd.concat([pressing1, pressing2], axis=0)
    pressing_summary = pressing_all.groupby('Team').agg({
        'Switches of play': 'mean',
        'Forced turnovers': 'mean'
    }).reset_index()
    pressing_summary['Switches of play'] = pressing_summary[
                     'Switches of play'].round(2)
    pressing_summary['Forced turnovers'] = pressing_summary[
                     'Forced turnovers'].round(2)
   
    return pressing_summary

# Create a list of country names
Country_names = ["ARGENTINA", "FRANCE", "CROATIA", "MOROCCO", "NETHERLANDS", "UNITED STATES", 
                 "AUSTRALIA", "POLAND", "ENGLAND", "SENEGAL", "JAPAN", "BRAZIL", 
                 "KOREA REPUBLIC", "SPAIN", "PORTUGAL", "SWITZERLAND"]

# Use list comprehension to apply Goal_area function to each country
Goal_type_list = [Goal_type(country) for country in Country_names]
# Combine data frames using pd.concat
Goal_type_all = pd.concat(Goal_type_list, ignore_index=True)
# Pivot a table of new variables
Goal_type_official = pd.melt(Goal_type_all, id_vars=['Team'], var_name='Goal type', value_name='Percent')


# Use list comprehension to apply function to each country
Fair_play_list = [Fair_play(country, wc) for country in Country_names]
# Combine data frames into one
Fair_play_all = pd.concat(Fair_play_list, ignore_index=True)
# Order teams by fouls
ordered_teams = Fair_play_all.sort_values(by='Fouls per match')['Team'].tolist()
# Pivot the dataset for plotting
Fair_play_official = Fair_play_all.melt(id_vars=['Team'],
                                        value_vars=['Fouls per match',  
                    'Red cards per match', 'Yellow cards per match'],
                     var_name='Types of unfair actions',
                     value_name='Average number of times per match')

# Use list comprehension to apply function to each country
Possession_list = [Possession(country, wc) for country in Country_names]
# Concatenate the list
Possession_official = pd.concat(Possession_list)
# Calculate median possession percentage for each team
median_possession = Possession_official.groupby('Team')['Possession percent'].median().reset_index()

# Use a list comprehension to apply the function to each country and combine the results
pressing_list = [pressing(country, wc) for country in Country_names]
pressing_official = pd.concat(pressing_list, axis=0)
# Calculate mean switches of play for each team
mean_switches = pressing_official.groupby('Team').agg({
        'Switches of play': 'mean'}).reset_index()
# Reorder the levels of the Team factor based on mean switches of play
team_order = mean_switches.sort_values('Switches of play')['Team']
pressing_official['Team'] = pd.Categorical(pressing_official['Team'], categories=team_order, ordered=True)

# Function to show the introduction page
def show_intro():
    st.markdown("""
        <h1 style='text-align: left; font-size: 100px;'>FOOTBALL FOR ALL</h1>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.title('Introduction')
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    with col1:

        st.markdown("<h3 style='font-size: 25px;'>Could we know your name to begin our journey. Please enter here!</h3>", unsafe_allow_html=True)
        prompt = st.text_input("")  # Empty label, as we're using the markdown above instead
        if prompt:
            st.markdown(f"""
            <p style="font-size: 30px;">
            <strong>Hello <i>{prompt}</i>. You are such a football enthusiast!</strong>
            </p>
                """, unsafe_allow_html=True)
    st.markdown(f"""
            <p style="font-size: 25px;">
            Welcome to our analysis website about FIFA World Cup 2022.<br>
            Here you will find all the necessary information you need to <br>
            study about football. <strong> Please turn off the left slidebar </strong> <br>
            of 4 different categories on next page to view content! 
             </p>
                """, unsafe_allow_html=True)
    
    if st.button("Click here to get started"):
        st.session_state.clicked = True
        st.experimental_rerun()  # Add this line

# Initialize session state
if 'clicked' not in st.session_state:
    st.session_state['clicked'] = False

if not st.session_state['clicked']:
    show_intro()
else:
    # Remove the background image when not on the intro page
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] > .main {
            background-image: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Define the categories
    categories = ["Football Analysis", "About FIFA WC 2022", "About our Dataset", "About our Team"]

# Create a sidebar with the categories
    st.sidebar.markdown('<p style="color: red; font-size: 40px;">CATEGORIES</p>', unsafe_allow_html=True)

# Use st.sidebar.radio without any custom formatting
    selected_category = st.sidebar.radio("", categories)

# Adjust the Streamlit theme to change radio button text size
    st.markdown("""
        <style>
        .stRadio [role=radiogroup] {
        font-size: 30px;
        }
        </style>
        """, unsafe_allow_html=True)

# Remove the custom CSS
# Add custom CSS to style the radio buttons
    st.markdown("""
<style>
.stRadio > div {
    font-size: 25px;
}
</style>
""", unsafe_allow_html=True)
# Handle category selection
    if selected_category == "Football Analysis":
        st.title(':blue[FOOTBALL ANALYSIS]')
    # Add tabs for different categories
        tab0, tab2, tab3, tab4 = st.tabs(["**GOAL TYPES**", "**UNFAIR PLAY ACTIONS**", "**BALL POSSESSION**", "**COUNTER & PRESSING TECHNIQUES**"])
        with tab0:
            st.subheader("Goal Type Distribution")
            st.markdown('<p style="font-family: SVN-Gilroy; font-size: 18px; font-weight: bold;">PLEASE SELECT A ROUND 16 TEAM BELOW!</p>', unsafe_allow_html=True)
            selected_country_goal = st.selectbox(label=" ", options=Country_names, key="goal_type_team_select")
            col1, col2 = st.columns([0.4, 0.6], gap="small")
            with col1:
                filtered_data_goal_type = Goal_type_official[Goal_type_official['Team'] == selected_country_goal]
                fig = px.pie(filtered_data_goal_type, values='Percent', names='Goal type', 
                     title=f'Pie Chart for {selected_country_goal}', 
                     color_discrete_sequence=['navajowhite', 'yellow', 'orange', 'orangered'], 
                     width=600, height=600)
                fig.update_layout(showlegend=True,
                          title= {'text':'GOAL TYPE DISTRIBUTION','font':{'family':'SVN-Gilroy','size':20}},
                          xaxis=dict(title="",title_font=dict(family="SVN-Gilroy",size=20, weight= 'bold')),
                          yaxis=dict(title="",title_font=dict(family="SVN-Gilroy",size=20, weight = 'bold')),
                          legend=dict(title="SELECTED TEAM", title_font=dict(family="SVN-Gilroy", size=18, weight = 'bold'),
                          font=dict(family="SVN-Gilroy", size=18, weight = 'bold'),
                          orientation="h",  # horizontal legend
                          x=0.5,  # centered horizontally
                          y=-0.2,  # positioned below the chart
                          xanchor="center",
                          yanchor="top"),
                          font=dict(family="SVN-Gilroy", size=20, weight = 'bold'),
                          paper_bgcolor="rgba(255,255,255,0)",
                          plot_bgcolor='rgba(255,255,255,0)')
                fig.update_traces(marker=dict(line=dict(color='white', width=1.5)), texttemplate='%{percent:.1%}', textposition='inside')
                st.plotly_chart(fig)
                # Display the plot in Streamlit
                penalty_url="https://www.si.com/.image/c_limit%2Ccs_srgb%2Cfl_progressive%2Ch_1200%2Cq_auto:good%2Cw_1200/MTk0NTM1NzUzNDQxNjE3NTE4/gonzalo-montiel.jpg"
                st.image(penalty_url, use_column_width=True)

            with col2:
                col2 = st.container()
                st.markdown('<span style="font-family: SVN-Gilroy; font-size: 25px; font-weight: bold;">Goal Type Analysis Of All Teams</span>', unsafe_allow_html=True)
                st.markdown("""
                <div style = "font-size: 20px;">
                These pie charts show the percentage of four different types of goals by sixteen teams in the round of 16 World Cup 2022. 
                Overall, it is observable that there is an overwhelming preference for assisted goals across all countries, while the occurrence of opponents' own goals is exceptionally uncommon.
                <br><br>
                The percentage of assisted goals is the majority in all countries, ranging from the lowest amount, roughly a quarter, in Poland to the entire 100% in Croatia and the United States. 
                Accordingly, this data is documented proof of the tendency to utilise collaborative gameplay, with Croatia and the US applying the most teamwork to scoring goals.
                <br><br>
                Following assisted goals, the frequency of individual goals is the second highest among the sixteen countries. 
                Representatives of this individualistic playing style are the Korea Republic and Senegal, with up to 40% of their goals being individual. 
                After that, the percentage of penalty goals is in third place. 
                It is essential to draw attention to the fact that in that year, Arsgentina broke the record for the most penalties for one team in a World Cup with five penalties. 
                Scoring four out of five penalties significantly contributed to bringing Argentina to first place in the 2022 World Cup, the second team with the highest percentage of penalty goals (26.67%). 
                That is just after Poland (33.33%), with an equal distribution of how they scored their goals in the last three mentioned goal types. 
                In contrast to the rate of other kinds of goals, opponents' own goals are rare, taking place only in Australia with a percentage of 25%.
                </div>    
                       """, unsafe_allow_html=True)
        
        with tab2:
            st.subheader("Unfair Play Actions")
            # Define custom CSS to adjust font sizes
            st.markdown(
            """
            <style>
            .css-145kmo2 p { 
            font-size: 25px; 
            }
            .css-1q8dd3e {
            font-size: 20px;
            }
            </style>
            """, 
            unsafe_allow_html=True
            )
            st.markdown('<p style="font-family: SVN-Gilroy; font-size: 18px; font-weight: bold;">PLEASE SELECT A ROUND 16 TEAM BELOW!</p>', unsafe_allow_html=True)
            selected_country_unfair_play = st.selectbox(label=" ", options=Country_names, key="unfair_play_team_select")
            col1, col2 = st.columns([0.4, 0.6], gap="small")
            with col2:
                filtered_data_unfair_play = Fair_play_official[Fair_play_official['Team'] == selected_country_unfair_play]

        # Pivot the data to get the actions as columns
            # Pivot the data to get the actions as columns
        # Pivot the data to get the actions as columns
                pivot_df = filtered_data_unfair_play.pivot(index='Team', columns='Types of unfair actions', values='Average number of times per match').reset_index()

    # Define the order of the bars
                action_types = ['Fouls per match', 'Red cards per match', 'Yellow cards per match']
                action_palette = {'Fouls per match': 'green', 'Red cards per match': 'red', 'Yellow cards per match': '#FFD700'}

    # Melt the pivoted dataframe for easy plotting
                melted_df = pivot_df.melt(id_vars=['Team'], value_vars=action_types, var_name='Action Type', value_name='Average Number of Times per Match')

    # Create the Plotly figure
                fig = px.bar(
                melted_df,
                x='Team',
                y='Average Number of Times per Match',
                color='Action Type',
                color_discrete_map=action_palette,
                barmode='group',
                height=800,
                width=1000
                )

    # Customize the layout
                fig.update_layout(
                    yaxis=dict(range=[0, 20]),  # Set a fixed y-axis limit
                    xaxis_title='Selected team',
                    yaxis_title='Average number of times per match',
                    legend_title_text='Types of Unfair Actions',
                    title={
                            'text': 'Unfair Play Actions',
                            'font': {'size': 30, 'color': 'black', 'family': 'SW-Gilroy', 'weight': 'bold'},
                            'x': 0.5,
                            'xanchor': 'center'
                            },
                legend=dict(
                    orientation="v",  # vertical orientation
                    yanchor="top",
                    y=1,  # position at the top
                    xanchor="right",
                    x=1,  # position at the right
                    title=dict(
                    text='Types of Unfair Actions',
                    font=dict(size=30, family="SW-Gilroy", color="black", weight="bold")  # Set legend title font size and bold
                    ),
                    font=dict(size=20, family="SW-Gilroy", color="black")  # Set legend item font size
                    )
                    )       
                
    # Annotate the bars with their respective values
                fig.update_traces(
                    texttemplate='%{y:.2f}',
                    textposition='outside',
                    textfont=dict(size=20,family="SW-Gilroy", color="black", weight="bold"))
                fig.update_layout(
                    xaxis=dict(
                        title_font=dict(size=25, family="SW-Gilroy", color="black", weight="bold"),
                        tickfont=dict(size=20, family="SW-Gilroy", color="black", weight="bold")
                    ),
                    yaxis=dict(
                        title_font=dict(size=25, family="SW-Gilroy", color="black", weight="bold"),
                        tickfont=dict(size=20, family="SW-Gilroy", color="black", weight="bold")
                        ))

                st.plotly_chart(fig)
                card_url="https://phapluatxahoi.kinhtedothi.vn/stores/news_dataimages/2022/122022/13/17/fifa-xoa-the-cho-cac-cau-thu-truoc-vong-ban-ket.jpg?rt=20221213172822"
                st.image(card_url, use_column_width=True)
        with col1:
                st.container()
                st.markdown('<span style="font-family: SVN-Gilroy; font-size: 25px; font-weight: bold;">Unfair Play Action Analysis Of All Teams</span>', unsafe_allow_html=True)
                st.markdown("""
            <div style= "font-size:20px;">
            The three bar charts illustrate the number of total fouls and red and yellow cards per match received by teams that
            enter the Round of 16. At first glance, most teams played not too unfairly, with very few red cards per match. It is also
            apparent that the Netherlands had the most unfair style of play, with the highest stats of all variables. Meanwhile,
            Spain and England seemed to perform the best fair play in football.
            <br><br>
            With an average count of approximately 17, total yellow cards of around 2.4, and total red cards of 0.2, the
            Netherlands has surged ahead, highlighting their too-competitive play style throughout the tournament. Argentina
            had also secured the position as the team with the third-highest total fouls and the second-highest number of total
            yellow cards per match. Argentina was considered the second-most fierce national team in the World Cup without
            any red cards because red cards rarely appeared.
            <br><br>               
            In contrast, Spain and England recorded the lowest statistics of unfair play. These two countries noticeably created a
            big gap with the rest of the countries in the number of yellow cards. While England only reported an average of 1
            yellow card per 5 matches, Spain would need about two games to receive a punishment like that.
            </div>
                            """, unsafe_allow_html=True)
        with tab3:
            st.subheader("Ball Possession Percentage Range")
            col1, col2 = st.columns([0.6, 0.4], gap="small")

            with col1:
        # Order teams by median possession percentage
                median_possession = Possession_official.groupby('Team')['Possession percent'].median().sort_values(ascending=False)
                ordered_teams = median_possession.index.tolist()
        # Add a slider for selecting the number of countries
                st.markdown('<p style="font-family: SVN-Gilroy; font-size: 18px; font-weight: bold;">PLEASE SCROLL TO SELECT THE NUMBER OF CUNTRIES TO DISPLAY !</p>', unsafe_allow_html=True)
                num_countries = st.slider("", 
                          min_value=5, 
                          max_value=15, 
                          value=15)

        # Filter the teams based on the slider value
                selected_teams = ordered_teams[:num_countries]
        # Create a color palette that's guaranteed to have enough colors
                country_colors = px.colors.qualitative.Plotly * (num_countries // len(px.colors.qualitative.Plotly) + 1)

        # Create the plot using Plotly
                fig = go.Figure()

                for i, team in enumerate(selected_teams):
                    team_data = Possession_official[Possession_official['Team'] == team]['Possession percent']
                    fig.add_trace(go.Box(
                    y=[team] * len(team_data),
                    x=team_data,
                    name=team,
                    orientation='h',
                    marker_color=country_colors[i]
                    ))


                fig.update_layout(
                height=600,
                width=800,
                yaxis_title='Top Round 16 teams in Possession',
                xaxis_title='Possession (%)',
                yaxis_categoryorder='array',
                yaxis_categoryarray=selected_teams[::-1], 
                yaxis_tickfont=dict(size=20,family="SW-Gilroy", color= "black",weight="bold"),
                xaxis_tickfont=dict(size=20, family="SW-Gilroy",color="black"),
                xaxis_title_font=dict(size=30, family="SW-Gilroy", weight="bold",color="black"),
                yaxis_title_font=dict(size=30, weight="bold", color="black"),
                showlegend=False
                )
                fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
                fig.update_yaxes(showgrid=False)

                st.plotly_chart(fig, use_container_width=True)
                possession_url="https://cloudfront-us-east-2.images.arcpublishing.com/reuters/KVR5YXPPORIOPATIZPDP4D7PJI.jpg"
                st.image(possession_url, use_column_width=True)
                possession2_url="https://lh3.googleusercontent.com/HgGcsLnU9nEdBczcwImV_NVCDFlsWzHl9Oyog3EwcP4Qiq25udQoNQd--m-EHrbLnWiZr8IRFnTKnZkFCuPsFR4NXL3Jp7BO2VAeYkKgrnZzLfY=s750"
                st.image(possession2_url, use_column_width=True)
            with col2:
                col2 = st.container()
                st.markdown('<span style="font-family: SVN-Gilroy; font-size: 25px; font-weight: bold;">Ball Possession Analysis Of All Teams</span>', unsafe_allow_html=True)
                st.markdown("""
                <div style="font-size: 20px;">
                The following box plots depict the possession distribution of the top 16 teams in the 2022 World Cup. 
                <br><br>  
                Most teams ranged their median possession rate from 40% to 60%, suggesting a balanced approach to most teams' possession. However, there were also cases of national teams that needed to be more dominant and flexible. There were 11 teams within the range of 40% to 60%. This list included most of the top-ranking countries and the 3 out of 4 teams that entered the semi-finals (Argentina, France, and Croatia). This showed the trend of each team trying to possess the ball with their opponents. This suggested that dominance in game tempo and flow was not the only aspect influencing the match's result. Spain had the most excellent median possession rate (72%). The country attempted to take over the game with persistent ball control, with the highest recorded rate of about 78%. This was more than fivefold the lowest possession rate, less than 15%. Despite having the lowest median - only around 28% - Japan holds the most extensive possession range among the 16 teams. The wide range of possession percentages for Japan (from 8% to 47%) indicates that Japan's possession varied significantly throughout the matches. Also, two of the four top teams that year, Argentina and Morocco, followed Japan in this trend. This suggested that the gameplay of some teams might have been more flexible than other teams, with high and low possession instances.
                <br><br>
                Specific teams' boxplots, such as those of the Netherlands, England, and Portugal, had relatively limited ranges. These results demonstrated a strictly consistent possession rate over matches, which relates to the players' tactical discipline and technical ability to carry out the game plan. However, there were several matches when their possession rate unexpectedly increases or decreases compared to their medians, resulting in some outliers outside the main box. These outliers could vary based on which opponents force those teams to adjust their style of play.
                </div>""", unsafe_allow_html=True)
        with tab4:
            st.subheader("Counter & Pressing Techniques")
            st.markdown('<p style="font-family: SVN-Gilroy; font-size: 18px; font-weight: bold;">PLEASE SELECT 1 or 2 TECHNIQUE(S) BELOW!</p>', unsafe_allow_html=True)
    
    # Checkboxes for selection
            switches_of_play_selected = st.checkbox('Switches of play')
            forced_turnovers_selected = st.checkbox('Forced turnovers')
            col1, col2 = st.columns([0.4, 0.6], gap="small")
            with col2:
                if switches_of_play_selected:
                    custom_palette = {'Switches of play': '#ff5b00'}
                    fig_switches = px.line(
                    pressing_official, 
                    x='Team', 
                    y='Switches of play', 
                    title='Switches of play',
                    markers=True,
                    color_discrete_sequence=[custom_palette['Switches of play']]
                    )
                    fig_switches.update_layout(
                    height=600,  # Increase this value to make the plot taller
                    title=dict(
                        text='Switches of play',
                        font=dict(size=30, family="SW-Gilroy", color="black", weight="bold"),
                        x=0.5),
                    xaxis_title='Round of 16 Teams',
                    yaxis_title='Average number of times per match',
                    legend_title='Switches of play',
                    xaxis_tickangle=-45,
                    xaxis_title_font=dict(size=20, family="SW-Gilroy", color="black", weight="bold"),
                    yaxis = dict(
                                title_font=dict(size=25, family="SW-Gilroy", color="black", weight="bold"),
                                tickfont=dict(size=20, family="SW-Gilroy", color="black", weight="bold"),
                                range=[0, 14],dtick = 2),
                    xaxis=dict(
                        title_font=dict(size=25, family="SW-Gilroy", color="black", weight="bold"),
                        tickfont=dict(size=20, family="SW-Gilroy", color="black", weight="bold")
                        ))
                      # Set y-axis range and step
                    st.plotly_chart(fig_switches, use_container_width=True)

                if forced_turnovers_selected or (not switches_of_play_selected and not forced_turnovers_selected):
                    custom_palette = {'Forced turnovers': '#742802'}
                    fig_turnovers = px.line(
                    pressing_official, 
                    x='Team', 
                    y='Forced turnovers', 
                    title='Forced turnovers',
                    markers=True,
                    color_discrete_sequence=[custom_palette['Forced turnovers']]
                    )
                    fig_turnovers.update_layout(
                    height = 600,
                    title=dict(
                        text='Forced turnovers',
                        font=dict(size=30, family="SW-Gilroy", color="black", weight="bold"),
                        x=0.5),
                    xaxis_title='Round of 16 Teams',
                    yaxis_title='Average number of times per match',
                    legend_title='Forced turnovers',
                    xaxis_tickangle=-45,
                    xaxis_title_font=dict(size=20, family="SW-Gilroy", color="black", weight="bold"),
                    yaxis_title_font=dict(size=20, family="SW-Gilroy", color="black", weight="bold"),
                    yaxis=dict(
                        title_font=dict(size=25, family="SW-Gilroy", color="black", weight="bold"),
                        tickfont=dict(size=20, family="SW-Gilroy", color="black", weight="bold"),
                        range=[55,95],dtick = 5),
                    xaxis=dict(
                        title_font=dict(size=25, family="SW-Gilroy", color="black", weight="bold"),
                        tickfont=dict(size=20, family="SW-Gilroy", color="black", weight="bold")
                        ))
                    st.plotly_chart(fig_turnovers, use_container_width=True)
                    pressing2_url="https://www.coachesvoice.com/wp-content/webpc-passthru.php?src=https://www.coachesvoice.com/wp-content/uploads/2022/11/spain1.jpg&nocache=1"
                    st.image(pressing2_url, use_column_width=True)
            with col1:
                col1 = st.container()
                st.markdown('<span style="font-family: SVN-Gilroy; font-size: 25px; font-weight: bold;">Counter & Pressing Analysis Of All Teams</span>', unsafe_allow_html=True)
                st.markdown("""
            <div style="font-size: 20px;">
            The line plots illustrate the average number of forced turnovers and switches of play for the 16 best teams in the World Cup 2022.
            <br><br>
            On the one hand, the mean number of forced turnovers varies significantly, ranging from 58 to 91, which is somewhat more
            significant than the switches' mean. The highest turnover mean was nine times the highest switches mean. That proved that
            the 16 most competitive World Cup 2022 teams had comparable abilities to press their opponents rather than escape that
            pressure.
            <br><br>
            On the other hand, while maintaining a consistent line throughout, the number of play switches revealed a four-times
            difference between the highest team (Korea Republic with 12) and the lowest team (Japan with 3). Another noteworthy aspect
            is that Argentina, the competition's champion, and France, the runner-up, had meager force-a-turnover ratings of 5.5 and 4,
            respectively. This could be attributed to each team's tactical style of play, possibly already dominating the opposition team, so
            there was no need to overcome pressing for top-ranking countries.
            <br><br>
            Despite having the most significant average number of switches of play (12), the Korea Republic has one of the lowest statistics
            among pressing competitors (about 65). It can be explained that the Korea Republic is not considered a competitive team in
            the world football ranking. Thus, their strategy might focus on adapting to their opponents' dominant circumstances. With the
            force-a-turnover stats, Spain maintains its lead with 90 while demonstrating its strength and flexibility when their switches
            place them in the top 5 teams.
            </div>
            """, unsafe_allow_html=True)
        
    elif selected_category == "About FIFA WC 2022":
    # Import and run the code from the second file
        from fifa_wc_2022 import show_fifa_wc_2022
        show_fifa_wc_2022()

    elif selected_category == "About our Dataset":
        from our_dataset import show_our_dataset
        show_our_dataset()

    elif selected_category == "About our Team":
    # Your existing team info code
        from our_team import show_our_team
        show_our_team()
