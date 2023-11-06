import streamlit as st
import re

def initialize_totalan(state_names,default_value=0):
    for state_name in state_names:
        if state_name not in st.session_state:
            st.session_state.state_name = default_value

def callback_input():
    st.session_state['total_aset_kas']= st.session_state.aset_lancar__kas_di_tangan 
    + st.session_state.aset_lancar__tabungan
    + st.session_state.aset_lancar__rdpu
    + st.session_state.aset_lancar__deposito
        