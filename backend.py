import streamlit as st
import re


def initialize(session_states):
    for session_state in session_states:
        if session_state not in st.session_state:
            st.session_state[session_state]=0

def default_warning(text="Masukkan pemasukan dan pengeluaran kamu terlebih dahulu."):
    st.warning(text)

def get_total():
    st.session_state['target_rasio_utang_pemasukan'] = int(st.session_state.total_pemasukan * st.session_state.rasio_dir)/100
    st.session_state['target_rasio_tabungan_pemasukan'] = int(st.session_state.total_pemasukan * st.session_state.rasio_tabungan_pemasukan)/100
    st.session_state['target_dana_darurat'] = int(st.session_state.total_pemasukan*st.session_state.dana_darurat)

    st.session_state['total_pemasukan'] = int(st.session_state.gaji
                                           + st.session_state.hasil_usaha
                                           + st.session_state.sampingan
                                           + st.session_state.uang_papa
                                           + st.session_state.deposito
                                           )

    st.session_state['total_subs'] = int(st.session_state.subs_spotify
                                      + st.session_state.subs_netflix
                                      + st.session_state.subs_chatgpt
                                      + st.session_state.subs_others
                                      + st.session_state.gym
                                      )
    st.session_state['total_cicilan'] = int(st.session_state.cicilan_rumah
                                         + st.session_state.cicilan_mobil
                                         + st.session_state.cicilan_motor
                                         + st.session_state.cicilan_cc
                                         )
    
    st.session_state['total_living_cost'] = int(st.session_state.kos_apartemen
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
    st.session_state['total_saving'] = int(st.session_state.rekening_tangan
                                        + st.session_state.rekening_tabungan
                                        + st.session_state.rdpu
                                        + st.session_state.rdpt
                                        + st.session_state.rds
                                        + st.session_state.rd_obligasi
                                        )
    st.session_state['total_pengeluaran'] = int(st.session_state.total_subs
                                            + st.session_state.total_cicilan
                                            + st.session_state.total_living_cost
                                            )
    
    st.session_state['total_pemasukan_pengeluaran'] = int(st.session_state.total_pengeluaran
                                                       + st.session_state.total_pemasukan
                                                       )
    st.session_state['selisih_pemasukan_pengeluaran'] = (st.session_state.total_pemasukan - st.session_state.total_pengeluaran)
    st.session_state['val_pemasukan'] = st.session_state.total_pemasukan<=0
    st.session_state['val_pengeluaran'] = st.session_state.total_pengeluaran<=0
    
def cek_pemasukan_pengeluaran():
    if st.session_state.total_pemasukan==0 or st.session_state.total_pengeluaran==0:
        default_warning()
    else:
        if st.session_state.total_pemasukan>st.session_state.total_pengeluaran:
            st.success("Good job! Pemasukan kamu masih lebih tinggi daripada pengeluaran. Kamu masih bisa nabung {:,}lagi".format(st.session_state.selisih_pemasukan_pengeluaran))
        elif st.session_state.total_pemasukan<st.session_state.total_pengeluaran:
            st.error("Waduh! Pengeluaran kamu melebihi pemasukan. Berikut saran yang dapat kamu lakukan")
            st.write("* Kamu membutuhkan pemasukan tambahan untuk mengimbangi pengeluaran yang terlampau besar.")
            st.write("* Kamu dapat meminimalisir pengeluaran yang tidak perlu.")
        else:
            default_warning()
    return st.session_state.cek_pemasukan_pengeluaran

def cek_rasio_utang_pemasukan():         
    if st.session_state.total_pemasukan<=0:
        default_warning("Masukkan pemasukan dan cicilan kamu terlebih dahulu.") 
    elif st.session_state.total_cicilan>st.session_state.target_rasio_utang_pemasukan:
        st.error("Waduh! Cicilan kamu lebih besar dari maksimal rasio cicilan yang diijinkan {} atau setara dengan {}".format(st.session_state.rasio_dir
                                                                                                                              , st.session_state.target_rasio_utang_pemasukan
                                                                                                                              ))
    else:
        st.success("Good job! Cicilan kamu {:,} masih dalam target rasio yang direncanakan {}% atau maksimal cicilan sebesar {:,} dari total pemasukan {:,}.".format(
                                                                                                                                    st.session_state.total_cicilan
                                                                                                                                    , st.session_state.rasio_dir
                                                                                                                                    , st.session_state.target_rasio_utang_pemasukan
                                                                                                                                    , st.session_state.total_pemasukan))
def cek_rasio_tabungan_pemasukan():
    if st.session_state.total_saving==0 or st.session_state.total_pemasukan==0:
        default_warning("Masukkan jumlah pemasukan yang diterima dan tabungan yang ditabung setiap bulannya")
    else:    
        if st.session_state.total_saving >= st.session_state.target_rasio_tabungan_pemasukan:
            st.success("Good job. Uang yang kamu tabung setiap bulan {:,} sudah mencapai target rasio tabungan {}% terhadap pemasukan {:,}".format(st.session_state.total_saving
                                                                                                                                            ,st.session_state.rasio_tabungan_pemasukan
                                                                                                                                            ,st.session_state.total_pemasukan)) 
        else:
            st.error("Waduh. Target tabungan kamu belum tercapai karena kamu berencana menabung sebesar {:,} ({}% dari pemasukan) sementara".format(st.session_state.target_rasio_tabungan_pemasukan
                                                                                                                                                    , st.session_state.rasio_tabungan_pemasukan
                                                                                                                                                    , st.session_state.total_pemasukan))
        
    
