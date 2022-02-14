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
add_selectbox = st.sidebar.selectbox('Choose an opening', ('General', 'Indian Defense', 'Modern Defense', "King's Indian Attack", 'Sicilian Defense Closed', 'Pirc Defense', 'Scandinavian Defense Mieses Kotroc Variation', 'Caro-Kann Defense', 'Horwitz Defense', 'Top 5 - titled', 'Top 5 - untitled'))
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
  Text
  """
  
if add_selectbox == 'Top 5 - titled':
  st.title('Top 5 openings titled')
  """
  Text
  """  
  st.image(im_titled_a)
  
if add_selectbox == 'Top 5 - untitled':
  st.title('Top 5 openings untitled')
  """
  Text
  """  
  st.image(im_untitled_a)
  
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
  
if add_selctbox == 'Scandinavian Defense Mieses Kotroc Variation':
  st.title("Openings: Scandinavian Defense: Mieses-Kotroc Variation")
  """
  The Scandinavian Defense: Mieses-Kotroc Variation is only in the top 5 of untitled players. Thus we are only going to look at the untitled players. 
  The Scandinavian Defense: Mieses-Kotroc Variation is played - times by untitled players, and the longest Scandinavian Defense: Mieses-Kotroc Variation game is 144 moves.
  """
  st.image(im_sdm_u)
  st.image(im_sdm_u_a)

if add_selctbox == 'Caro-Kann Defense':
  st.title("Openings: Caro-Kann Defense")
  """
  The Caro-Kann Defense is only in the top 5 of untitled players. Thus we are only going to look at the untitled players. 
  The Caro-Kann Defense is played 21 times by untitled players, and the longest Caro-Kann Defense game is 124 moves.
  """
  st.image(im_ckd_u)
  st.image(im_ckd_u_a)
  
if add_selctbox == 'Horwitz Defense':
  st.title("Openings: Horwitz Defense")
  """
  The Horwitz Defense is only in the top 5 of untitled players. Thus we are only going to look at the untitled players. 
  The Horwitz Defense is played 14 times by untitled players, and the longest Horwitz Defense game is 127 moves.
  """
  st.image(im_hd_u)
  st.image(im_hd_u_a)  
  
