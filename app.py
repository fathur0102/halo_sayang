import streamlit as st

# Pengaturan halaman
st.set_page_config(
    page_title="Ucapan Cinta",
    page_icon="💖",
    layout="centered"
)

# Variabel untuk login
NAMA_PACAR = "virginia shalikhah"
PASSWORD = "fahmi aufa fadhil"

# Fungsi halaman login
def login():
    st.title("Hallooo sayaangggg💖 coba buka ini yaaa, tapi sayangg harus login dulu. buat passwordnya nama asli pacar kamu ")
    nama = st.text_input("Masukkan Nama asli sayaangg", placeholder="Masukkan nama lengkap")
    password = st.text_input("Masukkan Password", type="password", placeholder="Masukkan password")
    login_button = st.button("Login")
    
    # Cek login
    if login_button:
        if nama.lower() == NAMA_PACAR.lower() and password == PASSWORD:
            st.success("Login berhasil! tekan lagiii tombol loginnyaaa")
            st.session_state["login_success"] = True
            st.session_state["halaman"] = 1
        else:
            st.error("Nama atau password salah. coba pake spasi sayaanggg. Silakan coba lagi.")

# Fungsi halaman video
def halaman_video():
    st.title("💖 FOR REMEMBER 💖")

    # Menampilkan video lokal
    st.video("love.mp4", start_time=0)
    
    # Teks tambahan
    st.markdown("""
    ## 🎥 FOR REMEMBER:
    Sayaangggkuuu,  
    Aku ingin kau tahu betapa besar cintaku padamu.  
    Setiap detik yang kuhabiskan bersamamu adalah momen paling berharga dalam hidupku.  
    Aku berjanji akan selalu ada untukmu, dalam suka maupun duka.  
    Aku mencintaimu lebih dari kata-kata yang bisa diungkapkan. I LOVE U ❤️  
    """)

    # Tombol Logout
    if st.button("Logout"):
        st.session_state["login_success"] = False
        st.session_state["halaman"] = 0

# Logika Multi-Halaman
if "halaman" not in st.session_state:
    st.session_state["halaman"] = 0

if st.session_state["halaman"] == 0:
    login()
elif st.session_state["halaman"] == 1 and st.session_state.get("login_success", False):
    halaman_video()
else:
    st.warning("Silakan login terlebih dahulu.")
    st.session_state["halaman"] = 0
    login()