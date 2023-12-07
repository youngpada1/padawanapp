import json
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie


### Set layout page to wide
st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

### Creating columns to add animation to column3
col1, col2, col3, col4 = st.columns(4)
with col1: # Page title
    st.title('Professional Experience')
with col2: # There's nothing here, bleh!
    st.write('''''')
with col3: # There's nothing here, bleh!
    st.write('''''')
with col4: # Load Lottie animation
    with open ('/Users/youngpadawan/flaviapp/padawanapp/padawapp/pages/Wrench.json', 'r') as f:
        data = json.load(f)
        st_lottie(data,
          speed=1,
          reverse=False,
          loop=True,
          width='200px',
          height='150px'
          )


### Adding Selectbox
def career():
    companies = st.selectbox(
        'Select a company',
        ('Focusrite Audio Engineering ltd.','MOD Devices', 'Patch Point', 'Konstruktiv GmbH', 'Koma Elektronik GmbH', 'Winter Modular', 'Befaco' )
)
    st.write(''' ''')
    
### Experience
    if companies == 'Focusrite Audio Engineering ltd.':
        ### Creating columns to add photos
        col1, col2, col3, col4 = st.columns (4)

        with col1: # Novation Impulse
            impulse = 'https://raw.githubusercontent.com/youngpada1/padawanapp/b5ac96c010b37c0d7054a1dc1c7db8c3f679bd05/padawapp/images/novation-impulse.jpg'
            st.markdown(f'''
                        <img src='{impulse}' width=84% />
                        </a>''',
                        unsafe_allow_html=True
                        )

        with col2: # Scarlett 3rd Gen
            scarlett3gen = 'https://raw.githubusercontent.com/youngpada1/padawanapp/9e9e0a43e4eb2534288a1dc82709d5b75c1969af/padawapp/images/s3g.png'
            st.markdown(f'''
                        <img src='{scarlett3gen}' width=70% />
                        </a>''',
                        unsafe_allow_html=True
                        )
        with col3: # Circuit Rythm & Tracks
            circuit = 'https://raw.githubusercontent.com/youngpada1/padawanapp/fd98b177760a2b9fe817b1f30f350bf75298abbc/padawapp/images/circuit%20-%20rythmandtracks.jpeg'
            st.markdown(f'''
                        <img src='{circuit}' width=93% />
                        </a>''',
                        unsafe_allow_html=True
                        )
        with col4: # Scarlett 4th Gen
            scarlett4gen = 'https://raw.githubusercontent.com/youngpada1/padawanapp/9e9e0a43e4eb2534288a1dc82709d5b75c1969af/padawapp/images/s4g.png'
            st.markdown(f'''
                        <img src='{scarlett4gen}' width=95% layout=centered/>
                        </a>''',
                        unsafe_allow_html=True
                        )
        st.write(''' ''')

        ### Creating categories - cost management, supply chain, etc...
        class categories:
            def nav_bar():
                select = option_menu(
                    menu_title=None,
                    menu_icon=None, default_index=0,
                    options=['Cost Management', 'Certification','Supply Chain Management',
                                  'Project and Process Development', 'Design Optimisation',
                                   'PLM System Trainee', 'Production Engineering Trainee',
                                   'Sustainability'],
                    orientation='horizontal',
                    styles={
                'container': {'padding': '5!important', 'background-color': '#000000'},
                'icon': {'color': 'orange', 'font-size': '10px'}, 
                'nav-link': {'font-size': '10px', 'text-align': 'center', 'margin':'0px', '--hover-color': '#eee'},
                'nav-link-selected': {'background-color': '#000000'},
                }
                )
                ### Cost Management - Information
                if select == 'Cost Management':
                    cost_management = st.expander('''''', expanded=True)
                    cost_management.markdown('''

In my role as a Production Engineer, I successfully managed NPI cost tracking, consistently providing accurate FOB updates for stakeholders. 
Managed material cost fluctuations, particularly for integrated circuits and inductors, employing data-driven strategies and tools like, python scripts,
Power Query Editor and Power BI. As part of my day-to day, I collaborated closely with the sourcing manager to negotiate favorable contract pricing with distributors, 
resulting in significant annual savings of components used across multiple SKUs. Demonstrating proactive problem-solving by identifying and resolving production-related challenges, 
whilst maintaining clear communication with stakeholders to prevent future issues, proposing practical and effective solutions.
''')
                ### Certification - Information
                elif select == 'Certification':
                    certification = st.expander('''''', expanded=True)
                    certification.markdown('''
As part of the NPI management and data maintenance of products in mass production, I served as the liaison between compliance teams and external partners (CSA, BLUETOOTH SIG, WIFI ALLIANCE, NEMKO, etc.), 
facilitating the management and submission of regulatory documentation for product compliance in various global territories (US, UK, Canada, Japan, etc.).
''')
                ### Supply Chain Management - Information
                elif select == 'Supply Chain Management':
                    supply_chain = st.expander('''''', expanded=True)
                    supply_chain.markdown('''
Daily operations included managing End-of-Life (EOL) components and alternates, strategically addressing those with extended lead times to prevent potential production delays. 
In order to streamline this process, I collaborated with the production engineering team, hardware department, operations, and external vendors to implement a new way to process and report data. 
Successfully transitioned from an Excel-based data tracker to Youtrack, significantly reducing validation and release times, resulting in a remarkable 40% boost in productivity. 
One of the main challenges I had to face this year, was to address a critical connector shortage in the Scarlett 3rd Gen series, responsible for a substantial portion of revenue (around £3 million), 
ensuring a timely resolution crucial for meeting financial year-end targets and supporting new product introductions dependent on this component.
''')
                elif select == 'Project and Process Development':
                    project_and_process = st.expander('''''', expanded=True)
                    project_and_process.markdown('''
One of my main objectives was to streamline workflows to ensure the smooth transition from raw data into processed data that could be imported or updated into the database. 
To reduce bottlenecks during this process, I developed a number of highly efficient Python scripts, reducing BOM processing time from 2 days to just 15 minutes. This streamlined workflows, enabled same-day releases of BOMs, software, 
firmware, artworks, and more through effective collaboration with engineering teams. As responsible for maintaining BOMs for products in mass production and New Product Introductions (NPIs), I collaborated closely with engineering teams ensuring effective 
communication with the project management team and other stakeholders on project milestones and risks.
As a result of this initiative, we enhanced productivity by efficiently managing and disseminating manufacturing data to vendors via Engineering Change Notifications (ECNs).

''')
                elif select == 'Design Optimisation':
                    design_optimization = st.expander('''''', expanded=True)
                    design_optimization.markdown('''
To optimise manufacturability and assembly processes in NPIs - I focused on implementing DFx principles, such us Design for Assembly and Design For Manufacturing. Learning from previous designs and with the support of the contract manufacturer's feedback. I contributed to enhance efficiency and standardisation across all affiliated companies within the group, aligning
with broader organisational goals and objectives.

''')
                elif select == 'PLM System Trainee':
                    plm_system_trainee = st.expander('''''', expanded=True)
                    plm_system_trainee.markdown('''
I became part of the Focusrite Group during a phase of organizational expansion, allowing me the opportunity to proactively implement new processes. In response, I spearheaded process enhancement initiatives both within the company and across affiliated entities.
My responsibilities extended to introducing and optimizing systems and processes for training new personnel in various departments, including Logistics, Service, Operations, Hardware, and Mechanical Design.
I also played a key role in developing software solutions for data processing, resulting in an impressive 50% increase in productivity. This achievement was realized through procedural refinement and workflow optimization, leveraging tools such as Youtrack, Confluence, and Jira. I collaborated with diverse disciplines, including IT, Power BI, and Data teams.
My proficiency extended to rectifying and enhancing the Arena PLM database through Python scripting and API utilization, showcasing my ability to navigate and improve complex systems.
Overall, I contributed to the seamless adaptation of processes and integration of manufacturing data for new companies, thereby playing a crucial role in the organizational growth of the Focusrite Group.
''')
                elif select == 'Production Engineering Trainee':
                    production_engineering_trainee = st.expander('''''', expanded=True)
                    production_engineering_trainee.markdown('''
I took the initiative to lead comprehensive inductions for new team members, ensuring a seamless assimilation into operational workflows. Additionally, I played a pivotal role in reviewing and aligning Engineering Change Orders (ECOs), 
integrating objectives and key results (OKRs) with our organizational goals. Within our dynamic team, I collaborated on addressing areas for improvement, such as material shortages and cost reduction measures.In leveraging my prior 
experience leading teams, I identified a valuable opportunity to contribute my insights. At ADAM Audio, where I served as the first and only production engineer in the engineering team, I worked closely with management and other engineering 
disciplines. Together, we crafted processes that incorporated production engineering tasks, tailored to seamlessly fit the existing flows and needs of the team. This experience allowed me to bring a unique perspective to our collaborative efforts.
''')
                elif select == 'Sustainability':
                    sustainability = st.expander('''''', expanded=True)
                    sustainability.markdown('''
I took the lead in driving sustainable initiatives, collaborating closely with external contract manufacturers to explore various options and materials. One notable accomplishment was the impressive 80% reduction in plastic usage achieved during a New Product Introduction (NPI) project.
In pursuit of sustainability goals, key achievements included replacing plastic seals with environmentally friendly paper seals, substituting plastic ties with paper wrapping, and eliminating PE Foam in favor of a robust cardboard infrastructure capable of supporting product weight.
These environmentally conscious practices were extended to other SKUs, demonstrating a commitment to sustainability while carefully adhering to budget constraints. As part of this effort, we optimized product dimensions to not only reduce shipping costs but also minimize carbon emissions, aligning with our commitment to a greener future.
''')

            nav_bar()
                
        

career()