import json
import streamlit as st
from streamlit_lottie import st_lottie


# Set layout page to wide
st.set_page_config(layout='wide')

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

    st.write('''___''')
    
# Experience
    if companies == 'Focusrite Audio Engineering ltd.':
        title = st.markdown('Production Engineer')
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
                             
Certification
‣ Served as the liaison between compliance teams and external partners (CSA, BLUETOOTH SIG, WIFI ALLIANCE, NEMKO, etc.), 
  facilitating the management and submission of regulatory documentation for product compliance in various global 
  territories (US, UK, Canada, Japan, etc.).
                                  
Supply Chain Management
‣ Proficiently managed End-of-Life (EOL) components and alternates, especially those with extended lead times, mitiga-
  ting potential production delays.
‣ Pioneered the implementation of a streamlined process in collaboration with the production engineering team, hardware 
  department, operations, and external vendors.
‣ Successfully transitioned from an Excel-based data tracker to the use of Youtrack, significantly reducing validation 
  and release times, leading to a remarkable 40% boost in productivity.
‣ Addressed a critical connector shortage in the Scarlett 3rd Gen series, responsible for a substantial portion of revenue 
  (around £3Million), ensuring a timely resolution that was pivotal for meeting financial year-end targets and supporting 
  new product introductions dependent on this component.
                                  
Project and Process Development
‣ Assumed responsibility for maintaining BOMs for products in mass production and New Product Introductions (NPIs). Collabo-
  rating with the engineering teams and communicating efficiently with the project management team and other stakeholders on 
  the project milestones and risks.
‣ Developed a highly efficient Python script that drastically reduced BOM processing time from 2 days to just 15 minutes.
‣ Streamlined workflows, ensuring same-day releases of BOMs, software, firmware, artworks, and more by effectively collabo-
  rating with engineering teams.
‣ Enhanced productivity through the efficient management and dissemination of manufacturing data to vendors via Engineering 
  Change Notifications (ECNs).
                             
Design Optimisation
‣ Focused on implementing DFx principles to optimise manufacturability and assembly processes.
‣ Contributed to enhancing efficiency and standardisation across all affiliated companies within the group, aligning with broader organisational goals
  and objectives.

PLM System Trainee
‣ Conducted process enhancement initiatives, both internally and across affiliated companies, during a period of organisational expansion.
‣ Introduced and optimised systems and processes for training new personnel across various departments, including Logistics, Service, 
  Operations, Hardware, and Mechanical Design.
‣ Developed software solutions for data processing, resulting in a remarkable 50% increase in productivity through procedural refinement 
  and workflow optimisation, utilising tools such as Youtrack, Confluence, and Jira, in collaboration with multiple disciplines, such as IT, 
  Power BI, and Data teams.
‣ Demonstrated proficiency in rectifying and enhancing the Arena PLM database through Python scripting and API utilisation.
‣ Facilitated seamless process adaptation and the integration of manufacturing data for new companies, contributing to organisational growth.

Production Engineering Trainee
‣ Conducted comprehensive inductions for new team members, ensuring a smooth assimilation into operational workflows.
‣ Reviewed and aligned Engineering Change Orders (ECOs), facilitating the integration of objectives and key results (OKRs) with organisational goals.
‣ Collaborated within a dynamic team to address areas requiring improvement, including material shortages and cost reduction measures.

Sustainability
‣ Led sustainable initiatives by researching various options and materials in collaboration with external contract manufacturers.
‣ Achieved an outstanding 80% reduction in plastic usage during a New Product Introduction (NPI) project.
‣ Notable achievements included the replacement of plastic seals with paper seals, substitution of plastic ties with
  paper wrapping, and the elimination of PE Foam in favor of a robust cardboard infrastructure capable of supporting
  product weight.
‣ Extended sustainable practices to other SKUs while adhering to budget constraints, optimizing product dimensions
  to reduce both shipping costs and carbon emissions.
                            
                            ''')
        
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
