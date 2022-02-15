import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image

"""
This project is based on the work of Kamiliah, Pawel and Kes, and writen by Kes.

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

if add_selectbox != 'General':
  """
  In all the graphs that are shown you will find the number of moves on the x-axis and the evals on the y-axis. The evals are numbers calculated by a computer, that is supposed to represent who has a higher change of winning.
  If the eval is positive then white has a higher change at winning, but if it is a negative value then black is more likely to win. These numbers can change a lot during the games, so it can go from negative to positive and back.
  Every game start with an eval of 0 since black and white are equally likely to win at the start of a game.
  """

if add_selectbox == 'General':
  st.title('General')
  """  
  Chess is one of the most popular boardgames in the world and has recently become even more popular through the tv show 'The Queens Gambit'. 
  We also became interested in this topic, so when we had to chose a topic for our research we chose chess.
  
  Everybody in the world is able to play chess, but of course some people are good at it and others not so much. Some people are even given official chess titles, such as Grand Master.
  We thought it would be fun to look at people who play chess and have a titled versus normal chess players like you and me, those without a title. Now we had to get some data.
  We used data from the popular chess website called lichess. On this website there are so called tournaments. They have tournaments in which everyone can enter and tournaments where only people with a title can enter.
  Thus we chose to get all the games from a bullet tournament played by normal players and all the games from the bullet titled arena, both of these tournaments were from jan 2022 (version of chess that restricst the players time to make a move).
  
  A chess game consist of an opening, a mid game and an end game. In our research we decided to narrow our analyses down to the openings in chess, but there are over a 1000 named opening and variations in chess.   
  Thus we decide to look at the openings which were most popular in our databases. We chose to look at the 5 most played openings in our titled players games data base and at the 5 most played openings in our untitled players games data base.
  
  In all the graphs that are shown you will find the number of moves on the x-axis and the evals on the y-axis. The evals are numbers calculated by a computer, that is supposed to represent who has a higher change of winning.
  If the eval is positive then white has a higher change at winning, but if it is a negative value then black is more likely to win. These numbers can change a lot during the games, so it can go from negative to positive and back.
  Every game start with an eval of 0 since black and white are equally likely to win at the start of a game.
  """
  
if add_selectbox == 'Top 5 - titled':
  st.title('Top 5 openings titled')
  """
  Within our titled player data base we found 1076 different openings and variations. The 5 most common ones were the Indian Defense, the Modern Defense, the King's Indian Attack, the Sicilian Defense Closed and the Pirc Defense.
  The Indian Defense was played 128 times (1.9%) The Modern Defense was played 119 times (1.8%). The King's Indian Attack was played 89 times (1.4%). The Sicilian Defense Closed was played 82 times (1.2%) and the Pirc Defense was played 78 times (1.2%).
  
  In the graph below you can see the graph of all the average games of the top 5 openings of the titled players. The graph is cut of at the 100th move since not all games are of the same length so this way the end of the graph which might be made up of 2 games is not visible.
  We don't want it to be visible because an average made up of say 2 games is not an average that is of interest to us. You can see more detailed graphs of the different opening on their own page.
  """  
  st.image(im_titled_a)
  """ 
  As you can see all the lines stay very close to the zero at the beginning. Except around the 5th move where both the Pirc Defense and the Modern Defense make a small and short jump into the positive.
  This suggests that the white players has an opportunity there, but almost always loses this opportunity.
  All the lines stay very close to 0 at the beginning but seem to all be positive until around the 22th move when the Pirc Defense goes deeply into the negative. This seems to suggest that all the favourite openings slightly favour white a little bit.
  Which makes sense since white plays the first move and therefore naturally has a small advantage.
  It also seems to me that the green line, thus the Indian Defense stays closest to the zero line, this might suggest that it allows for a very equal setting that continuous for the rest of the game and might explain why it is the all time favourite.
  """
  
if add_selectbox == 'Top 5 - untitled':
  st.title('Top 5 openings untitled')
  """ 
  Within our untitled player data base we found 478 different openings and variations, so quite a lot less then in the titled player data base. The 5 most common ones were the Scandinavian Defense Mieses Kotroc Variation, the Caro-Kann Defense, the Sicilian Defense Closed, the Indian Defense and the Horwitz Defense.
  The Scandinavian Defense Mieses Kotroc Variation was played 21 times (2%). The Caro-Kann Defense was played 21 times (2%). The Sicilian Defense Closed was played 19 times (1.8%). The Indian Defense was played 17 times (1.6%). The Horwitz Defense was played 14 times (1.4%).
  So it seems that the two most popular openings for titled and untitled players are played almost as often, but there are small differences in how often other 3 are chosen.
  
  In the graph below you can see the graph of all the average games of the top 5 openings of the untitled players. The graph is cut of at the 75th move since not all games are of the same length so this way the end of the graph which might be made up of 2 games is not visible.
  You can see more detailed graphs of the different opening on their own page.
  """  
  st.image(im_untitled_a)
  """ 
  As you can see unlike with the titled players the untitled players have an opening that moves away from the mean of 0 very quickly. This is the Scandinavian Defense Mieses Kotroc Variation. It almost instantly has a positive eval,
  this seems to suggest that this opening is very favourable for white. The other lines seem to stay around the zero line until at least the 10th move. After this we can see the Horwitz Defense go away from the zero line and join the Scandinavian Defense line in the positive.
  We can also see that the Sicilians Defence Closed moves away from the zero line after about the 25th move and becomes negative. Thus, favouring the black player.
  
  As you can see these lines are much less steady than the lines of the titled players. This could be because the titled players have a better insight into the game and can thus both control the opening so that neither has a bigger change at winning.
  But it could also be that we have more games to make up the average in titled players than the untitled players and that that is what makes the lines of the titled players smoother.
  """
  
if add_selectbox == 'Indian Defense':
  st.title('Openings: Indian Defense')
  """ 
  The Indian Defense is in the top 5 of untitled players and in the top 5 of titled players. We are first going to have a look at titled players, then at untitled players. 
  And then we end with a comparison of the 2 types of players.
  The Indian Defense is played 128 times by titled players, and the longest Indian Defense game is 160 moves.
  
  Below you can see all the 128 games of the Indian Defense by the titled players, and whilst I think this looks very pretty it isn't exactly readable. Therefore we continue with the average of all the games of the titled players.
  """
  st.image(im_id_t)
  """  
  As you might have noticed not all the games are as long as the other. This means that nearing the end of the average line it might be made from 2 of the 128 games, thus it is not telling us much about the average Indian Defense game.
  Therefore we will not analyse the end of this line but only up to around the 100th move.
  """
  st.image(im_id_t_a)
  """  
  From the graph we can see that the average Indian Defense game played by titled players stays around the zero line for quite a long time. Although it does seem like the evals are slightly positive in the beginning, and thus favour the white player.
  Somewhere between the 50th move and the 75th move we can however see that the average game starts to favour the black player.

  Now we look at the untitled players. The Indian Defense is played 17 times by titled players, and the longest Sicilian Defense game is a 129 moves.
  Below you can see all the 17 games of the Indian Defense by untitled players, but again these are still fare to many lines to analyse with our eyes. Therefore we continue with the average of all the games of the untitled players.
  """
  st.image(im_id_u)
  """
  We of course still have the same problem with the average line as we did with the untitled player. It however does seem that the games are a lot shorter so we shall not analyse them past the 50th move.
  """
  st.image(im_id_u_a)
  """  
  From the graph we can see that the average Indian Defense game played by untitled players stays around the zero line at the beginning with a slight trend downwards, thus favouring the black player.
  
  Now that we have looked at these lines individually we will now compare them. 
  But before we look at the actual lines it seems interesting to note that the longest titled player game went on for about 30 moves longer then the longest untitled player game, with respect to the Indian Defense.
  """
  st.image(im_id_vs)
  """  
  In the graph you can see that the titled players and the untitled players have almost the same evals for the first 10 moves. This is probably due to the fact that they have the same opening.
  You can also see the line of the titled players stays closer to the zero line whereas the untitled player line is slightly lower. This suggests that the Indian Defense has a slight advantage for the black player if you are not playing with a very advanced white player.
  Because if the white player is very good then this player can still make it so that nobody has a real advantage.
  We can also see that the titled players games are much steadier than that of the untitled players.
  """
  
if add_selectbox == 'Modern Defense':
  st.title('Openings: Modern Defense')
  """
  The Modern Defense is only in the top 5 of titled players. Thus we are only going to look at the titled players. 
  The Modern Defense is played 119 times by titled players, and the longest Modern Defense game is 228 moves.
  
  Below you can see all the 119 games of the Modern Defense by the titled players, and whilst I think this looks very pretty it isn't exactly readable. Therefore we continue with the average of all the games of the titled players.
  """
  st.image(im_md_t)
  """
  As you might have noticed not all the games are as long as the other. This means that nearing the end of the average line it might be made from 2 of the 119 games, thus it is not telling us much about the average Modern Defense game.
  Therefore we will not analyse the end of this line but only up to around the 100th move.
  """
  st.image(im_md_t_a)
  """
  The Modern Defense seems to favour the white player a little bit, since the line is just above the zero line for quite a number of moves. We can also see that at the first or second move the line goes up quite a bit for so early in the game.
  """

if add_selectbox == "King's Indian Attack":
  st.title("Openings: King's Indian Attack")
  """
  The King's Indian Attack is only in the top 5 of titled players. Thus we are only going to look at the titled players. 
  The King's Indian Attack is played 89 times by titled players, and the longest King's Indian Attack game is 205 moves.
  
  Below you can see all the 89 games of the King's Indian Attack by the titled players, and whilst I think this looks very pretty it isn't exactly readable. Therefore we continue with the average of all the games of the titled players.
  """
  st.image(im_kia_t)
  """
  As you might have noticed not all the games are as long as the other. This means that nearing the end of the average line it might be made from 2 of the 89 games, thus it is not telling us much about the average King's Indian Attack game.
  Therefore we will not analyze the end of this line but only up to around the 100th move.
  """
  st.image(im_kia_t_a)
  """
  We can see in the graph that the King's Indian Attack is slightly positive for the first 50 moves and then seems to become negative. It thus favours the white player and then the black player.
  """
  
if add_selectbox == 'Sicilian Defense Closed':
  st.title('Openings: Sicilian Defense Closed')
  """
  The Sicilian Defense Closed is in the top 5 of untitled players and in the top 5 of titled players. We are first going to have a look at titled players, then at untitled players. 
  And then we end with a comparison of the 2 types of players.
  The Sicilian Defense Closed is played 82 times by titled players, and the longest Sicilian Defense game is a 180 moves.
  
  Below you can see all the 82 games of the Sicilian Defense Closed by the titled players, and whilst I think this looks very pretty it isn't exactly readable. This is why we continue with the average of all the games of the titled players.
  """
  st.image(im_sdc_t)
  """
  As you might have noticed not all the games are as long as the other. This means that nearing the end of the average line it might be made from 2 of the 82 games, thus it is not telling us much about the average Sicilian Defense Closed game.
  Therefore we will not analyse the end of this line but only up to around the 100th move.
  """
  st.image(im_sdc_t_a)
  """
  From the graph we can see that the average Sicilian Defense closed game played by titled players stays around the zero line for quite a long time. The graph is slightly positive from the beginning and does not seem to start favouring the black player until after the 100th move.

  Now we look at the untitled players. The Sicilian Defense Closed is played 19 times by titled players, and the longest Sicilian Defense game is a 114 moves.
  Below you can see all the 19 games of the Sicilian Defense Closed by untitled players, but again these are still fare to many lines to analyse with our eyes. This is why we continue with the average of all the games of the untitled players.
  """
  st.image(im_sdc_u)
  """
  We of course still have the same problem with the average line as we did with the untitled player. It however does seem that the games are a lot shorter so we shall not analyse them past the 50th move.
  """
  st.image(im_sdc_u_a)
  """
  From the graph we can see that the average Sicilian Defense Closed game played by untitled players stays around the zero line at the beginning with a slight trend downwards, thus favouring the black player.
  
  Now that we have looked at these lines individually we will now compare them. 
  But before we look at the actual lines it seems interesting to note that the longest titled player game went on for about 70 moves longer then the longest untitled player game, with respect to the Sicilian Defense Closed.
  """
  st.image(im_sdc_vs)
  """
  As you can see the line of the titled players stays closer to the zero line with a slight trend upwards whereas the untitled player line is less stable and lower. 
  This suggests that the Sicilian Defense Closed has a slight advantage for the black player if you are not playing with a very advanced white player.
  Because if the white player is very good then this player can still make it so that nobody has a real advantage.
  We can also see that the two lines are the exact same for about 5 moves, which probably means that on average the titled player and the untitled player play the exact same moves.
  """

if add_selectbox == "Pirc Defense":
  st.title("Openings: Pirc Defense")
  """
  The Pirc Defense is only in the top 5 of titled players. Thus we are only going to look at the titled players. 
  The Pirc Defense is played 78 times by titled players, and the longest Pirc Defense game is 197 moves.
  
  Below you can see all the 78 games of the Pirc Defense by the titled players, and whilst I think this looks very pretty it isn't exactly readable. This is why we continue with the average of all the games of the titled players.
  """
  st.image(im_pd_t)
  """
  As you might have noticed not all the games are as long as the other. This means that nearing the end of the average line it might be made from 2 of the 78 games, thus it is not telling us much about the average Pirc Defense game.
  Therefore we will not analyse the end of this line but only up to around the 75th move.
  """
  st.image(im_pd_t_a)
  """
  In the graph of the average titled Pirc Defense game you can see that white has the advantage for about 5 moves since the graph is positive, but that after this it starts to go down and into the negative around the 25th move.
  """
  
if add_selectbox == 'Scandinavian Defense Mieses Kotroc Variation':
  st.title("Openings: Scandinavian Defense: Mieses-Kotroc Variation")
  """
  The Scandinavian Defense: Mieses-Kotroc Variation is only in the top 5 of untitled players. Thus we are only going to look at the untitled players. 
  The Scandinavian Defense: Mieses-Kotroc Variation is played - times by untitled players, and the longest Scandinavian Defense: Mieses-Kotroc Variation game is 144 moves.
  
  Below you can see all the 21 games of the Scandinavian Defense Mieses Kotroc Variation by the untitled players, and whilst I think this looks very pretty it isn't exactly readable. Therefore we continue with the average of all the games of the untitled players.
  """
  st.image(im_sdm_u)
  """
  As you might have noticed not all the games are as long as the other. This means that nearing the end of the average line it might be made from 2 of the 21 games, thus it is not telling us much about the average Scandinavian Defense Mieses Kotroc Variation game.
  Therefore we will not analyse the end of this line but only up to around the 50th move.
  """
  st.image(im_sdm_u_a)
  """
  The graph seems to have a positive trend and not really go below the zero line. This seems to suggest that this is a opening that really favours the white player.
  """

if add_selectbox == 'Caro-Kann Defense':
  st.title("Openings: Caro-Kann Defense")
  """
  The Caro-Kann Defense is only in the top 5 of untitled players. Thus we are only going to look at the untitled players. 
  The Caro-Kann Defense is played 21 times by untitled players, and the longest Caro-Kann Defense game is 124 moves.
  
  Below you can see all the 21 games of the Caro-Kann Defense by the untitled players, and whilst I think this looks very pretty it isn't exactly readable. Therefore we continue with the average of all the games of the untitled players.
  """
  st.image(im_ckd_u)
  """
  As you might have noticed not all the games are as long as the other. This means that nearing the end of the average line it might be made from 2 of the 21 games, thus it is not telling us much about the average Caro-Kann Defense game.
  Therefore we will not analyse the end of this line but only up to around the 50th move.
  """  
  st.image(im_ckd_u_a)
  """
  The graph seems to have a negative trend and not really go above the zero line. This seems to suggest that this is a opening that really favours the black player.
  """
  
if add_selectbox == 'Horwitz Defense':
  st.title("Openings: Horwitz Defense")
  """
  The Horwitz Defense is only in the top 5 of untitled players. Thus we are only going to look at the untitled players. 
  The Horwitz Defense is played 14 times by untitled players, and the longest Horwitz Defense game is 127 moves.

  Below you can see all the 14 games of the Caro-Kann Defense by the untitled players, and whilst I think this looks very pretty it isn't exactly readable. This is why we continue with the average of all the games of the untitled players.
  """
  st.image(im_hd_u)
  """
  As you might have noticed not all the games are as long as the other. This means that nearing the end of the average line it might be made from 2 of the 14 games, thus it is not telling us much about the average Horwitz Defense game.
  Therefore we will not analyse the end of this line but only up to around the 50th move.
  """  
  st.image(im_hd_u_a)  
  """
  The graph of the average Horwitz Defense seems to stay around the zero line for the first 25 moves, and therefore does not really favour any particular player. 
  After the 25th move the line does go down into the negative, and thus it seems to favour the black player.
  """
  
