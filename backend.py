import streamlit as st
import re

input_loops = {
    'Aset':{
        'info':"""Pada bagian ini kita akan menentukan berapa aset yang dimiliki.""",
        'kategori':{
            'aset_lancar':{
                'Kas di tangan':0,
                'Tabungan':0,
                'Deposito':0,
                'Reksadana Pasar Uang':0
            },
            'aset_tidak_lancar':{
                'emas_logam_mulia':0,
                'rdpt':0,
                'rd_campuran':0,
                'rd_saham':0,
                'obligasi':0,
                'saham':0,
                'nilai_tunai_polis':0,
                'lain-lain':0
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