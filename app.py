import streamlit as st
from PyPDF2 import PdfReader
from gtts import gTTS
import tempfile

st.title("📄 PDF to Audio Converter")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    # Save temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content

    if text:
        tts = gTTS(text=text, lang='en')
        audio_path = "output.mp3"
        tts.save(audio_path)

        st.success("✅ Conversion done!")
        st.audio(audio_path)
    else:
        st.error("❌ No readable text found")