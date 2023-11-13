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
                           ,'total_subs_exist'
                           ,'total_saving'
                           ,'target_rasio_tabungan_pemasukanras'  
                           ,'total_aset_kas_lancar'   
                           ,'total_aset_lancar'       
                           ,'total_aset_tidak_lancar'
                           ,'total_aset' 
                           ,'total_aset_investasi_lancar'   
                           ,'total_utang'
                           ,'total_utang_jangka_pendek'
                           ,'total_utang_jangka_panjang'
                           ,'total_utang_outstanding'
                           ,'target_rasio_utang_outstanding_aset'   
                           ,'target_premi_asuransi'       
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
    

    
tab1,tab2,tab3,tab4,tab5,tab6,tab7 = st.tabs(['Home','Pemasukan','Pengeluaran','Aset','Utang','Financial Checkup','Debug'])


with st.sidebar:
    st.title("[Asmurcom](https://twitter.com/asmurcom) Financial Checkup")
    st.subheader("Konfigurasi")
    slider_input("Target Rasio Utang terhadap Pemasukan (%)",'rasio_dir',valuenya=30,default_max_value=100,helpnya="30% merupakan rasio maksimal yang direkomendasikan")
    slider_input("Target Rasio Tabungan terhadap Pemasukan (%)",'rasio_tabungan_pemasukan',valuenya=50,default_max_value=100)
    slider_input("Target Rasio Utang Outstanding terhadap Aset (%)",'rasio_utang_aset',default_max_value=100,valuenya=10)
    # slider_input("Target Emergency Fund (bulan)",keynya='dana_darurat',default_min_value=3,default_max_value=12,valuenya=6)



with tab1:
    st.subheader("Hi")
    st.write("Welcome to Asmurcom Financial Checkup. The purpose of this app is helping users finding insight/pattern regarding their Income/Expenditure/Asset/Expenses.")
    st.write("Kudos to the following friends and colleague for their contributions in this project. ")
    st.write("* [Asuransimurni.com](https://asuransimurni.com) - Agen Asuransi AXA Financial Indonesia")
    st.write("* [Pitchstar Chernenko](https://www.linkedin.com/in/nencor) and [Tikidata Analytics](https://www.linkedin.com/company/tikidata-analytics)  - Data Analytics Agency")
    st.write("* [Guntur](https://twitter.com/47px) - Dark Magick Software Engineer")
    st.subheader("How to use")
    st.write("* * Fill current income in 'Pemasukan' tab.")
    st.write("* * Fill current Expenditure / Expenses in 'Aset' tab.")
    st.write("* * Fill current Asset in 'Aset' tab.")
    st.write("* * Fill current Liabilities, Morgage in 'Utang' tab.")
    st.write("* * Check the result in 'Financial Checkup' tab.")
    st.subheader("Disclaimer:")
    st.write("Disclaimer: Tikidata dan Developers don't store your data. The tools provides no Financial Recommendation. Always reach out your personal Financial Planner to seek any advice / guidance in Financial.")
    st.subheader("Support:")
    st.write("Any comments and feedbacks are welcome in [Twitter](https://twitter.com/asmurcom). Should you need more metrics / data, let's talk!")
    st.subheader("FAQ")
    with st.expander("What distinguish 'Total Cicilan' in 'Pengeluaran' tab with 'Total Utang' in 'Utang' tab."):
        st.write("* * 'Total Cicilan' in 'Pengeluaran' is something that we pay every month while 'Total Utang' in 'Utang' is how much the Unpaid/Outstanding Liabilities/Morgages.")
    with st.expander("I want Apps and Automation that work similar to this"):
        st.write("* * Feel free to reach out Chernenko through his [Twitter](https://twitter.com/asmurcom) and contact him directly.")
    st.subheader("Future Improvement")
    st.write("* Add Visualizations and Charts to help users in digesting data and information")
    st.write("* Translation texts")
    st.write("* Improving layout, UI / UX")
    st.write("* Add more Financial Metrics and Ratios")

with tab2:
        st.subheader("Total Pemasukan: {:,} per bulan.".format(st.session_state.total_pemasukan))
        number_input("Gaji",keynya='gaji',helpnya="Gaji yang diterima setiap bulan include THR dan bonus prorata per bulan")
        number_input("Hasil usaha",keynya='hasil_usaha',helpnya="Rata-rata/minimum hasil usaha yang diterima setiap bulan")
        number_input("Sampingan",keynya='sampingan',helpnya='Rata-rata / minimum pemasukan sampingan seperti ngajar les, ngeband, GoCar, komisi asuransi,komisi properti setiap bulannya')
        number_input("Uang jajan dari papa",keynya='uang_papa',helpnya='Rata-rata / minimum pemasukan dari investor kandung setiap bulan')
        number_input("Deposito",keynya='deposito',helpnya="Bila memiliki Investasi Deposito yang masuk ke rekening setiap bulan.")

        with st.expander("FAQ"):
             st.write("FAQ bakal diupdate disini")

