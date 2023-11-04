import streamlit as st
import re

def callback_input():
    if 'data' not in st.session_state:
        st.session_state['data'] = {}
    
    st.session_state.data = {
        'details':{
            'aset':{
                'aset_lancar':{
                    'aset_kas':{
                        'kas_di_tangan':st.session_state.aset_lancar__kas_di_tangan,
                        'tabungan': st.session_state.aset_lancar__tabungan,
                        'deposito': st.session_state.aset_lancar__deposito,
                        'rdpu':st.session_state.aset_lancar__rdpu
                    },
                    'aset_investasi':{
                        'emas':st.session_state.aset_lancar__emas,
                        'rdpt':st.session_state.aset_lancar__rdpt,
                        'rdc':st.session_state.aset_lancar__rdc,
                        'rds':st.session_state.aset_lancar__rds,
                        'obligasi':st.session_state.aset_lancar__obligasi,
                        'saham':st.session_state.aset_lancar__saham,
                        'polis':st.session_state.aset_lancar__polis,
                        'others':st.session_state.aset_lancar__others

                    }
                },
                'aset_tidak_lancar':{

                }
            },
            'kewajiban':{

            }
        }
    }
    st.write(st.session_state.data)