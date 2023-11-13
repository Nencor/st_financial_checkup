import streamlit as st
import re


def initialize(session_states):
    for session_state in session_states:
        if session_state not in st.session_state:
            st.session_state[session_state]=0

def default_warning(text="Masukkan pemasukan dan pengeluaran kamu terlebih dahulu."):
    st.warning(text)

def get_total():    
    # st.session_state['target_dana_darurat'] = int(st.session_state.total_pemasukan*st.session_state.dana_darurat)

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
                                      + st.session_state.mentoring
                                      )
    st.session_state['total_cicilan'] = int(st.session_state.cicilan_kpr
                                            +st.session_state.cicilan_kpa
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
                                            + st.session_state.total_saving
                                            )
    
    st.session_state['total_pemasukan_pengeluaran'] = int(st.session_state.total_pengeluaran
                                                       + st.session_state.total_pemasukan
                                                       )
    st.session_state['total_aset_kas_lancar'] = int(st.session_state.aset_lancar__kas_di_tangan
                                             + st.session_state.aset_lancar__tabungan
                                             + st.session_state.aset_lancar__deposito
                                             + st.session_state.aset_lancar__rdpu
                                             )
    st.session_state['total_aset_investasi_lancar'] = int(st.session_state.aijp__emas
                                                          +st.session_state.aijp__rdpt
                                                          +st.session_state.aijp__rdc
                                                          +st.session_state.aijp__rds
                                                          +st.session_state.aijp__obligasi
                                                          +st.session_state.aijp__saham
                                                          +st.session_state.aijp__nilai_tunai_asuransi
                                                          +st.session_state.aijp__lain_lain
                                                          )
    st.session_state['total_aset_konsumsi_tidak_lancar'] = int(st.session_state.aktl__rumah
                                                               +st.session_state.aktl__perhiasan
                                                               +st.session_state.aktl__mobil
                                                               +st.session_state.aktl__motor
                                                               )
    st.session_state['total_aset_investasi_tidak_lancar'] = int(st.session_state.aitl__bpjsnaker
                                                                + st.session_state.aitl__bpjsjht
                                                                + st.session_state.aitl__dplk
                                                                + st.session_state.aitl__koleksi
                                                                + st.session_state.aitl__properti
                                                                + st.session_state.aitl__tanah
                                                                + st.session_state.aitl__nilai_bersih_usaha
                                                                )

    st.session_state['total_aset_lancar'] = int(st.session_state.total_aset_kas_lancar
                                                +st.session_state.total_aset_investasi_lancar
                                                )
    st.session_state['total_aset_tidak_lancar'] = int(st.session_state.total_aset_konsumsi_tidak_lancar
                                                      + st.session_state.total_aset_investasi_tidak_lancar
                                                      )
    
    st.session_state['total_utang_jangka_pendek'] = int(st.session_state.ujpe__cc
                                                        +st.session_state.ujpe__personal_loan
                                                        +st.session_state.ujpe__mobil
                                                        +st.session_state.ujpe__motor
                                                        +st.session_state.ujpe__kta
                                                        +st.session_state.ujpe__lainnya
                                                        )
    st.session_state['total_utang_jangka_panjang'] = int(st.session_state.ujpa__kpr
                                                         +st.session_state.ujpa__kpa
                                                         +st.session_state.ujpa__lainnya
                                                     )
    st.session_state['total_aset'] = int(st.session_state.total_aset_lancar
                                    + st.session_state.total_aset_tidak_lancar
                                    )
    st.session_state['total_utang_outstanding']=int(st.session_state.total_utang_jangka_pendek + st.session_state.total_utang_jangka_panjang)
    
    st.session_state['selisih_pemasukan_pengeluaran'] = (st.session_state.total_pemasukan - st.session_state.total_pengeluaran)
    st.session_state['target_rasio_utang_pemasukan'] = int((st.session_state.total_pemasukan * st.session_state.rasio_dir)/100)
    st.session_state['target_rasio_tabungan_pemasukan'] = int(st.session_state.total_pemasukan * st.session_state.rasio_tabungan_pemasukan/100)
    st.session_state['target_rasio_utang_outstanding_aset'] = int(st.session_state.total_aset*st.session_state.rasio_utang_aset/100)
    st.session_state['rasio_premi_asuransi_pemasukan'] = int((st.session_state.asuransi/st.session_state.total_pemasukan)*100)
    st.session_state['target_premi_asuransi'] = int(st.session_state.total_pemasukan * 0.1)
    st.session_state['val_pemasukan'] = st.session_state.total_pemasukan<=0
    st.session_state['val_pengeluaran'] = st.session_state.total_pengeluaran<=0
    st.session_state['total_subs_exist'] = st.session_state.total_subs>0
    st.session_state['val_utang'] = st.session_state.total_utang
    st.session_state['total_net_worth'] = st.session_state.total_aset - st.session_state.total_utang_outstanding

    