with tab3:
    st.subheader("Total Pengeluaran: {:,} per bulan.".format(st.session_state.total_pengeluaran))
    st.write("##### Total living Cost: {:,} per bulan".format(st.session_state.total_living_cost))
    with st.expander("Living cost"):
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
    
    st.write("##### Total Saving: {:,}".format(st.session_state.total_saving))
    with st.expander("Saving"):    
        number_input("Kas di tangan",keynya='rekening_tangan',helpnya='Jika menabung uang tunai secara rutin')
        number_input("Rekening tabungan",keynya='rekening_tabungan',helpnya='Jika menabung di rekening tabungan secara rutin')
        number_input("Reksadana Pasar Uang",keynya='rdpu',helpnya='Jika menabung di Reksadana Pasar Uang secara rutin')
        number_input("Reksadana Pendapatan Tetap",keynya='rdpt',helpnya='Jika menabung di Reksadana Pendapatan Tetap')
        number_input("Reksadana Saham",keynya='rds',helpnya='Jika menabung di Reksadana Saham secara rutin')
        number_input("Reksadana Obligasi",keynya='rd_obligasi',helpnya='Jika menabung di Reksadana Obligasi secara rutin')

    st.write("##### Total Cicilan: {:,}".format(st.session_state.total_cicilan))
    with st.expander("Cicilan"):
        
        number_input("Cicilan KPR",keynya='cicilan_kpr',helpnya='Total cicilan seluruh rumah per bulan')
        number_input("Cicilan KPA",keynya='cicilan_kpa',helpnya='Total cicilan seluruh apartemen per bulan')
        number_input("Cicilan motor",keynya='cicilan_motor',helpnya="Total cicilan seluruh motor per bulan")
        number_input("Cicilan mobil",keynya='cicilan_mobil',helpnya='Total cicilan seluruh mobil per bulan')
        number_input("Cicilan Kartu Kredit",keynya='cicilan_cc',helpnya='Total cicilan seluruh Kartu Kredit per bulan')
    
    st.write("##### Total Subscription: {:,}".format(st.session_state.total_subs))
    with st.expander("Subscription"):
        
        number_input("Streaming Spotify",keynya='subs_spotify',helpnya='Biaya langganan Spotify tiap bulannya')
        number_input("Streaming Netflix",keynya='subs_netflix', helpnya='Biaya langganan Netflix tiap bulannya')
        number_input('Subscription ChatGPT',keynya='subs_chatgpt',helpnya='Biaya langganan ChatGPT setiap bulannya')
        number_input("Subscription/Streaming lainnya",keynya='subs_others',helpnya='Biaya langganan streaming lainnya')
        number_input("Gym/Zumba/Poundfit/Yoga Subscription",keynya='gym',helpnya='Biaya langganan gym tiap bulannya')
        number_input("Mentoring/Coaching",keynya='mentoring',helpnya='Biaya langganan mentoring/coaching tiap bulannya')

    with st.expander("FAQ"):
        st.write("FAQ bakal diupdate disini")
        
