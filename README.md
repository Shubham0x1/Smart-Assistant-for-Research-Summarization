# 📚 Smart Assistant for Research Summarization

## Overview

This project is a web application that enables users to upload PDF documents, extract and summarize their text content, and interact with a Q&A chatbot to get answers related to the document. The application leverages advanced models for text summarization and question-answering to provide valuable insights and answers.

## Features

- **PDF Upload**: Upload PDF files for processing.
- **Text Extraction**: Extract and clean text from the uploaded PDF.
- **Text Summarization**: Generate concise summaries of the extracted text.
- **Q&A Chatbot**: Ask questions related to the PDF content and receive relevant answers.
- **User-Friendly UI**: Clean and interactive interface with logo integration.

## Technologies

- **Streamlit**: Framework for building the web application.
- **Hugging Face Transformers**: For text summarization and question-answering models.
- **PyPDF2**: For extracting text from PDF files.
- **Python**: Programming language used for development.

## 📂 Project Structure
```plaintext
Smart-Assistant-for-Research-Summarization/
│
├── app.py                 # Streamlit main app
├── summarizer.py          # T5-based summarization logic
├── pdf_extractor.py       # PDF text extraction logic
├── text_cleaner.py        # Text cleaning utilities
├── QA_chatbot.py          # Q&A logic
├── logo.png               # App logo
├── requirements.txt       # Python dependencies
└── .gitignore             # Ignore venv & cache files
```
### 🧰 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-github-repo-url>
cd <repo-directory>
```
### 2. Create a virtual environment (recommended):
````
python -m venv venv
````

### 3. Activate the virtual environment:
````
venv\Scripts\activate
````

### 4. Install the required packages:
````
pip install -r requirements.txt
````

## Configuration

### 1. Update app.py:

Make sure the path to the logo image and any other local paths are correctly set in the app.py file.

### 2. Set up your models:

Ensure that the models used in QA_chatbot.py are properly downloaded and accessible.

## Usage

### 1. Run the application:
````
streamlit run app.py
````

### 2. Interact with the application:

Upload PDF: Click the "Upload a PDF file" button to upload your PDF document.
Summarize: Click the "Summarize" button to get a summary of the extracted text.
Ask Questions: Enter your question in the text input field to get answers based on the PDF content.

### Screenshots
Below is a snapshot of the **Smart Assistant for Research Summarization** web app running on Streamlit.  
It shows the clean, modern interface for uploading a PDF file to generate summaries and answer questions.

![Screenshot 2025-07-13 225211.png](https://github.com/Shubham0x1/Smart-Assistant-for-Research-Summarization/blob/main/Screenshot%202025-07-13%20225211.png)

## 📝 PDF Upload and Extracted Text View

This screenshot shows the **Smart Assistant for Research Summarization** app with a PDF file uploaded  
and its extracted text displayed. Users can then summarize the text or ask questions about its content.

![Screenshot 2025-07-13 225737.png](https://github.com/Shubham0x1/Smart-Assistant-for-Research-Summarization/blob/main/Screenshot%202025-07-13%20225737.png)

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code adheres to the project’s coding standards and includes tests where applicable.

### License

This project is licensed under the MIT License. 
### Acknowledgements

Hugging Face: For providing powerful NLP models.
Streamlit: For making it easy to build interactive web applications.

