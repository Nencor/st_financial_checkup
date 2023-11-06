import streamlit as st 
from backend import *


initialize_totalan(state_names=['total_aset_kas']) #set the st.session_state.total_aset_kas = 0

def number_input (labelnya,keynya,helpnya='',default_min_value=0):
    
    st.session_state.keynya = st.number_input(label=labelnya
                             ,value=default_min_value
                             ,min_value=default_min_value
                             ,on_change=callback_input
                             ,key=keynya
                             ,help=helpnya)
    

    
tab1,tab2,tab3,tab4,tab5 = st.tabs(['Aset','Kewajiban','Pendapatan','Pengeluaran','Debug'])
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
            # st.subheader("Total Aset Kas: {}".format(st.session_state.total_aset_kas)) #uncomment this to see the error
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
with tab2:
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Jangka Pendek")
        number_input("Kartu Kredit",'kewajiban_jangka_pendek__kartu_kredit')
        number_input("Pinjaman Pribadi",'kewajiban_jangka_pendek__pinjaman_pribadi')    
        number_input("Pinjaman Mobil",'kewajiban_jangka_pendek__pinjaman_mobil')
        number_input("Pinjaman KTA (Kredit Tanpa Agunan)",'kewajiban_jangka_pendek__kta')                          
        number_input("Lainnya",'kewajiban_jangka_pendek__lainnya')        
    with col2:
        st.subheader("Jangka Panjang")
        number_input("Pinjaman Rumah",'kewajiban_jangka_panjang__pinjaman_rumah')
        number_input("Pinjaman Apartemen",'kewajiban_jangka_panjang__pinjaman_apartement')        
        number_input("Pinjaman dari Perusahaan",'kewajiban_jangka_panjang__pinjaman_perusahaan')        
        number_input("Pinjaman lainnya",'kewajiban_jangka_panjang__kartu_kredit')        

with tab3:
    st.subheader("Pendapatan rutin per bulan")
    number_input("Gaji",'pendapatan_rutin__gaji')
    number_input("Bagi hasil bisnis",'pendapatan_rutin__bagi_hasil_bisnis')        
    number_input("Pendapatan Sewa",'pendapatan_rutin__pendapatan_sewa')
    number_input("Pendapatan Lain-lain",'pendapatan_rutin__lain_lain')     

with tab4:
    st.subheader("Pengeluaran rutin per bulan")
    col1,col2,col3 = st.columns(3)
    with col1:
        number_input("Gaji",'pengeluaran_rutin__tabungan_investasi')
        number_input("Zakat/Perpuluhan/Sedekah",'pengeluaran_rutin__zakat_perpuluhan_sedekah')
        number_input("Premi Asuransi",'pengeluaran_rutin__asuransi')    
        number_input("Listrik",'pengeluaran_rutin__tabungan_listrik')    
        number_input("Air / PDAM",'pengeluaran_rutin__tabungan_air')
    with col2:
        number_input("Pulsa / Paket Data Smartphone",'pengeluaran_rutin__telepon')
        number_input("Internet",'pengeluaran_rutin__internet')
        number_input("Belanja bulanan / dapur",'pengeluaran_rutin__belanja_dapur')
        number_input("Transportasi",'pengeluaran_rutin__transportasi')    
        number_input("Kesehatan",'pengeluaran_rutin__kesehatan')    
    with col3:
        number_input("Pendidikan",'pengeluaran_rutin__pendidikan')    
        number_input("Belanja Pribadi",'pengeluaran_rutin__belanja_pribadi')    
        number_input("Pengeluaran Anak",'pengeluaran_rutin__pengeluaran_anak')
        number_input("Cicilan utang",'pengeluaran_rutin__cicilan_utang')
        number_input("Gaya Hidup",'pengeluaran_rutin__gaya')      
with tab5:
    st.write(st.session_state)