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

hi
"""
st.sidebar.write('Menu')
add_selectbox = st.sidebar.selectbox('Choose an opening', ('General', 'indian defense', 'modern defense', 'Sicilian Defense Closed'))
im_sdc_vs = Image.open('/app/streamlit-example/Sicilian Defense Closed - untitled vs titled.png')

if add_selectbox == 'Sicilian Defense Closed':
  st.title('Openings: Sicilian Defense Closed')
  st.write('Sicilian Defense Closed')
  """
  hi this is kes
  """
  st.image(im_sdc_vs)
