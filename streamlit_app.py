import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image

"""
# Chess

Edit `/streamlit_app.py` to customize this app to your heart's desire

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:

"""
st.sidebar.write('Menu')
add_selectbox = st.sidebar.selectbox('Choose an opening', ('General', 'Top 5 - titled', 'Top 5 - untitled', 'Indian Defense', 'Modern Defense', "King's Indian Attack", 'Sicilian Defense Closed', 'Pirc Defense', 'Scandinavian Defense Mieses Kotroc Variation', 'Caro-Kann Defense', 'Horwitz Defense'))
im_id_t = Image.open('/app/streamlit-example/Indian Defense - titled.png') 
im_id_t_a = Image.open('/app/streamlit-example/Indian Defense - titled - average.png')
im_id_u = Image.open('/app/streamlit-example/Indian Defense - untitled.png') 
im_id_u_a = Image.open('/app/streamlit-example/Indian Defense - untitled - average.png') 
im_id_vs = Image.open('/app/streamlit-example/Indian Defense - titled vs untitled.png')
im_md_t = Image.open('/app/streamlit-example/Modern Defense - titled.png')
im_md_t_a = Image.open('/app/streamlit-example/Modern Defense - titled - average.png')
im_kia_t = Image.open("/app/streamlit-example/King's Indian Attack - titled.png")
im_kia_t_a = Image.open("/app/streamlit-example/King's Indian Attack - titled - average.png")
im_sdc_t = Image.open("/app/streamlit-example/Sicilian Defense Closed - titled.png")
im_sdc_t_a = Image.open("/app/streamlit-example/Sicilian Defense Closed - titled - average.png") 
im_sdc_u = Image.open("/app/streamlit-example/Sicilian Defense Closed - untitled.png")
im_sdc_u_a = Image.open("/app/streamlit-example/Sicilian Defense Closed - untitled - average.png")
im_sdc_vs = Image.open('/app/streamlit-example/Sicilian Defense Closed - titled vs untitled.png')
im_pd_t = Image.open('/app/streamlit-example/Pirc Defense - titled.png')
im_pd_t_a = Image.open('/app/streamlit-example/Pirc Defense - titled - average.png') 
im_sdm_u = Image.open('/app/streamlit-example/Scandinavian Defense Mieses-Kotroc Variation - untitled.png')
im_sdm_u_a = Image.open('/app/streamlit-example/Scandinavian Defense Mieses-Kotroc Variation - untitled -average.png')
im_ckd_u = Image.open('/app/streamlit-example/Caro-Kann Defense - untitled.png') 
im_ckd_u_a = Image.open('/app/streamlit-example/Caro-Kann Defense - untitled - average.png')
im_hd_u = Image.open('/app/streamlit-example/Horwitz Defense - untitled.png')
im_hd_u_a = Image.open('/app/streamlit-example/Horwitz Defense - untitled - average.png') 
im_titled_a = Image.open('/app/streamlit-example/Titled - average.png')
im_untitled_a = Image.open('/app/streamlit-example/Untitled - average.png')

if add_selectbox == 'General':
  st.title('General')
  """
  Chess is one of the most popular boardgames in the world and has reseantly become even more popular throught the tv show 'The Queens Gambit'. 
  We also became intrested in this topic so when we had to chose a topic for our research we chose chess.
  
  Everybody in the world is able to play chess, but of course some people are good at it and others not so much. Some people are even given official chess titles, such as Grand Master.
  We thought it would be fun to look at people who play chess and have a titled versus normal chess players like you and me, those without a title. Now we had to get some data.
  We used data from the popular chess website called lichess. On this website there are so called tournaments. They have tournaments in which everyone can enter and tournaments where only people with a title can enter.
  Thus we chose to get all the games from a tournament played by normal players and all the games from the bullet titled arenea, both of these tournaments were from jan 2022.
  
  A chess game consist of an opening, a mid game and an end game. In our research we decided to narrow our analyses down to the openings in chess, but there are over a 1000 named opening and variations in chess.   
  Thus we decide to look at the openings which were most popular in our databases. We chose to look at the 5 most played openings in our titled players games data base and at the 5 most played openings in our untitled players games datat base.
  
  In all the grapths that are shown you will find the number of moves on the x-axis and the evals on the y-axis. The evals are number calculated by a computer, that is supposed to represent who has a higher change of winning.
  If the eval is positive then white has a higher change at winning, but if it is a negative value then black is more likely to win. These numbers can change a lot during the games, so it can go from negative to positve and back.
  Every game start with an eval of 0 since black and white are equally likely to win at the start of a game.
  """
  
