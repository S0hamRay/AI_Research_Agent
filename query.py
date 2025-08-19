from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

OPENAI_API_KEY="completely_legitimate_api_key"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def create_qa_chain(db_dir='./data/chroma_db'):
    """Create a question-answering chain with the vector database"""
    # Load the persisted database
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=db_dir, embedding_function=embeddings)
    
    # Create retriever
    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )
    
    # Create custom prompt template
    template = """You are a helpful assistant that answers questions based on the user's personal knowledge base.
    Use only the following context to answer the question. If you don't know the answer, say you don't know.
    
    Context: {context}
    
    Question: {question}
    
    Answer:"""
    
    PROMPT = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )
    
    # Initialize the language model
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    
    # Create the QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )
    
    return qa_chain

def query_knowledge_base(query, qa_chain=None, db_dir='./data/chroma_db'):
    """Query the knowledge base"""
    if qa_chain is None:
        qa_chain = create_qa_chain(db_dir)
    
    result = qa_chain({"query": query})
    
    return {
        "answer": result["result"],
        "sources": [doc.metadata for doc in result["source_documents"]]
    }