with tab4:
    st.subheader("Total Aset: {:,}".format(st.session_state.total_aset))
    
    st.write("##### Total Aset Lancar: {:,}".format(st.session_state.total_aset_lancar))
    
    with st.expander("Aset Kas Lancar"):
        st.write("##### Total Aset Kas Lancar: {:,}".format(st.session_state.total_aset_kas_lancar))
        number_input("Kas di tangan",keynya="aset_lancar__kas_di_tangan")
        number_input("Tabungan",keynya="aset_lancar__tabungan")
        number_input("Deposito",keynya="aset_lancar__deposito")
        number_input("Reksadana Pasar Uang",keynya="aset_lancar__rdpu")
    
    with st.expander("Aset Investasi Lancar"):
        st.write("##### Total Investasi Lancar: {:,}".format(st.session_state.total_aset_investasi_lancar))
        number_input("Emas / Logam berharga",keynya="aijp__emas")
        number_input("Reksadana Pendapatan Tetap",keynya="aijp__rdpt")
        number_input("Reksadana Campuran",keynya="aijp__rdc")
        number_input("Reksadana Saham",keynya="aijp__rds")        
        number_input("Obligasi",keynya="aijp__obligasi")        
        number_input("Saham",keynya="aijp__saham")
        number_input("Nilai Tunai Polis",keynya="aijp__nilai_tunai_asuransi",helpnya="Berlaku pada Asuransi Dwiguna dan Unit Link")
        number_input("Lain-lain",keynya="aijp__lain_lain")
    
    st.write("##### Total Aset Tidak Lancar: {:,}".format(st.session_state.total_aset_tidak_lancar))
    with st.expander("Aset Konsumsi Tidak Lancar"):
        number_input("Rumah dihuni",keynya="aktl__rumah",helpnya="Taksiran harga rumah bila dijual hari ini")
        number_input("Perhiasan",keynya="aktl__perhiasan",helpnya="Taksiran harga perhiasan bila dijual hari ini")
        number_input("Mobil",keynya="aktl__mobil",helpnya="Taksiran harga mobil bila dijual hari ini")
        number_input("Motor",keynya="aktl__motor",helpnya="Taksiran harga motor bila dijual hari ini")

    with st.expander("Aset Investasi Tidak Lancar"):
        number_input("BPJS Ketenagakerjaan",keynya="aitl__bpjsnaker")
        number_input("BPJS Jaminan Hari Tua",keynya="aitl__bpjsjht")
        number_input("Jaminan Pensiun (DPLK)",keynya="aitl__dplk")
        number_input("Barang Koleksi / Antique",keynya="aitl__koleksi",helpnya="Taksiran harga Koleksi / Antique bila dijual hari ini")
        number_input("Properti",keynya="aitl__properti",helpnya="Taksiran harga rumah bila dijual hari ini")
        number_input("Tanah",keynya="aitl__tanah",helpnya="Taksiran harga tanah bila dijual hari ini")
        number_input("Nilai Bersih Usaha",keynya='aitl__nilai_bersih_usaha',helpnya="Taksiran nilai bisnis")

with tab5:
    st.subheader("Total Utang: {:,}".format(st.session_state.total_utang_outstanding))
    st.write("##### Total Utang Jangka Pendek: {:,}".format(st.session_state.total_utang_jangka_pendek))
    with st.expander("Utang jangka pendek"):
        number_input("Kartu Kredit",keynya="ujpe__cc",helpnya="Total Outstanding Utang Kartu Kredit")
        number_input("Pinjaman Pribadi ",keynya='ujpe__personal_loan',helpnya=("Total Outstanding Pinjaman Pribadi"))
        number_input("KKB Mobil",keynya='ujpe__mobil',helpnya="Total Outstanding KKB Mobil")
        number_input("KKB Motor",keynya='ujpe__motor',helpnya="Total Outstanding KKB Motor")
        number_input("Kredit tanpa agunan",keynya='ujpe__kta',helpnya="Total Outstanding KTA")
        number_input("Kredit lainnya",keynya='ujpe__lainnya',helpnya="Total Outstanding Kredit lainnya")

    st.write("##### Total Utang Jangka Panjang: {:,}".format(st.session_state.total_utang_jangka_panjang))
    with st.expander("Utang jangka panjang"):
        number_input("Kredit Rumah / KPR",keynya='ujpa__kpr')
        number_input("Kredit Apartemen / KPA",keynya='ujpa__kpa')
        number_input("Pinjaman lainnya (jangka panjang)",keynya='ujpa__lainnya')

with tab6:
    st.write("Di bawah ini beberapa feedback yang dapat dipertimbangkan:")
    col1,col2 = st.columns(2)
    with col1:
        with st.expander("Cek Cashflow"):
            cek_pemasukan_pengeluaran()        
        with st.expander("Cek rasio Utang Oustanding terhadap Aset"):
            cek_rasio_utang_outstanding_aset()
        with st.expander("Cek Net Worth"):
            cek_net_worth()

    with col2:
        with st.expander("Cek rasio utang terhadap Pemasukan"):
            cek_rasio_utang_pemasukan()
        with st.expander("Cek rasio Premi Asuransi terhadap Pemasukan"):
            cek_rasio_asuransi_pemasukan()
        with st.expander("Cek rasio tabungan terhadap Pemasukan"):
            cek_rasio_tabungan_pemasukan()
             
with tab7:
    st.json(st.session_state)
    # st.write(type(st.session_state))
