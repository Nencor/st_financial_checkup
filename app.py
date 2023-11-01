import streamlit as st 
from backend import *

input_loops = {
    'Aset':{
        'info':"""Pada bagian ini kita akan menentukan berapa aset yang dimiliki.""",
        'kategori':{
            'aset_lancar':{
                'Aset Kas':{
                'Kas di tangan':0,
                'Tabungan':0,
                'Deposito':0,
                'Reksadana Pasar Uang':0
                },
                'Aset Investasi':{
                'Emas Logam Mulia':0,
                'Reksadana Pendapatan Tetap':0,
                'Reksadana Campuran':0,
                'Reksadana Saham':0,
                'Obligasi':0,
                'Saham':0,
                'Nilai Tunai Polis':0,
                'Lain-Lain':0
                }
            }
        }

    },
    'Kewajiban':{

    },
    'Pendapatan':{

    },
    'Pengeluaran':{
        
    },

    'Lihat Hasil':{

    }
}
if 'data' not in st.session_state:
    st.session_state['data'] = input_loops


tab1,tab2,tab3,tab4,tab5 = st.tabs(list(input_loops))


with st.sidebar:
    st.title("Tikidata Analytics Financial Checkup")
    st.slider("Allowed Debt to Income Ratio(%)",min_value=0,max_value=100,format="%g",value=30)
    st.subheader("Disclaimer: Tikidata dan Tim tidak mengambil data apapun yang dimasukkan dalam aplikasi ini.")

with tab1:
    st.write(st.session_state.data['Aset']['info'])

    with st.expander("Aset Lancar"):
        col1,col2 = st.columns(2)
        with col1:
            for komponen in st.session_state.data['Aset']['kategori']['aset_lancar']['Aset Kas']:
                output = st.number_input(komponen,0,key=komponen,format='%g')
                st.session_state.data['Aset']['kategori']['aset_lancar']['Aset Kas'][komponen] = output
            st.subheader("Total Aset Kas: {:,}".format(get_total(st.session_state.data['Aset']['kategori']['aset_lancar']['Aset Kas'])))                
        
        with col2:
            st.subheader("Total Aset Investasi: {:,}".format(get_total(st.session_state.data['Aset']['kategori']['aset_lancar']['Aset Investasi'])))
            for komponen in st.session_state.data['Aset']['kategori']['aset_lancar']['Aset Investasi']:
                output = st.number_input(komponen,0,key=komponen,format='%g')
                st.session_state.data['Aset']['kategori']['aset_lancar']['Aset Investasi'][komponen] = output

