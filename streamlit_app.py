import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image

"""
# Openings!

Edit `/streamlit_app.py` to customize this app to your heart's desire

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:

hi
"""
st.title('Openings')
st.sidebar.write('Menu')
add_selectbox = st.sidebar.selectbox('Choose an opening', ('indian defense', 'modern defense'))
image = Image.open('Sicilian Defense Closed - untitled vs titled.pgn')

st.image(image)
