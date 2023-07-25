# Language Processing Application

  This repository contains two Python scripts
`lang_app.py` & `chainlit_app.py`,
which are used for language processing and document retrieval.


![Project Image](./data/DALL·E.png)

## Important Note

Before starting, it's recommended to create a new environment (like using Conda) to avoid any package conflicts and to keep your workspace clean.

## lang_app.py

This script is a language processing application that uses OpenAI and Pinecone to process a PDF file and create a Pinecone index from the documents. It sets up a retrieval question-answering chain with the Pinecone index and provides a function to handle user input and generate responses.

To use this script, you need to have the following environment variables set:

- `OPENAI_KEY`: Your OpenAI API key.
- `PINECONE_API_KEY`: Your Pinecone API key.

The script will load and process a PDF file located at the path specified in the `pdf_file_path` variable. It will then create a Pinecone index from the documents and set up a retrieval question-answering chain with the Pinecone index.

The `handle_input(user_input)` function processes the user's input with the chain and returns the answer if it's related to the PDF content.

## chainlit_app.py

This script uses the Chainlit library to create a web application that can process text and PDF files and answer questions about the content of the files.

To use this script, you need to have the following environment variables set:

- `OPENAI_KEY`: Your OpenAI API key.
- `PINECONE_API_KEY`: Your Pinecone API key.

The script will process the file uploaded by the user and create a Pinecone index from the documents. It will then set up a retrieval question-answering chain with the Pinecone index.

The `start()` function is called when a chat starts. It asks the user to upload a file and processes the file. The `main(message)` function is called when a message is received. It retrieves the chain from the user session and processes the message with the chain.

# Requirements

- Python 3.11
- OpenAI
- Pinecone
- Chainlit

# Installation

1. Clone this repository.
2. Install the required packages with `pip install -r requirements.txt`.
3. Set the `OPENAI_KEY` and `PINECONE_API_KEY` environment variables.
4. Run `python lang_app.py` or `chainlit run chainlit_app.py` to start the application.

# Usage

For `lang_app.py`, the application will prompt you to ask a question about the content of the PDF file.

For `chainlit_app.py`, you can start a chat and upload a file. The application will process the file and you can ask questions about the content of the file.


# Please note that you may need to adjust the paths and environment variables according to your setup.

---

# For more information about the Chainlit library used in this project, please visit [Chainlit's official documentation](https://docs.chainlit.io/overview) or their [GitHub repository](https://github.com/chainlit/chainlit).
