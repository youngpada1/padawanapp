import json
import streamlit as st
from streamlit_lottie import st_lottie


# Set layout page to wide
st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

# Creating columns to add animation to column3
col1, col2, col3 = st.columns(3)
with col1: # Page title
    st.title('Professional Experience')
with col2: # There's nothing here, bleh!
    st.write('''''')
with col3: # Load Lottie animation
    with open ('/Users/youngpadawan/flaviapp/padawanapp/padawapp/pages/Wrench.json', 'r') as f:
        data = json.load(f)
        st_lottie(data,
          speed=1,
          reverse=False,
          loop=True,
          width='200px',
          height='150px'
          )


# Adding Selectbox
def career():
    companies = st.selectbox(
        'Select a company',
        ('Focusrite Audio Engineering ltd.','MOD Devices', 'Patch Point', 'Konstruktiv GmbH', 'Koma Elektronik GmbH', 'Winter Modular', 'Befaco' )
)
    st.write(''' ''')
    
# Experience
    if companies == 'Focusrite Audio Engineering ltd.':
        ## Creating columns to add photos
        col1, col2, col3, col4 = st.columns (4)
        with col1: # Scarlett 3rd Gen
            scarlett3gen = 'https://raw.githubusercontent.com/youngpada1/padawanapp/9e9e0a43e4eb2534288a1dc82709d5b75c1969af/padawapp/images/s3g.png'
            st.markdown(f'''
                        <img src='{scarlett3gen}' width=50% />
                        </a>''',
                        unsafe_allow_html=True
                        )
        with col2: # Scarlett 4th Gen
            scarlett4gen = 'https://raw.githubusercontent.com/youngpada1/padawanapp/9e9e0a43e4eb2534288a1dc82709d5b75c1969af/padawapp/images/s4g.png'
            st.markdown(f'''
                        <img src='{scarlett4gen}' width=70% />
                        </a>''',
                        unsafe_allow_html=True
                        )
        title = st.markdown('Production Engineer (High Wycombe) - November 2021 - Present')
        options = st.multiselect('',
                                 ['Cost Management', 'Certification','Supply Chain Management',
                                  'Project and Process Development', 'Design Optimisation',
                                   'PLM System Trainee', 'Production Engineering Trainee',
                                   'Sustainability' ])
        focusrite = st.text(''' 
                                  Cost Management
‣ Successfully managed NPI cost tracking, consistently delivering accurate FOB updates to stakeholders.
‣ Effectively managed material cost fluctuations, including integrated circuits (ICs) and inductors, employing 
  data-driven strategies.
‣ Collaborated closely with the sourcing manager to negotiate and secure favorable contract pricing with distributors,
  resulting in substantial 
  annual savings of approximately $55,000 across three critical components used in multiple SKUs.
‣ Demonstrated proactive problem-solving by identifying and resolving production-related challenges, employing clear 
  communication with stakeholders to prevent future issues, and proposing practical and effective solutions.
                             
''')
        

        


career()