if add_selectbox == 'Top 5 - titled':
  st.title('Top 5 openings titled')
  """
  Within our titled player data base we found 1076 different openings and variations. The 5 most common ones were the Indian Defense, the Modern Defense, the King's Indian Attack, the Sicilian Defense Closed and the Pirc Defense.
  The Indian Defense was played 128 times (1.9%) The Modern Defense was played 119 times (1.8%). The King's Indian Attack was played 89 times (1.4%). The Sicilian Defense Closed was played 82 times (1.2%) and the Pirc Defense was played 78 times (1.2%).
  
  In the graph below you can see the graph of all the average games of the top 5 openings of the titled players. The graph is cut of at the 100th move since not all games are of the same length so this way the end of the graph which might be made up of 2 games is not visible.
  You can see more detailed graphs of the different opening on their own page.
  """  
  st.image(im_titled_a)
  """
  As you can see all the lines stay very close to the mean of 0 at the beginning. Except around the 5th move wher both the pirc defense and the modern defense make a small and short jump into the positive.
  This suggests that the white players has an opertunity there, but almost always loses it.
  All the lines stay very close to 0 at the beginning but seem to all be positive untill around the 22th move when the pirc defense goes deeply into the negative. This seems to suggest that all the favorite openings sligetly favor white a little bit.
  Which makes sence since white plays the first move and therefore naturally has a small advantage.
  It also seems to me that the green line, thus the Indian defense stays closed to the mean, this might suggest that it allows for a very equal setting that continuos for the rest of the game and might explain why it is the all time favorite.
  """
  
if add_selectbox == 'Top 5 - untitled':
  st.title('Top 5 openings untitled')
  """
  Within our untitled player data base we found 478 different openings and variations. The 5 most common ones were the Scandinavian Defense Mieses Kotroc Variation, the Caro-Kann Defense, the Sicilian Defense Closed, the Indian Defense and the Horwitz Defense.
  The Scandinavian Defense Mieses Kotroc Variation was played 21 times (2%). The Caro-Kann Defense was played 21 times (2%). The Sicilian Defense Closed was played 19 times (1.8%). The Indian Defense was played 17 times (1.6%). The Horwitz Defense was played 14 times (1.4%).
  So it seems that the two most popular openings for titled and untitled players are played almost as often, but there are small diferences in how often other 3 are choosen.
  
  In the graph below you can see the graph of all the average games of the top 5 openings of the untitled players. The graph is cut of at the 75th move since not all games are of the same length so this way the end of the graph which might be made up of 2 games is not visible.
  You can see more detailed graphs of the different opening on their own page.
  """  
  st.image(im_untitled_a)
  """
  As you can see unlike with the titled players the untitled players have an opening that moves away from the mean of 0 very quickly. This is the Scandinavian Defense Mieses Kotroc Variation. It almost instantly has an postive eval,
  this seems to suggest that this opening is very favorable for white. The other lines seem to stay around the zero line until at least the 10th move. After this we can also see the Horwitz Defense go away from the zero line and join the Scandinavian Defense line in the positive.
  We can also see that the Sililian Defence moves away from the zero line after about the 25th move, and becomes negative. Thus favoring the black player.
  
  As you can see these lines are much less steady then the lines of the titled players. This could be because the titled players have a better insight into the game and can thus both control the opening so that neither has a bigger change at winning.
  But it could also be that we have more games to make up the average in titled players than the untitled players and that that is what makes the lines of the titled players smoother.
  """
  