def cek_pemasukan_pengeluaran():
    if st.session_state.total_pemasukan==0 or st.session_state.total_pengeluaran==0:
        default_warning()
    else:
        if st.session_state.total_pemasukan>st.session_state.total_pengeluaran:
            st.success("Good job! Pemasukan kamu {:,} masih lebih tinggi daripada pengeluaran {:,}. Kamu masih bisa nabung {:,} lagi.".format(st.session_state.total_pemasukan
                                                                                                                                                ,st.session_state.total_pengeluaran
                                                                                                                                                ,st.session_state.selisih_pemasukan_pengeluaran))
        elif st.session_state.total_pemasukan<st.session_state.total_pengeluaran:
            st.error("Waduh! Pengeluaran kamu {:,} melebihi pemasukan {:,}. Berikut saran yang dapat kamu lakukan".format(st.session_state.total_pengeluaran,st.session_state.total_pemasukan))
            st.write("* Kamu membutuhkan pemasukan tambahan untuk mengimbangi pengeluaran yang terlampau besar.")
            st.write("* Kamu dapat meminimalisir pengeluaran yang tidak perlu.")
            st.write("* * Kamu dapat menghemat uang sebesar {:,} jika kamu menghentikan seluruh Subscription tersebut".format(st.session_state.total_subs)) if st.session_state.total_subs_exist else st.write("")
        else:
            default_warning()
    return st.session_state.cek_pemasukan_pengeluaran

def cek_rasio_utang_pemasukan():         
    if st.session_state.total_pemasukan<=0:
        default_warning("Masukkan pemasukan dan cicilan kamu terlebih dahulu.") 
    elif st.session_state.total_cicilan>st.session_state.target_rasio_utang_pemasukan:
        st.error("Waduh! Cicilan kamu lebih besar dari maksimal rasio cicilan yang diijinkan {} atau setara dengan {:,}".format(st.session_state.rasio_dir
                                                                                                                              , st.session_state.target_rasio_utang_pemasukan
                                                                                                                              ))
        st.subheader("Rekomendasi:")
        st.write("* Cari pemasukan tambahan")
        st.write("* Kurangi pengeluaran utang dengan memperpanjang tenor atau melunasi utang sekaligus")
    else:
        st.success("Good job! Cicilan kamu {:,} masih dalam target rasio yang direncanakan {}% atau maksimal cicilan sebesar {:,} dari total pemasukan {:,}.".format(
                                                                                                                                    st.session_state.total_cicilan
                                                                                                                                    , st.session_state.rasio_dir
                                                                                                                                    , st.session_state.target_rasio_utang_pemasukan
                                                                                                                                    , st.session_state.total_pemasukan))
def cek_rasio_tabungan_pemasukan():
    if st.session_state.total_saving==0 or st.session_state.total_pemasukan==0:
        default_warning("Masukkan Jumlah Pemasukan yang diterima dan Jumlah Tabungan (Saving) yang ditabung setiap bulannya pada tab Pengeluaran.")
    else:    
        if st.session_state.total_saving >= st.session_state.target_rasio_tabungan_pemasukan:
            st.success("Good job. Uang yang kamu tabung setiap bulan {:,} sudah mencapai target rasio tabungan {}% terhadap pemasukan {:,}".format(st.session_state.total_saving
                                                                                                                                            ,st.session_state.rasio_tabungan_pemasukan
                                                                                                                                            ,st.session_state.total_pemasukan)) 
        else:
            st.error("Waduh. Target tabungan kamu belum tercapai karena kamu berencana menabung sebesar {:,} ({}% dari pemasukan) sementara".format(st.session_state.target_rasio_tabungan_pemasukan
                                                                                                                                                    , st.session_state.rasio_tabungan_pemasukan
                                                                                                                                                        , st.session_state.total_pemasukan))
