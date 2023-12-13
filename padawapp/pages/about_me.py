import streamlit as st
from streamlit_lottie import st_lottie
import os, base64
import pandas as pd
from pathlib import Path
from PIL import Image
import ruamel.yaml


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
    profile_pic = Path('/Users/youngpadawan/flaviapp/padawanapp/padawapp/images/Menu/Flavia - Profile pic.png') #Profile picture
    st.image(str(profile_pic), width=100)

# Download resume
with col2:
    resume = Path('/Users/youngpadawan/flaviapp/padawanapp/padawapp/images/Menu/Flavia Ferreira .pdf') #Resume
    #loading resume in PDF Format
    with open(resume, 'rb') as f:
        bytes_data = f.read()
# Adding download button
    st.download_button( 
       label='Download Resume',
       data=bytes_data,
       file_name='Flavia Ferreira | Resume',
       mime='application/pdf'    
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

# Page Intro    
st.write('I am a dedicated manufacturing engineer with 6+ years of experience in this field, supply chain, and leadership.My expertise lies in successfully delivering new products to the market, with a passion for optimising processes, conducting data analysis, and proficiently managing projects. I am recognised for my leadership style, leading by example and thriving within collaborative team environments. I take pride in consistently delivering excellence and viewing challenges as valuable learning opportunities. My career aspirations revolve around a commitment to continuous growth and a desire to explore new challenges in diverse fields, utilising my extensive experience while acquiring new skills. Within the audio industry, I have actively contributed to the community by providing technical support and serving as a business consultant to small brands.')
st.write(''' ''')

# Adding link to interviews (Media)
st.subheader('Other Links')


# Organizing links per column
col1, col2, col3= st.columns(3)

# Attack Mag
with col1:
    attackmag = 'https://raw.githubusercontent.com/youngpada1/padawanapp/c1fbfe2975240555c9dd6968ae8ada7962da0551/padawapp/images/Attack%20Mag.png'
    col1.markdown('5 Women In the Synthesizer Industry : Flavia Ferreira')
    st.markdown(f'''
                <a href='https://www.attackmagazine.com/features/interview/5-women-in-the-synthesizer-industry-flavia-ferreira-focusrite/'>
                <img src='{attackmag}' width=100% height=310px/>
                </a>''',
                unsafe_allow_html=True
                )

# Elektor Mag
with col2:
    elektor = 'https://raw.githubusercontent.com/youngpada1/padawanapp/c1fbfe2975240555c9dd6968ae8ada7962da0551/padawapp/images/Elektor%20Mag.png'
    col2.markdown('Elektor Magazine : Women in Tech')
    st.markdown(f'''
                <a href='https://www.elektormagazine.com/articles/women-in-tech'>
                <img src='{elektor}' width=100% height=310px/>
                </a>''',
                unsafe_allow_html=True
                )

# Instagram
with col3:
    instagram = 'https://raw.githubusercontent.com/youngpada1/padawanapp/c1fbfe2975240555c9dd6968ae8ada7962da0551/padawapp/images/Focusrite.jpeg'
    col3.markdown('Focusrite : Women in Engineering Day')
    st.markdown(f'''
                <a href='https://www.instagram.com/reel/Ct1yGcQoE91/'>
                <img src='{instagram}' width=100% height=100%/>
                </a>''',
                unsafe_allow_html=True
                )

st.write('''''') #Space between mag links & Youtube Videos

# Adding Youtube Videos
col1, col2, col3 = st.columns(3)
# Video 1 - Octatrack
with col1:
    col1.markdown('Soldering Repair Tricks for Beginners (Padawans)')
    octa_video = st.video('https://youtu.be/i4GFGXrruok')
# Video 2 - Atari
with col2:
    col2.markdown('Atari 2600 Mod')
    atari_video = st.video('https://www.youtube.com/watch?v=glaTan_GPs0')
# Video 3 - Octatrack
with col3:
    col3.markdown('Desoldering Tricks for Beginners')
    eurorack_video = st.video('https://www.youtube.com/watch?v=l1DEk35WWA8')



    
