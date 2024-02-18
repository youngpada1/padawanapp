from pathlib import Path
import streamlit as st
import json
import yaml


def certificates():
            # Adding introductory message
        st.title('Certificates')
        st.write(''' ''')
        # Reading the certificates.yaml file and parsing it into a dictionary object
        with open(Path(__file__).resolve().parent / 'certificates.yml' , 'r') as f:
                cert_info = yaml.safe_load(f)
                # Creating sidebar for user to select which certificate they want to view
                selected_certificate = st.sidebar.selectbox("Select Certificate", list)

certificates()