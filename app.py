import streamlit as st 
from backend import *



def number_input (labelnya,keynya,helpnya=''):
    st.number_input(label=labelnya
        ,value=default_min_value,min_value=default_min_value
        ,on_change=callback_input
        ,key=keynya
        ,help=helpnya
    )
tab1,tab2 = st.tabs(['Aset','Kewajiban'])
default_min_value = 0


with st.sidebar:
    st.title("Tikidata Analytics Financial Checkup")
    st.slider("Allowed Debt to Income Ratio(%)",min_value=0,max_value=100,format="%g",value=30)
    st.subheader("Disclaimer: Tikidata dan Tim tidak mengambil data apapun yang dimasukkan dalam aplikasi ini.")

with tab1:
    with st.expander("Aset Lancar"):
        col1,col2 = st.columns(2)
        with col1:   
            st.subheader("Aset Kas")
            number_input('Kas di Tangan','aset_lancar__kas_di_tangan')
            number_input('Tabungan','aset_lancar__tabungan')
            number_input('Deposito','aset_lancar__deposito')
            number_input('Reksadana Pasar Uang','aset_lancar__rdpu')            
        with col2:        
            st.subheader("Aset Investasi")
            number_input('Emas Logam Mulia','aset_lancar__emas')                       
            number_input('Reksadana Pendapatan Tetap','aset_lancar__rdpt')
            number_input('Reksadana Campuran','aset_lancar__rdc')  
            number_input('Reksadana Saham','aset_lancar__rds')                    
            number_input('Obligasi','aset_lancar__obligasi')
            number_input('Saham','aset_lancar__saham')
            number_input('Nilai Tunai Polis','aset_lancar__polis')
            number_input('Lain-lain','aset_lancar__others')

    with st.expander("Aset Tidak Lancar"):
        col1,col2 = st.columns(2)
        with col1:
            st.subheader("Aset Konsumsi")
            number_input("Harga rumah (milik) dihuni",'aset_tidak_lancar__rumah')
            number_input("Harga perhiasan",'aset_tidak_lancar__perhiasan')
            number_input("Harga mobil",'aset_tidak_lancar__mobil')
            number_input("Harga motor",'aset_tidak_lancar__motor')            
        with col2:
            st.subheader("Aset Investasi")
            number_input("BPJS Ketenagakerjaan",'aset_tidak_lancar__bpjs_naker')
            number_input("Dana Pensiun",'aset_tidak_lancar__pensiun')
            number_input("Barang koleksi",'aset_tidak_lancar__koleksi')
            number_input("Properti","aset_tidak_lancar__properti")
            number_input("Tanah","aset_tidak_lancar__tanah")
            number_input("Nilai Bersih Usaha","aset_tidak_lancar__bisnis")
            print("Hello world")