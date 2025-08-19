# process_documents.py

import os
import shutil
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

# Load environment variables
load_dotenv()
OPENAI_API_KEY = "your_openai_api_key_here"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Initialize embedding model
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

def load_document(file_path):
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

    docs = loader.load()

    # Attach filename as the source
    for doc in docs:
        doc.metadata["source"] = os.path.basename(file_path)

    return docs

def process_documents(doc_dir='./data/documents/', db_dir='./data/chroma_db'):
    from langchain_community.document_loaders import (
        PyPDFLoader, TextLoader, UnstructuredMarkdownLoader, BSHTMLLoader
    )
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_openai import OpenAIEmbeddings
    from langchain_community.vectorstores import Chroma

    embeddings = OpenAIEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = []

    for root, _, files in os.walk(doc_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file.startswith('.'):
                continue  # Skip .DS_Store, etc.
            try:
                ext = os.path.splitext(file)[1].lower()
                if ext == '.pdf':
                    loader = PyPDFLoader(file_path)
                elif ext == '.txt':
                    loader = TextLoader(file_path)
                elif ext == '.md':
                    loader = UnstructuredMarkdownLoader(file_path)
                elif ext in ['.html', '.htm']:
                    loader = BSHTMLLoader(file_path)
                else:
                    print(f"Skipping unsupported file type: {file}")
                    continue

                docs = loader.load()
                for doc in docs:
                    doc.metadata['source'] = file  # ⬅️ Set source explicitly
                documents.extend(docs)
                print(f"Loaded: {file}")

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    if not documents:
        print("No valid documents found.")
        return None

    chunks = text_splitter.split_documents(documents)
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=db_dir
    )
    vectordb.persist()
    print(f"✅ Vector DB created with {len(chunks)} chunks from {len(documents)} docs.")
    return vectordb


if __name__ == "__main__":
    process_documents()
