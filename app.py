import streamlit as st 
from backend import *
tab1,tab2,tab3,tab4,tab5 = st.tabs(list(input_loops))


with st.sidebar:
    st.title("Tikidata Analytics Financial Checkup")
    st.slider("Allowed Debt to Income Ratio(%)",min_value=0,max_value=100,format="%g",value=30)
    st.subheader("Disclaimer: Tikidata dan Tim tidak mengambil data apapun yang dimasukkan dalam aplikasi ini.")
    
with tab1:
    st.write(st.session_state.data['Aset']['info'])

    with st.expander("Aset Lancar"):
        for komponen in st.session_state.data['Aset']['kategori']['aset_lancar']:
            st.number_input(komponen,0,key=komponen,format='%g')
        

    with st.expander("Aset Tidak Lancar"):
        st.write('hello')

    # print(st.session_state.data['Aset']['info'])