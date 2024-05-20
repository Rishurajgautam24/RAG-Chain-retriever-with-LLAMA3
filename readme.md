# PDF Query Application

This project is a Streamlit application that allows users to upload a PDF and query its contents using a language model. The application splits the PDF into manageable chunks, embeds the text for efficient retrieval, and uses a language model to answer user queries based on the context provided.

## Features

- **Upload PDF**: Users can upload a PDF file.
- **Text Splitting**: The PDF content is split into chunks for better processing.
- **Embedding and Retrieval**: Text chunks are embedded using a language model for efficient retrieval.
- **Question Answering**: Users can ask questions about the content of the PDF, and the application provides answers based on the context.

## Installation

To run this application, you'll need to have Python installed. Follow these steps to set up the project:

1. Clone the repository:
    ```sh
    git clone https://github.com/Rishurajgautam24/RAG-Chain-retriever-with-LLAMA3.git
    cd RAG-Chain-retriever-with-LLAMA3
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your Langchain API key:
    ```env
    LANGCHAIN_API_KEY=your_api_key_here
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and navigate to the local Streamlit server URL (usually `http://localhost:8501`).

3. Upload a PDF file using the file uploader.

4. Enter your question in the text input box and click "Get Answer".

# *Dependencies*
`streamlit`
`langchain_community`
`langchain`
`dotenv`

Make sure to install all the dependencies listed in `requirements.txt`.

