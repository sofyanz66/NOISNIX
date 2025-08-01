import streamlit as st
import soundfile as sf
import tempfile

st.set_page_config(page_title="Noisnix Lite", layout="centered")
st.title("🔊 Noisnix - Audio Upload & Playback")

st.markdown("Upload audio `.wav`, putar, dan unduh ulang.")

uploaded_file = st.file_uploader("Unggah file audio (.wav)", type=["wav"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    # Simpan ulang di file sementara
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
        tmpfile.write(uploaded_file.read())
        tmpfile_path = tmpfile.name

    # Tombol unduh ulang
    with open(tmpfile_path, "rb") as f:
        st.download_button("📥 Download ulang audio", f, file_name="download.wav")
