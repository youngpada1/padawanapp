import streamlit as st
from streamlit_timeline import st_timeline

# Set layout page to wide
st.set_page_config(layout='wide')

# Adding Selectbox
def career():
    st.title('Professional Experience')
    companies = st.selectbox(
        'Select a company',
        ('Focusrite','MOD Devices', 'Patch Point', 'Konstruktiv GmbH', 'Koma Elektronik GmbH', 'Winter Modular' 'Befaco' )
)
    st.write('''___''')

# Timeline 
    years = [
       {'Focusrite': 1, 'content': 'Present', 'start': '2021-11-01'},
       {'MOD Devices': 2, 'content': '2021-07-01', 'start': '2020-07-01'},
       {'Patch Point': 3, 'content': '2020-04-01', 'start': '2018-09-01'},
       {'Konstruktiv GmbH': 4, 'content': '2022-10-16', 'start': '2022-10-16'},
       {'Koma Elektronik GmbH': 5, 'content': '2022-10-25', 'start': '2022-10-25'},
       {'Winter Modular': 6, 'content': '2022-10-27', 'start': '2022-10-27'},
       {'Befaco': 7, 'content': '2022-10-27', 'start': '2022-10-27'}
]
    timeline = st_timeline(years, groups=[], options={}, height='150px')
   
# Experience
    if companies == 'Focusrite':
        title = st.markdown('Production Engineer - Focusrite Audio LTD')
        experience = st.text('''
                                  PLM System Trainee
- Identified process enhancement opportunities during organizational expansion.
- Results after the first year:
- Introduced systems and processes to train new personnel across various departments (Logistics, Service, Operations, Hardware, Mechanical Design).
- Software development for processing data resulted in a 50% increase in productivity.
- Improved existing settings and rectified the Arena PLM database using Python scripting and API utilization.
- Facilitated seamless process adaptation and integration of manufacturing data for new companies.
                             
Production Engineering Trainee
- Facilitated integration of new team members into operational workflows.
- Conducted comprehensive inductions, reviewed Engineering Change Orders (ECOs), and supported alignment of objectives and key results (OKRs).
- Focused on addressing areas requiring improvement, such as material shortages and cost reduction measures.
                                  
Sustainability
- Achieved an 80% reduction in plastic usage in the New Product Introduction (NPI) project.
- Replaced plastic seals with paper seals, plastic ties with paper wrapping, and eliminated PE Foam.
- Extended sustainable practices to other SKUs while adhering to budget constraints.
- Optimized product dimensions, reducing both shipping costs and carbon emissions.
                                  
Bill of Materials (BOM) Management
- Overseeing maintenance of BOM for mass production and NPIs.
- Developed a Python script that reduced processing time from 2 days to a mere 15 minutes.
                             
Component Engineering
- Managed End-of-Life (EOL) components and alternates to mitigate potential production delays.
- Transitioned from an Excel-based data tracker to Youtrack, streamlining communication and reducing validation and release times.
- Increased productivity by an impressive 40%.
- Successfully managed a connector shortage impacting 71% of revenue.

Cost Management
- Tracked NPI costs, reported FOB updates, and managed material cost fluctuations.
- Negotiated contract pricing with distributors, resulting in substantial savings of approximately $55,000 per year (only in three components) used in multiple SKUs.
- Proactively identified and resolved production-related challenges, proposing pragmatic solutions.

Design Optimization
- Focused on implementing Design for Manufacturing (DFM) and Design for Assembly (DFA) principles to optimize manufacturability and assembly processes, enhancing efficiency and standardization.''')
        
    
    st.write()

career()
