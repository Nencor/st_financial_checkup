import streamlit as st 
from backend import *

initialize(session_states=['total_pemasukan'
                           ,'total_pengeluaran'
                           ,'total_cicilan'
                           ,'total_subs'
                           ,'total_living_cost'
                           ,'target_rasio_utang_pemasukan'
                           ,'cek_pemasukan_pengeluaran'
                           ,'val_pemasukan'
                           ,'val_pengeluaran'
                           ,'total_saving'
                           ,'target_rasio_tabungan_pemasukanras'                           
                           ])

def number_input (labelnya,keynya,helpnya='',default_min_value=0):
    keynya = st.number_input(label=labelnya
                             ,value=default_min_value
                             ,min_value=default_min_value
                             ,on_change=get_total
                             ,key=keynya
                             ,help=helpnya
                             ,step=1000000)
def slider_input(labelnya,keynya,helpnya='',valuenya=50,default_min_value=0,default_max_value=100):
    st.slider(label=labelnya
              ,key=keynya
              ,help=helpnya
              ,min_value=default_min_value
              ,max_value=default_max_value
              ,value=valuenya
              ,on_change=get_total
              )
    

    
tab1,tab2,tab3,tab4,tab5 = st.tabs(['Pemasukan','Pengeluaran','Financial Checkup','Debug','Credit'])


with st.sidebar:
    st.title("Tikidata Analytics Financial Checkup")
    slider_input("Target rasio utang terhadap pemasukan (%)",'rasio_dir',valuenya=30)
    slider_input("Target rasio tabungan terhadap pemasukan (%)",'rasio_tabungan_pemasukan',valuenya=50)
    # slider_input("Target Emergency Fund (bulan)",keynya='dana_darurat',default_min_value=3,default_max_value=12,valuenya=6)




with tab1:
        st.subheader("Total Pemasukan: {:,}".format(st.session_state.total_pemasukan))
        number_input("Gaji",keynya='gaji',helpnya="Gaji yang diterima setiap bulan include THR dan bonus prorata per bulan")
        number_input("Hasil usaha",keynya='hasil_usaha',helpnya="Rata-rata/minimum hasil usaha yang diterima setiap bulan")
        number_input("Sampingan",keynya='sampingan',helpnya='Rata-rata / minimum pemasukan sampingan seperti ngajar les, ngeband, GoCar, komisi asuransi,komisi properti setiap bulannya')
        number_input("Uang jajan dari papa",keynya='uang_papa',helpnya='Rata-rata / minimum pemasukan dari investor kandung setiap bulan')
        number_input("Deposito",keynya='deposito',helpnya="Bila memiliki Investasi Deposito yang masuk ke rekening setiap bulan.")

        with st.expander("FAQ"):
             st.write("FAQ bakal diupdate disini")

with tab2:
    st.header("Total Pengeluaran: {:,}".format(st.session_state.total_pengeluaran))
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Living Cost: {:,}".format(st.session_state.total_living_cost))
        number_input('Sewa Kos / Apartemen',keynya='kos_apartemen',helpnya='Biaya sewa kos/apartemen per bulan')
        number_input("Biaya Iuran Pemeliharaan Lingkungan (IPL)",keynya='ipl',helpnya='Biaya Iuran Pemeliharaan Lingkungan setiap bulannya')
        number_input("Biaya listrik",keynya='pln',helpnya="Listrik prabayar / paskabayar tiap bulan (AVG)")
        number_input("Biaya internet WIFI",keynya='internet_wifi',helpnya='Paket data internet wifi')
        number_input("Biaya PDAM",keynya='pdam',helpnya='Tulis 0 kalo kamu pake air sumur / air sungai')
        number_input("Paket data Smartphone",keynya='paket_data',helpnya='Harga paket data per bulan')
        number_input("Sedekah/Infaq/Perpuluhan/Kemanusiaan",keynya='kemanusiaan',helpnya="Budget untnuk sedekah/infaq/perpuluhan/kemanusiaan lainnya")
        number_input("Bakti untuk orang tua",keynya='bakti_ortu',helpnya='Jumlah uang yang kamu berikan untuk orang tua setiap bulannya')
        number_input("Uang Makan",keynya='uang_makan')
        number_input("Transport Bulanan",keynya='transport')
        number_input("Premi Asuransi",keynya='asuransi',helpnya="Budget pembayaran premi asuransi tiap bulannya. Jika pembayaran tahunan maka diinput prorata per bulan.")
        number_input("Parkiran Kendaraan",keynya='parkiran',helpnya='Jumlah budget Parkiran baik di kantor / rumah / apartemen yang ditanggung pribadi')
    with col2:
        st.subheader("Total Saving: {:,}".format(st.session_state.total_saving))
        number_input("Kas di tangan",keynya='rekening_tangan',helpnya='Uang tunai yang dimiliki secara tunai')
        number_input("Rekening tabungan",keynya='rekening_tabungan',helpnya='Total uang di seluruh rekening tabungan')
        number_input("Reksadana Pasar Uang",keynya='rdpu')
        number_input("Reksadana Pendapatan Tetap",keynya='rdpt')
        number_input("Reksadana Saham",keynya='rds')
        number_input("Reksadana Obligasi",keynya='rd_obligasi')

        st.subheader("Total Cicilan: {:,}".format(st.session_state.total_cicilan))
        number_input("Cicilan rumah/apartemen/",keynya='cicilan_rumah',helpnya='Total cicilan seluruh rumah/apartemen per bulan')
        number_input("Cicilan motor",keynya='cicilan_motor',helpnya="Total cicilan seluruh motor per bulan")
        number_input("Cicilan mobil",keynya='cicilan_mobil',helpnya='Total cicilan seluruh mobil per bulan')
        number_input("Cicilan Kartu Kredit",keynya='cicilan_cc',helpnya='Total cicilan seluruh Kartu Kredit per bulan')
    
        st.subheader("Total Subscription: {:,}".format(st.session_state.total_subs))
        number_input("Streaming Spotify",keynya='subs_spotify')
        number_input("Streaming Netflix",keynya='subs_netflix')
        number_input('Subscription ChatGPT',keynya='subs_chatgpt')
        number_input("Subscription/Streaming lainnya",keynya='subs_others')
        number_input("Gym/Zumba/Poundfit/Yoga Subscription",keynya='gym')

    with st.expander("FAQ"):
        st.write("FAQ bakal diupdate disini")
        
with tab3:
    st.write("Di bawah ini beberapa feedback yang dapat dipertimbangkan:")
    with st.expander("Cek Cashflow"):
        cek_pemasukan_pengeluaran()

    with st.expander("Cek rasio utang terhadap pemasukan"):
        cek_rasio_utang_pemasukan()

    with st.expander("Cek rasio tabungan terhadap pemasukan"):
        cek_rasio_tabungan_pemasukan()
with tab4:
    st.json(st.session_state)
    # st.write(type(st.session_state))
with tab5:
    st.write("Kudos to the following friends and colleague for their contributions in this project. ")
    st.write("Disclaimer: Tikidata dan Tim tidak mengambil data apapun yang dimasukkan dalam aplikasi ini. Tools ini bukan merupakan rekomendasi keuangan.")
    st.write("Follow our [Linkedin Pages](https://www.linkedin.com/company/tikidata-analytics) for more freebies.")
    st.write("This project is in collaboration with [Asuransimurni.com](https://asuransimurni.com)")
    st.write("Any comments and feedbacks are welcome in [Twitter](https://twitter.com/asmurcom).")