import streamlit as st
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

st.set_page_config(page_title="Simple Audio App", layout="centered")
st.title("🎧 Simple Audio Uploader")

uploaded_file = st.file_uploader("Unggah file audio (.wav)", type=["wav"])

if uploaded_file is not None:
    # Baca audio
    y, sr = librosa.load(uploaded_file, sr=None)
    st.audio(uploaded_file, format="audio/wav")

    # Tampilkan waveform
    fig, ax = plt.subplots()
    librosa.display.waveshow(y, sr=sr, ax=ax)
    ax.set_title("Waveform Audio")
    st.pyplot(fig)

    # Simpan audio hasil (tidak diubah)
    sf.write("saved_output.wav", y, sr)
    with open("saved_output.wav", "rb") as f:
        st.download_button("📥 Download ulang audio", f, file_name="saved_output.wav")
