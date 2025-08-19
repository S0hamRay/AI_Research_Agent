#!/usr/bin/env python3
"""
Demo script for the Personal Knowledge Base Assistant
This script demonstrates the basic functionality of the RAG system
"""

import os
import sys
from pathlib import Path

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def create_sample_document():
    """Create a sample document for testing"""
    sample_content = """
# Sample Research Document

## Introduction
This is a sample research document to demonstrate the RAG system's capabilities.

## Key Concepts
- Retrieval Augmented Generation (RAG)
- Vector databases for semantic search
- OpenAI embeddings for text understanding
- LangChain for AI chain orchestration

## Methodology
The system processes documents by:
1. Loading and parsing various file formats
2. Splitting text into manageable chunks
3. Converting chunks to vector embeddings
4. Storing in a vector database for retrieval

## Results
The RAG system successfully demonstrates:
- Document processing and ingestion
- Semantic search capabilities
- Contextual question answering
- Source attribution and transparency

## Conclusion
This sample document shows how the system can handle structured research content and provide intelligent responses based on the stored knowledge.
"""
    
    # Create documents directory if it doesn't exist
    docs_dir = Path("./data/documents")
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    # Write sample document
    sample_file = docs_dir / "sample_research.md"
    with open(sample_file, "w") as f:
        f.write(sample_content)
    
    print(f"✅ Created sample document: {sample_file}")
    return str(sample_file)

def run_demo():
    """Run the demo with sample data"""
    print("🚀 Personal Knowledge Base Assistant - Demo Mode")
    print("=" * 50)
    
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY not set")
        print("   Please set your OpenAI API key to test the full functionality")
        print("   export OPENAI_API_KEY='your-key-here'")
        print()
    
    # Create sample document
    sample_file = create_sample_document()
    
    print("\n📚 Sample document created successfully!")
    print(f"   File: {sample_file}")
    
    print("\n🔧 To test the system:")
    print("   1. Set your OpenAI API key:")
    print("      export OPENAI_API_KEY='your-key-here'")
    print("   2. Run the terminal interface:")
    print("      python app.py")
    print("   3. Ask questions about the sample document")
    print("   4. Try commands like 'refresh' and 'exit'")
    
    print("\n📧 To test email functionality:")
    print("   1. Set up Gmail API credentials")
    print("   2. Run the email interface:")
    print("      python app2.py")
    
    print("\n🎯 Sample questions to try:")
    print("   - What is RAG?")
    print("   - How does the system process documents?")
    print("   - What are the key concepts discussed?")
    print("   - What methodology is used?")
    
    print("\n✨ Demo setup complete! Happy testing!")

if __name__ == "__main__":
    run_demo()
