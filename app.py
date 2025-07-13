import streamlit as st
from summarizer import summarize_text
from pdf_extractor import extract_text_from_pdf
from text_cleaner import  clean_text
from QA_chatbot import ask_question
import base64

# Set page title and icon
st.set_page_config(
    page_title="Smart Assistant for Research Summarization",
    page_icon=":book:",  # Emoji icon or you can use an image path
    layout="centered"  # Optional: can be "centered" or "wide"
)

# Function to load and encode the logo
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to the logo
logo_path = "logo.png"
logo_base64 = get_base64_of_bin_file(logo_path)

# Custom CSS
# ✅ Your Custom CSS with text input label and input box styling
st.markdown(f"""
    <style>
        .main {{
            background-color: #003300; /* Dark Green */
            color: #f0f0f0; /* Light text for contrast */
        }}

        .stTextInput > div > div > input {{
            border: 2px solid #66b2ff; /* Light Blue border for input */
            background-color: #004d00; /* Slightly lighter input BG */
            color: #ffffff; /* White text */
        }}

        /* === Style text input label === */
        label {{
            color: #66b2ff !important;
            font-weight: bold;
        }}

        /* === Style generic text input box === */
        input[type="text"] {{
            background-color: #004d00 !important;
            color: #ffffff !important;
            border: 2px solid #66b2ff !important;
        }}

        .stButton>button {{
            background-color: #66b2ff; /* Light Blue button */
            color: #003300; /* Dark Green text for contrast */
            border-radius: 6px;
            border: none;
            padding: 8px 16px;
            font-weight: bold;
            transition: 0.3s;
        }}
        .stButton>button:hover {{
            background-color: #3399ff; /* Brighter Blue on hover */
            color: #ffffff;
        }}
        .header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #66b2ff; /* Light Blue Header */
            padding: 12px;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            color: #003300; /* Dark Green text for header */
            font-weight: bold;
            font-size: 20px;
        }}
        .logo {{
            width: 120px;
        }}
    </style>
""", unsafe_allow_html=True)

# App title with logo
st.markdown(f"""
    <div class="header">
        <h2>Smart Assistant for Research Summarization</h2>
        <img src="data:image/png;base64,{logo_base64}" class="logo">
    </div>
    <hr>
""", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    raw_text = extract_text_from_pdf(uploaded_file)
    cleaned_text = clean_text(raw_text)
    
    # Display extracted text
    st.markdown(
    "<h3 style='color: #66b2ff;'>Extracted Text</h3>",
    unsafe_allow_html=True
    )
    st.text_area("Extracted Text", cleaned_text, height=300)
    
    # Summarization section
    if st.button("Summarize"):
      summary = summarize_text(cleaned_text)

      st.markdown(
        "<h3 style='color: #66b2ff;'>Summary</h3>",
        unsafe_allow_html=True
      )
      st.markdown(
        f"<div style='background-color: #004d00; color: #ffffff; padding: 15px; border-radius: 8px;'>{summary}</div>",
        unsafe_allow_html=True
      )


    
    # Q&A section
    st.markdown(
    "<h3 style='color: #66b2ff;'>Ask Questions About the PDF</h3>",
    unsafe_allow_html=True
)

    question = st.text_input("Enter your question:")
    if question:
       answer = ask_question(question, cleaned_text)
       st.markdown(
        "<h3 style='color: #66b2ff;'>Answer</h3>",
        unsafe_allow_html=True
       )
       st.markdown(
        f"<div style='background-color: #004d00; color: #ffffff; padding: 15px; border-radius: 8px;'>{answer}</div>",
        unsafe_allow_html=True
       )

 