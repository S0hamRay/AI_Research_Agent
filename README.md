# Personal Knowledge Base Assistant - RAG System

A sophisticated **Retrieval Augmented Generation (RAG)** system that transforms your personal documents into an intelligent, queryable knowledge base using cutting-edge AI technologies (a.k.a. calling the ChatGPT API 👍).

This was inspired by a retrieval-augmented generation project via Llama I came across on GitHub a while ago, will link it here as soon as I can find it again

The email functionality is rudimentary and currently just for proof of concept. This was initially intended to run solely in the terminal because quickly accessing information from different research papers constitutes most of my use case for this project.

## 🚀 Features

- **Document Processing**: Automatically processes PDFs, text files, markdown, and HTML documents
- **Vector Database**: Uses Chroma vector database with OpenAI embeddings for semantic search
- **Dual Interface**: 
  - Terminal-based interactive assistant
  - Email-based automated response system
- **Real-time Updates**: Refresh knowledge base on-the-fly
- **Source Attribution**: Always know where information comes from

## 🏗️ Architecture

This project implements a modern **agentic AI** architecture using:

- **LangChain**: For building and orchestrating AI chains
- **OpenAI API**: For embeddings and language model interactions
- **Chroma Vector Database**: For efficient document storage and retrieval
- **Sentence Transformers**: For advanced text processing

## 🔧 Technologies Used

- **Python 3.8+**
- **LangChain Framework** - Core RAG orchestration
- **OpenAI GPT Models** - Language understanding and generation
- **Chroma Vector Database** - Document storage and similarity search
- **Sentence Transformers** - Text embedding generation
- **Gmail API** - Email integration for automated responses

## 📁 Project Structure

```
RAGStuff/
├── app.py              # Terminal-based RAG interface
├── app2.py             # Email-based RAG interface  
├── ingest.py           # Document processing and ingestion
├── ingest2.py          # Enhanced document processing
├── query.py            # Query processing and retrieval
├── query2.py           # Streamlined query processing
├── data/
│   ├── documents/      # Your personal documents
│   └── chroma_db/      # Vector database storage
├── credentials2.json   # Gmail API credentials
└── token.pickle        # Gmail authentication token
```

## 🚀 Quick Start

### Prerequisites

1. **Python Environment**: Ensure you have Python 3.8+ installed
2. **OpenAI API Key**: Get your API key from [OpenAI Platform](https://platform.openai.com/)
3. **Gmail API** (for email functionality): Set up OAuth2 credentials

### Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd RAGStuff
   ```

2. **Install dependencies**:
   ```bash
   pip install langchain langchain-openai langchain-community chromadb sentence-transformers python-dotenv google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

3. **Set up your OpenAI API key**:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

4. **Add your documents** to the `data/documents/` folder

### Usage

#### Terminal Interface
```bash
python app.py
```
- Interactive Q&A with your knowledge base
- Type 'refresh' to update the database
- Type 'exit' to quit

#### Email Interface
```bash
python app2.py
```
- Automatically processes emails and responds using your knowledge base
- Requires Gmail API setup

## 🔍 How It Works

Document Ingestion => Vector Storage => Query Processing


## 🎯 Use Cases

- **Research Assistant**: Query your research papers and documents
- **Knowledge Management**: Organize and access personal knowledge
- **Email Automation**: Automated responses based on your documents
- **Learning Tool**: Study and review your materials interactively


## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:

- Bug fixes
- Feature enhancements
- Documentation improvements
- Performance optimizations

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **OpenAI** for providing the language models and embeddings
- **LangChain** team for the excellent framework
- **Chroma** for the vector database solution
- **Google** for the Gmail API

---

**Built with ❤️ using modern AI technologies for intelligent document management and retrieval.**
