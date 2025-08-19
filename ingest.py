import os
from langchain_community.document_loaders import (
    PyPDFLoader, 
    TextLoader, 
    UnstructuredMarkdownLoader,
    BSHTMLLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import shutil




# Load environment variables

OPENAI_API_KEY="your_openai_api_key_here"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
load_dotenv()


# Initialize embedding model
embeddings = OpenAIEmbeddings(openai_api_key = OPENAI_API_KEY)

# Configure text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

def load_document(file_path):
    """Load document based on file extension"""
    _, extension = os.path.splitext(file_path)
    
    if extension == '.pdf':
        loader = PyPDFLoader(file_path)
    elif extension == '.txt':
        loader = TextLoader(file_path)
    elif extension == '.md':
        loader = UnstructuredMarkdownLoader(file_path)
    elif extension in ['.html', '.htm']:
        loader = BSHTMLLoader(file_path)
    else:
        raise ValueError(f"Unsupported file extension: {extension}")
    
    return loader.load()

def process_documents(doc_dir='./data/documents/', db_dir='./data/chroma_db'):
    """Process all documents in the directory and create a vector database"""
    documents = []
    
    # Iterate through all files in the document directory
    for root, _, files in os.walk(doc_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                doc = load_document(file_path)
                documents.extend(doc)
                print(f"Processed: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    # Split documents into chunks
    if documents:
        chunks = text_splitter.split_documents(documents)
        
        # Create or update vector database
        vectordb = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=db_dir
        )
        
        # Persist the database
        vectordb.persist()
        print(f"Vector database created with {len(chunks)} chunks.")
        return vectordb
    else:
        print("No documents were processed.")
        return None

if __name__ == "__main__":
    process_documents()