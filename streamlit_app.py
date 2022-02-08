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
add_selectbox = st.sidebar.selectbox('Choose an opening', ('General', 'Indian Defense', 'Modern Defense', "King's Indian Attack", 'Pirc Defense', 'Sicilian Defense Closed'))
im_sdc_vs = Image.open('/app/streamlit-example/Sicilian Defense Closed - untitled vs titled.png')
im_id_t = Image.open('/app/streamlit-example/Indian Defense - titled.png') 
im_id_t_a = Image.open('/app/streamlit-example/Indian Defense - titled - average.png')
im_id_u = 
im_id_u_a = 
im_id_vs = 
im_md_t = Image.open('/app/streamlit-example/Modern Defense - titled.png')
im_md_t_a = Image.open('/app/streamlit-example/Modern Defense - titled - average.png')
im_kia_t = Image.open("/app/streamlit-example/King's Indian Attack - titled.png")
im_kia_t_a = Image.open("/app/streamlit-example/King's Indian Attack - titled - average.png")
im_pd_t = Image.open('/app/streamlit-example/Pirc Defense - titled.png')
im_pd_t_a = Image.open('/app/streamlit-example/Pirc Defense - titled - average.png')

if add_selectbox == 'Sicilian Defense Closed':
  st.title('Openings: Sicilian Defense Closed')
  st.write('Sicilian Defense Closed')
  """
  We now look at the Sicilian Defense Closed. First we look at the titled players.
  """
  """
  Now we look at the untitled players.
  """
  """
  And now we shall compare the two types of players
  """
  st.image(im_sdc_vs)
  
if add_selectbox == 'Indian Defense':
  st.title('Openings: Indian Defense')
  """
  The Indian Defense is in the top 5 of untitled players and in the top 5 of titled players. We are first going to have a look at titled players, then at untitled players. 
  And then we end with a comparison of the 2 types of players.
  The Indian Defense is played 128 times by titled players, and the longest indian defense game is a 160 moves.
  """
  st.image(im_id_t)
  st.image(im_id_t_a)
  
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
  The King's Indian Attack is played 89 times by titled players, and the longest modern defense game is 205 moves.
  """
  st.image(im_kia_t)
  st.image(im_kia_t_a)

if add_selectbox == "Pirc Defense":
  st.title("Openings: Pirc Defense")
  """
  The Pirc Defense is only in the top 5 of titled players. Thus we are only going to look at the titled players. 
  The Pirc Defense is played 78 times by titled players, and the longest modern defense game is 197 moves.
  """
  st.image(im_pd_t)
  st.image(im_pd_t_a)
  
  
