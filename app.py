import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import io

st.title("PDF to Word Converter")
st.write("Upload a PDF file and convert it to a Word document")

# File upload
upload_file = st.file_uploader("Choose a PDF file", type=['pdf'])

if upload_file is not None:
    # Read the PDF
    reader = PdfReader(upload_file)
    st.write("PDF file loaded successfully")

    # Display the number of pages
    st.write(f"Number of pages: {len(reader.pages)}")

    # Create a Word document
    doc = Document()
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()
        doc.add_paragraph(text)

    # Save the Word document to an in-memory file
    word_io = io.BytesIO()
    doc.save(word_io)
    word_io.seek(0)

    # Download button for the Word document
    st.download_button(
        label="Download Word Document",
        data=word_io,
        file_name="converted.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
