import streamlit as st
import os, base64
import pandas as pd
from pathlib import Path
from PIL import Image

# Set layout page to wide
st.set_page_config(layout='wide')

# Adding introductory message
st.title('Flavia Ferreira')
st.markdown('''Welcome to the Flaviapp. Who am I? Let's find out!''')
st.write('''___''')

# Adding columns
col1, col2, col3, col4 = st.columns(4)
# Profile photo section
with col1: 
    profile_pic = Path('/Users/youngpadawan/flaviapp/padawanapp/padawapp/images/Flavia - Profile pic.png') #Profile picture
    st.image(str(profile_pic), width=100)

# Download resume
with col2:
    resume = Path('/Users/youngpadawan/flaviapp/padawanapp/padawapp/images/Flavia Ferreira - Resume (IT Management).pdf') #Resume
    #loading resume in PDF Format
    with open(resume, 'rb') as f:
        bytes_data = f.read()
# Adding download button
    st.download_button( 
       label='Download Resume',
       data=bytes_data,
       file_name='Flavia Ferreira | Resume',
       mime='application/pdf',
     
)
# Link to Github
with col3:
    github = 'https://raw.githubusercontent.com/youngpada1/padawanapp/a98515a589676598e3ff4fa18a3c24d6f23971b8/padawapp/images/github.png'
    st.markdown(f'''
    <a href='https://github.com/youngpada1'>
        <img src='{github}' width='20px'/>
    </a>''',
    unsafe_allow_html=True
)

# Link to LinkedIn
with col4:
    linkedin = 'https://raw.githubusercontent.com/youngpada1/padawanapp/a98515a589676598e3ff4fa18a3c24d6f23971b8/padawapp/images/linkedin.png' #LinkedIn profile
    st.markdown(f'''
    <a href='https://www.linkedin.com/in/flaviaferr/'>
        <img src='{linkedin}' width='20px'/>
    </a>''',
    unsafe_allow_html=True
)

    
st.write('I am a dedicated manufacturing engineer with 6+ years of experience in this field, supply chain, and leadership.My expertise lies in successfully delivering new products to the market, with a passion for optimising processes, conducting data analysis, and proficiently managing projects. I am recognised for my leadership style, leading by example and thriving within collaborative team environments. I take pride in consistently delivering excellence and viewing challenges as valuable learning opportunities. My career aspirations revolve around a commitment to continuous growth and a desire to explore new challenges in diverse fields, utilising my extensive experience while acquiring new skills. Within the audio industry, I have actively contributed to the community by providing technical support and serving as a business consultant to small brands.')

