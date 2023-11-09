import streamlit as st
import re


def initialize(session_states):
    for session_state in session_states:
        if session_state not in st.session_state:
            st.session_state[session_state]=0

def default_warning(text="Masukkan pemasukan dan pengeluaran kamu terlebih dahulu."):
    st.warning(text)

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
    
    st.session_state['total_pemasukan_pengeluaran'] = (st.session_state.total_pengeluaran
                                                       + st.session_state.total_pemasukan
                                                       )
    st.session_state['val_pemasukan'] = st.session_state.total_pemasukan<=0
    st.session_state['val_pengeluaran'] = st.session_state.total_pengeluaran<=0
    
def cek_pemasukan_pengeluaran():
    if st.session_state.total_pemasukan>st.session_state.total_pengeluaran:
        st.success("Good job! Pemasukan kamu masih lebih tinggi daripada pengeluaran.")
    elif st.session_state.total_pemasukan<st.session_state.total_pengeluaran:
        st.error("Waduh! Pengeluaran kamu melebihi pemasukan. Berikut saran yang dapat kamu lakukan")
        st.write("* Kamu membutuhkan pemasukan tambahan untuk mengimbangi pengeluaran yang terlampau besar.")
        st.write("* Kamu dapat meminimalisir pengeluaran yang tidak perlu.")
    else:
        default_warning()
    return st.session_state.cek_pemasukan_pengeluaran

def cek_debt_income_ratio():        
    if st.session_state.total_pemasukan<=0:
        default_warning("Masukkan pemasukan dan cicilan kamu terlebih dahulu") 
    elif st.session_state.total_cicilan>st.session_state.ideal_debt_to_income_ratio:
        st.error("Waduh! Cicilan kamu lebih besar dari maksimal rasio cicilan yang diijinkan {} atau setara dengan {}".format(st.session_state.rasio_dir
                                                                                                                              , st.session_state.ideal_debt_to_income_ratio
                                                                                                                              ))
    else:
        st.success("Good job! Cicilan kamu {:,} masih dalam target rasio yang direncanakan {}% atau maksimal cicilan sebesar {:,} dari total pemasukan {:,}.".format(
                                                                                                                                    st.session_state.total_cicilan
                                                                                                                                    , st.session_state.rasio_dir
                                                                                                                                    , int(st.session_state.ideal_debt_to_income_ratio)
                                                                                                                                    , int(st.session_state.total_pemasukan)))
