import os
from ingest import process_documents
from query import create_qa_chain, query_knowledge_base

OPENAI_API_KEY="completely_legitimate_api_key"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
def main():
    # Check if database exists, if not create it
    db_dir = './data/chroma_db'
    
    if not os.path.exists(db_dir):
        print("No existing database found. Processing documents...")
        process_documents()
    
    # Create QA chain once
    qa_chain = create_qa_chain()
    
    print("Welcome to your Personal Knowledge Base Assistant!")
    print("Type 'exit' to quit or 'refresh' to update the knowledge base.")
    
    while True:
        user_input = input("\nAsk a question: ")
        
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'refresh':
            print("Refreshing knowledge base...")
            process_documents()
            qa_chain = create_qa_chain()
            print("Knowledge base refreshed!")
        else:
            print("\nSearching your knowledge base...")
            result = query_knowledge_base(user_input, qa_chain)
            
            print("\nAnswer:", result["answer"])
            
            # Print sources if available
            if result["sources"]:
                print("\nSources:")
                for i, source in enumerate(result["sources"], 1):
                    if 'source' in source:
                        print(f"{i}. {source['source']}")

if __name__ == "__main__":
    main()