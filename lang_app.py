import os
import openai
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chat_models import ChatOpenAI
import pinecone

# Initialize OpenAI and Pinecone
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")
pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment='asia-southeast1-gcp-free')

# Load and process the PDF file
pdf_file_path = '/home/adriperse/Desktop/repos/Chainlit_qa/data/the-big-book-of-mlops-final-062722.pdf'
loader = PyPDFLoader(pdf_file_path)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
documents = loader.load()
docs = text_splitter.split_documents(documents)

# Create a Pinecone index from the documents
embeddings = OpenAIEmbeddings()
index_name = 'pdfdoc'
docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)

# Set up a retrieval question-answering chain with the Pinecone index
chain = RetrievalQAWithSourcesChain.from_chain_type(ChatOpenAI(temperature=0, streaming=True), chain_type='stuff', retriever=docsearch.as_retriever(max_tokens_limit=4097))

# Function to handle user input and generate response
def handle_input(user_input):
    # Process the user's input with the chain
    res = chain(user_input)
    answer = res['answer']
    sources = res['sources'].strip()

    # Only return the answer if it's related to the PDF content
    if sources:
        return answer
    else:
        return "I'm sorry, but I can only answer questions related to the content of the PDF."

# Example usage
while True:
    user_input = input('Ask a question: ')
    print(handle_input(user_input))