def cek_rasio_utang_outstanding_aset():
    if st.session_state.total_utang_outstanding>0 and st.session_state.total_aset>0:
        if st.session_state.total_utang_outstanding<=st.session_state.target_rasio_utang_outstanding_aset:
            st.success("Good job! Jumlah utang outstanding kamu dibawah target, yakni {}% dari total aset {:,} atau setara dengan {:,}. Total Utang Outstanding kamu adalah {:,} ".format(st.session_state.rasio_utang_aset
                                                                                                                                                                                        ,st.session_state.total_aset
                                                                                                                                                                                        ,st.session_state.target_rasio_utang_outstanding_aset
                                                                                                                                                                                        ,st.session_state.total_utang_outstanding))    
        else:
            st.error("Waduh. Jumlah Utang Outstanding kamu adalah {:,}, melebihi target yang kamu tentukan yakni {:,}% dari total aset {:,} atau setara dengan {:,}. Artinya Utang Outstanding tersebut akan mengejar kita sekalipun seluruh Aset telah dijual / dilikuidasi.".format(st.session_state.total_utang_outstanding
                                                                                                                    ,st.session_state.rasio_utang_aset
                                                                                                                    ,st.session_state.total_aset
                                                                                                                    ,st.session_state.target_rasio_utang_outstanding_aset
                                                                                                                    ))
    else:
        default_warning("Masukkan jumlah Utang Outstanding pada tab Utang dan Jumlah Aset pada tab Aset")

def cek_rasio_asuransi_pemasukan():
    if st.session_state.asuransi & st.session_state.total_pemasukan:
        if st.session_state.rasio_premi_asuransi_pemasukan<=0.1:
            st.success("Good job! Total Premi Asuransi kamu adalah {:,} dan nominal tersebut hanya {} dari total pemasukan kamu {:,}. Premi Asuransi yang ideal ialah 10% dari total Pemasukan. Kalau Preminya kebanyakan khawatir nanti bakal susah nabungnya.".format(st.session_state.asuransi
                                                                                                               ,st.session_state.rasio_premi_asuransi_pemasukan
                                                                                                               ,st.session_state.total_pemasukan
                                                                                                               ))
        else:
            st.error("Waduh! Total Premi Asuransi kamu adalah {:,} dan nominal tersebut {}% dari total pemasukan kamu {:,}. Premi Asuransi yang ideal ialah 10% dari total Pemasukan ({:,}). Kalau Preminya kebanyakan khawatir nanti bakal susah nabungnya.".format(st.session_state.asuransi
                                                                                                    ,st.session_state.rasio_premi_asuransi_pemasukan
                                                                                                    ,st.session_state.total_pemasukan
                                                                                                    , st.session_state.target_premi_asuransi))
    else:
        default_warning("Masukkan Jumlah Premi Asuransi pada tab Pengeluaran dan Jumlah Pemasukan pada tab Pemasukan")

def cek_net_worth():
    if st.session_state.total_aset & st.session_state.total_utang_outstanding:
        if st.session_state.total_net_worth>0:
            st.success("Total Net Worth kamu adalah {}. Total Aset kamu adalah {:,} sementara Total Utang Outstanding adalah {:,}. Way to go to Financial Indepentend, Retire Early!")
        else:
            st.error("Waduh. Total Net Worth kamu adalah {:,}. Total Utang Outstanding {:,} lebih besar dari Total Aset".format(st.session_state.total_net_worth
                                                                                                  , st.session_state.total_utang_outstanding
                                                                                                  ,st.session_state.total_aset))
    else:
        default_warning("Masukkan Jumlah Aset pada tab Aset dan Jumlah Utang pada tab Utang")