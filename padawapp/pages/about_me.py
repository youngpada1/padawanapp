import pandas as pd
import glob
import streamlit as st
from PIL import Image

# Set layout page to wide
st.set_page_config(layout='wide')

# Adding introductory message
st.title('Flavia Ferreira')
st.markdown('''This is a web app that allows you to see my professional experience''')
st.write('''___''')

# Adding columns
col1, col2, col3 = st.columns(3)
with col1: #first section - profile photo
    photo_loc = '/Users/youngpadawan/flaviapp/padawanapp/padawapp/images/Flavia - Profile pic.png'
    st.image(photo_loc, width=100)

with col2:
    resume = '/Users/youngpadawan/flaviapp/padawanapp/padawapp/images/Flavia Ferreira - Resume (IT Management).pdf'
    #loading resume in PDF Format
    with open(resume, 'rb') as f:
        bytes_data = f.read()
#adding download button
st.download_button( 
    label='Download my resume',
    data=bytes_data,
    file_name='Flavia Ferreira | Resume',
    mime='application/pdf'
)

#link to LinkedIn & Github
with col3:
    st.markdown('''
            Linkedin (https://www.linkedin.com/in/flaviaferr/)
            
            ''')
    st.markdown('''
            Github (https://github.com/youngpada1)
            
            ''')
    
    

st.write('I am a dedicated manufacturing engineer with over 6 years of experience in this field, supply chain, and leadership.  Delivering new products to the market. I am passionate about optimising processes, data analysis and project management. Known for leading by example and thriving in collaborative team environments, I take pride in delivering excellence and view challenges as valuable learning opportunities. My career aspirations revolve around continuous growth and seeking new challenges in diverse fields where I can leverage my extensive experience while acquiring new skills. Within the audio industry, I have actively contributed to the community by providing technical support and serving as a business consultant to small brands.')


