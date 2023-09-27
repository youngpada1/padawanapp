import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np


#BOM Tools Menu

#Submenu - Combine BOMs
class menu_page():
    def menu():
       with st.sidebar:
        selected = option_menu(
            menu_title='Flavia Ferreira',
            menu_icon='pages', default_index=0,
            options=['About Me', 'Portfolio', 'Salary'],
            #orientation='horizontal',
            styles={
        'container': {'padding': '5!important', 'background-color': '#000000'},
        'icon': {'color': 'orange', 'font-size': '10px'}, 
        'nav-link': {'font-size': '12px', 'text-align': 'left', 'margin':'0px', '--hover-color': '#eee'},
        'nav-link-selected': {'background-color': '#000000'},
    }   
    )
    menu()