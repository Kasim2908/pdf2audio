import streamlit as st
from PyPDF2 import PdfReader
from gtts import gTTS
import tempfile


st.set_page_config(page_title="PDF to Audio", page_icon="🎧", layout="centered")
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #ffffff;
}
.subtitle {
    text-align: center;
    color: #cfcfcf;
    margin-bottom: 30px;
}
.card {
    padding: 25px;
    border-radius: 20px;
    background: #1e1e2f;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.6);
}
.small-text {
    color: #aaa;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# Title Section
st.markdown('<div class="title">📄 → 🎧 PDF to Audio</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Convert documents into natural speech in seconds</div>', unsafe_allow_html=True)

# Card Container
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # Upload
    uploaded_file = st.file_uploader("📤 Upload your PDF", type="pdf")

    # Options
    col1, col2 = st.columns(2)

    with col1:
        language = st.selectbox("🌍 Language", ["en", "hi", "fr", "de"])

    with col2:
        speed = st.selectbox("⚡ Speech Speed", ["Normal", "Slow"])

    slow = True if speed == "Slow" else False

    # Process
    if uploaded_file is not None:
        st.markdown(f"<div class='small-text'>📄 File: {uploaded_file.name}</div>", unsafe_allow_html=True)

        with st.spinner("🔄 Converting your PDF into audio..."):
            # Save temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                pdf_path = tmp_file.name

            reader = PdfReader(pdf_path)
            text = ""

            progress = st.progress(0)

            for i, page in enumerate(reader.pages):
                content = page.extract_text()
                if content:
                    text += content
                progress.progress((i + 1) / len(reader.pages))

            if text:
                tts = gTTS(text=text, lang=language, slow=slow)
                audio_path = "output.mp3"
                tts.save(audio_path)

                st.success("✅ Conversion Completed!")

                st.markdown("### 🎧 Listen to your audio")
                st.audio(audio_path)

                with open(audio_path, "rb") as f:
                    st.download_button("⬇️ Download Audio", f, file_name="output.mp3")

            else:
                st.error("❌ No readable text found in PDF")

    st.markdown('</div>', unsafe_allow_html=True)