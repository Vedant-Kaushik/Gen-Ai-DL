import streamlit as st
import os
import tempfile
import sys
sys.path.append('webpagereader')

# Import everything from your existing pdfquestion.py
from pdfquestion import (
    model, 
    prompt_summary, 
    prompt_mcq, 
    prompt_qa, 
    StrOutputParser, 
    RunnableSequence, 
    RunnableParallel,
    PyPDFLoader,
    parser
)

# Page config
st.set_page_config(
    page_title="PDF Question Generator",
    layout="wide"
)

# Simple CSS for black output background
st.markdown("""
<style>
    .black-bg {
        background-color: black;
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        white-space: pre-wrap;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("PDF Question Generator")
st.write("Upload a PDF and get summary, MCQs, or ask questions!")

# Sidebar for options
st.sidebar.header("Options")

# Feature selection
st.sidebar.write("What do you want to do?")
summary_option = st.sidebar.checkbox("Summary", value=True)
mcq_option = st.sidebar.checkbox("MCQ Generation")
qa_option = st.sidebar.checkbox("Q&A")

# File upload
st.header("Upload PDF")
uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])

# Question input for Q&A
question = ""
if qa_option:
    st.header("Ask a Question")
    question = st.text_area("Enter your question:", placeholder="What do you want to know about the PDF?")

# Process button
if st.button("Process PDF", type="primary"):
    if uploaded_file is not None:
        # Show processing message
        with st.spinner("Processing PDF..."):
            
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.getvalue())
                tmp_path = tmp.name
            
            try:
                # Use your PyPDFLoader
                loader = PyPDFLoader(tmp_path)
                docs = loader.load()
                text = docs[0].page_content
            finally:
                os.remove(tmp_path)
            
            # Use your existing parser
            # parser = StrOutputParser()  # Already imported from your file
            
            # Process based on selected options using your existing chains
            if summary_option:
                st.subheader("Summary")
                summary_chain = RunnableSequence(prompt_summary, model, parser)
                summary_result = summary_chain.invoke({"text": text, "question": "Summarize the document."})
                st.markdown(f'<div class="black-bg">{summary_result}</div>', unsafe_allow_html=True)
            
            if mcq_option:
                st.subheader(" MCQ Questions")
                mcq_chain = RunnableSequence(prompt_mcq, model, parser)
                mcq_result = mcq_chain.invoke({"text": text, "question": "Generate MCQs."})
                st.markdown(f'<div class="black-bg">{mcq_result}</div>', unsafe_allow_html=True)
            
            if qa_option and question:
                st.subheader("Q&A Answer")
                qa_chain = RunnableSequence(prompt_qa, model, parser)
                qa_result = qa_chain.invoke({"text": text, "question": question})
                st.markdown(f'<div class="black-bg">{qa_result}</div>', unsafe_allow_html=True)
            
            st.success(" Processing complete!")
            
    else:
        st.error("Please upload a PDF file first!")

# Footer
