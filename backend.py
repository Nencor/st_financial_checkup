import streamlit as st
import re

def get_total(session_state):
    total = 0 
    for item in session_state:
        total+=session_state[item]
    return total