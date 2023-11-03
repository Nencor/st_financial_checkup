import streamlit as st
import re

def get_total_aset_kas():
    value = 0
    for item in st.session_state.data['Aset']['kategori']['aset_lancar']['Aset Kas']:
        value += st.session_state.data['Aset']['kategori']['aset_lancar']['Aset Kas'][item]
    return value