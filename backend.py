import streamlit as st
import re


def initialize(session_states):
    for session_state in session_states:
        if session_state not in st.session_state:
            st.session_state[session_state]=0

def get_total():
    st.session_state['ideal_debt_to_income_ratio'] = (st.session_state.total_pemasukan * st.session_state.rasio_dir)/100

    st.session_state['total_pemasukan'] = (st.session_state.gaji
                                           + st.session_state.hasil_usaha
                                           + st.session_state.sampingan
                                           + st.session_state.uang_papa
                                           + st.session_state.deposito
                                           )

    st.session_state['total_subs'] = (st.session_state.subs_spotify
                                      + st.session_state.subs_netflix
                                      + st.session_state.subs_chatgpt
                                      + st.session_state.subs_others
                                      + st.session_state.gym
                                      )
    st.session_state['total_cicilan'] = (st.session_state.cicilan_rumah
                                         + st.session_state.cicilan_mobil
                                         + st.session_state.cicilan_motor
                                         + st.session_state.cicilan_cc
                                         )
    
    st.session_state['total_living_cost'] = (st.session_state.kos_apartemen
                                             + st.session_state.ipl
                                             + st.session_state.pln
                                             + st.session_state.internet_wifi
                                             + st.session_state.pdam
                                             + st.session_state.paket_data
                                             + st.session_state.kemanusiaan
                                             + st.session_state.bakti_ortu
                                             + st.session_state.uang_makan
                                             + st.session_state.transport 
                                             + st.session_state.asuransi
                                             + st.session_state.parkiran
                                             )
    st.session_state['total_pengeluaran'] = (st.session_state.total_subs
                                            + st.session_state.total_cicilan
                                            + st.session_state.total_living_cost
                                            )
    
