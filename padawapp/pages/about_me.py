import streamlit as st
import os, base64
import pandas as pd
from pathlib import Path
from PIL import Image

# Set layout page to wide
st.set_page_config(layout='wide')

# Adding introductory message
st.title('Flavia Ferreira')
st.markdown('''This is a web app that allows you to see my professional experience''')
st.write('''___''')

# Adding columns
col1, col2, col3, col4 = st.columns(4)
# Profile photo section
with col1: 
    profile_pic = Path('/Users/youngpadawan/flaviapp/padawanapp/padawapp/images/Flavia - Profile pic.png') #Profile picture
    st.image(str(profile_pic), width=100)

# Download resume
    resume = Path('/Users/youngpadawan/flaviapp/padawanapp/padawapp/images/Flavia Ferreira - Resume (IT Management).pdf') #Resume
    #loading resume in PDF Format
    with open(resume, 'rb') as f:
        bytes_data = f.read()
# Adding download button
    st.download_button( 
       label='Download my resume',
       data=bytes_data,
       file_name='Flavia Ferreira | Resume',
       mime='application/pdf'
)
# Link to Github
with col3:
    github = Path(__file__) / '../images/github.png' #GitHub profile
    st.markdown('''
    <a href='https://github.com/youngpada1'>
        <img src='{github}'/>
    </a>''',
    unsafe_allow_html=True
)

# Link to LinkedIn
with col4:
    linkedin = Path('/Users/youngpadawan/flaviapp/padawanapp/padawapp/images/linkedin.png') #LinkedIn profile
    st.markdown('''
    <a href='https://www.linkedin.com/in/flaviaferr/'>
        <img src={linkedin}/>
    </a>''',
    unsafe_allow_html=True
)

    
st.write('I am a dedicated manufacturing engineer with over 6 years of experience in this field, supply chain, and leadership. Delivering new products to the market. I am passionate about optimising processes, data analysis and project management. Known for leading by example and thriving in collaborative team environments, I take pride in delivering excellence and view challenges as valuable learning opportunities. My career aspirations revolve around continuous growth and seeking new challenges in diverse fields where I can leverage my extensive experience while acquiring new skills. Within the audio industry, I have actively contributed to the community by providing technical support and serving as a business consultant to small brands.')

