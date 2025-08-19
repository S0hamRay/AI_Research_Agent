from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma


def create_qa_chain(db_dir='./data/chroma_db'):
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=db_dir, embedding_function=embeddings)

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain


def query_knowledge_base(query, qa_chain):
    result = qa_chain.invoke({"query": query})

    answer = result["result"]
    sources = list({doc.metadata.get("source", "unknown") for doc in result["source_documents"]})

    return {
        "answer": answer,
        "sources": sources
    }