if add_selectbox == 'Indian Defense':
  st.title('Openings: Indian Defense')
  """
  The Indian Defense is in the top 5 of untitled players and in the top 5 of titled players. We are first going to have a look at titled players, then at untitled players. 
  And then we end with a comparison of the 2 types of players.
  The Indian Defense is played 128 times by titled players, and the longest indian defense game is a 160 moves.
  """
  st.image(im_id_t)
  st.image(im_id_t_a)
  """
  Now we look at the untitled players. The Indian Defense is played 17 times by titled players, and the longest sicilian defense defense game is a 129 moves.
  """
  st.image(im_id_u)
  st.image(im_id_u_a) 
  st.image(im_id_vs)
  
if add_selectbox == 'Modern Defense':
  st.title('Openings: Modern Defense')
  """
  The Modern Defense is only in the top 5 of titled players. Thus we are only going to look at the titled players. 
  The Modern Defense is played 119 times by titled players, and the longest modern defense game is 228 moves.
  """
  st.image(im_md_t)
  st.image(im_md_t_a)

if add_selectbox == "King's Indian Attack":
  st.title("Openings: King's Indian Attack")
  """
  The King's Indian Attack is only in the top 5 of titled players. Thus we are only going to look at the titled players. 
  The King's Indian Attack is played 89 times by titled players, and the longest king's indian attack game is 205 moves.
  """
  st.image(im_kia_t)
  st.image(im_kia_t_a)
  
if add_selectbox == 'Sicilian Defense Closed':
  st.title('Openings: Sicilian Defense Closed')
  """
  The Sicilian Defense Closed is in the top 5 of untitled players and in the top 5 of titled players. We are first going to have a look at titled players, then at untitled players. 
  And then we end with a comparison of the 2 types of players.
  The Sicilian Defense Closed is played 82 times by titled players, and the longest sicilian defense defense game is a 180 moves.
  """
  st.image(im_sdc_t)
  st.image(im_sdc_t_a)
  """
  Now we look at the untitled players. The Sicilian Defense Closed is played 19 times by titled players, and the longest sicilian defense defense game is a 114 moves.
  """
  st.image(im_sdc_u)
  st.image(im_sdc_u_a)
  """
  And now we shall compare the two types of players
  """
  st.image(im_sdc_vs)

if add_selectbox == "Pirc Defense":
  st.title("Openings: Pirc Defense")
  """
  The Pirc Defense is only in the top 5 of titled players. Thus we are only going to look at the titled players. 
  The Pirc Defense is played 78 times by titled players, and the longest pirc defense game is 197 moves.
  """
  st.image(im_pd_t)
  st.image(im_pd_t_a)
  
if add_selectbox == 'Scandinavian Defense Mieses Kotroc Variation':
  st.title("Openings: Scandinavian Defense: Mieses-Kotroc Variation")
  """
  The Scandinavian Defense: Mieses-Kotroc Variation is only in the top 5 of untitled players. Thus we are only going to look at the untitled players. 
  The Scandinavian Defense: Mieses-Kotroc Variation is played - times by untitled players, and the longest Scandinavian Defense: Mieses-Kotroc Variation game is 144 moves.
  """
  st.image(im_sdm_u)
  st.image(im_sdm_u_a)

if add_selectbox == 'Caro-Kann Defense':
  st.title("Openings: Caro-Kann Defense")
  """
  The Caro-Kann Defense is only in the top 5 of untitled players. Thus we are only going to look at the untitled players. 
  The Caro-Kann Defense is played 21 times by untitled players, and the longest Caro-Kann Defense game is 124 moves.
  """
  st.image(im_ckd_u)
  st.image(im_ckd_u_a)
  
if add_selectbox == 'Horwitz Defense':
  st.title("Openings: Horwitz Defense")
  """
  The Horwitz Defense is only in the top 5 of untitled players. Thus we are only going to look at the untitled players. 
  The Horwitz Defense is played 14 times by untitled players, and the longest Horwitz Defense game is 127 moves.
  """
  st.image(im_hd_u)
  st.image(im_hd_u_a)  
  
