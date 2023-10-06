import streamlit as st

# Set layout page to wide
st.set_page_config(layout='wide')

# Adding Selectbox
def career():
    st.title('Professional Experience')
    companies = st.selectbox(
        'Select a company',
        ('Focusrite','MOD Devices', 'Patch Point', 'Konstruktiv GmbH', 'Koma Elektronik GmbH', 'Winter Modular', 'Befaco' )
)
    st.write('''___''')

# Experience
    if companies == 'Focusrite':
        title = st.markdown('Production Engineer')
        focusrite = st.text('''
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
        
    elif companies == 'MOD Devices':
        title = st.markdown('Production Manager')
        mod_devices = st.text('''
- Strategically planned, coordinated, and meticulously documented production and quality control processes across multiple departments.
- Demonstrated expertise in diagnosing and resolving technical issues, contributing to efficient problem-solving and minimizing production downtime.
- Proficiently debugged Linux-based hardware systems, diligently documenting issues and ensuring seamless releases to the factories.
- Executed the construction and rigorous validation of prototypes vital for hardware development, specifically New Product Introductions (NPI).
- Proactively identified and communicated potential risks to stakeholders, fostering timely mitigation to prevent production delays and issues, all while championing a culture of continuous process improvement.
- Collaborated effectively with external service providers to facilitate the seamless transition of products into Mass Production.
- Managed logistics operations encompassing production, fulfillment, and comprehensive customer support to ensure operational excellence.
''')
    
    elif companies == 'Patch Point':
        title = st.markdown('Production Manager')
        patch_point = st.text('''
During my time at Patch Point, I had the privilege of contributing to several high-profile projects. Among these accomplishments, I take particular pride in overseeing the construction of all Serge systems and the TTSH for the University of New York (US).My responsibilities at Patch Point encompassed a diverse range of critical tasks, demonstrating my comprehensive skill set and commitment to excellence:
Methodically documented and established streamlined processes to ensure operational efficiency.
- Led a team of personnel, providing supervision and comprehensive training to ensure optimal performance.
- Applied technical expertise in soldering, assembly, testing, and precision calibration of intricate instruments.
- Managed the procurement of components and production materials, ensuring seamless workflow.
- Leveraged problem-solving skills to troubleshoot hardware issues and facilitate swift resolutions.
- Delivered the implementation of an inventory management system, optimising production line organisation for enhanced productivity.

''')
        
    elif companies == 'Koma Elektronik GmbH':
        title = st.markdown('Manufacturing Technican')
        koma = st.text('''
- Proficiently performed comprehensive product assembly of boutique audio equipment.
- Demonstrated expertise in diagnosing and resolving technical issues.
- Conducted rigorous quality control assessments and meticulous testing procedures. 
''')
    
    elif companies == 'Konstruktiv GmbH':
        title = st.markdown('Testing Engineer')
        konstruktiv = st.text('''

- Assembled prototypes for external companies, ensuring precision and attention to detail in the manufacturing process.
- Conducted manufacturability assessments to optimize product design and production efficiency, resulting in cost savings and improved product quality.
- Proficiently performed comprehensive product assembly of boutique audio equipment, meeting or exceeding quality standards and production timelines.
- Demonstrated expertise in diagnosing and resolving technical issues, contributing to efficient problem-solving and minimizing production downtime.
- Conducted rigorous quality control assessments to maintain high product standards and customer satisfaction.
- Implemented meticulous testing procedures to validate product performance and functionality, ensuring reliability and adherence to specifications

''')
        
    elif companies == 'Winter Modular':
        title = st.markdown('Manufacturing Technician')
        winter_modular = st.text('''
- Played a pivotal role in the successful delivery of 250 units for the first release within a tight two-week timeframe. This involved active participation in product assembly, quality assurance, and packaging.
- Demonstrated exceptional problem-solving skills while working tirelessly to overcome production challenges, such as the faceplate not fitting well with the PCB, despite the absence of documentation.
- Proficiently performed comprehensive product assembly, ensuring the highest standards of quality and craftsmanship.
- Showcased expertise in diagnosing and effectively resolving technical issues, contributing to the seamless production process.
- Conducted rigorous quality control assessments and implemented meticulous testing procedures, upholding stringent quality standards throughout the production cycle.
                                 ''')
    
    elif companies == 'Befaco':
        title = st.markdown('Manufacturing Technican')
        befaco = st.text('''
- Started my career in the audio tech industry as a novice and quickly gained proficiency in comprehensive product assembly.
- Demonstrated expertise in diagnosing and effectively resolving technical issues, contributing to smooth production processes.
- Conducted thorough quality control assessments and implemented meticulous testing procedures, upholding the company's commitment to product excellence.

''')

    st.write()

career()
