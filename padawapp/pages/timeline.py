# Streamlit Timeline Component Example 
import streamlit as st
from streamlit_timeline import timeline
import pathlib as Path


# use full page width
st.set_page_config(page_title="Timeline Example", layout="wide")

# load data
career_timeline = '''<iframe src="https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=1xuY4upIooEeszZ_lCmeNx24eSFWe0rHe9ZdqH2xqVNk&font=Default&lang=en&initial_zoom=2&height=100%" width="100%" frameborder="0"></iframe>
                    '''
#with open('timeline.json', "r") as f:
   #data = f.read()

# render timeline
timeline(career_timeline, height=800)