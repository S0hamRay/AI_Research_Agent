# Personal Knowledge Base Assistant - RAG System

A sophisticated **Retrieval Augmented Generation (RAG)** system that transforms your personal documents into an intelligent, queryable knowledge base using cutting-edge AI technologies.

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

### 1. Document Ingestion
- Documents are loaded and processed using appropriate loaders
- Text is split into manageable chunks using RecursiveCharacterTextSplitter
- OpenAI embeddings convert text chunks into vector representations

### 2. Vector Storage
- Chunks are stored in Chroma vector database
- Each chunk maintains metadata about its source document
- Similarity search enables semantic retrieval

### 3. Query Processing
- User queries are converted to embeddings
- Similar chunks are retrieved from the vector database
- OpenAI language models generate contextual responses
- Sources are provided for transparency

## 🎯 Use Cases

- **Research Assistant**: Query your research papers and documents
- **Knowledge Management**: Organize and access personal knowledge
- **Email Automation**: Automated responses based on your documents
- **Learning Tool**: Study and review your materials interactively

## 🔐 Security & Privacy

- **Local Processing**: Documents are processed locally
- **API Key Management**: Secure handling of OpenAI API keys
- **Gmail OAuth**: Secure email authentication
- **No Data Sharing**: Your documents stay private

## 🚧 Limitations

- Requires OpenAI API credits for embeddings and responses
- Gmail API setup required for email functionality
- Document processing limited to supported file types
- Vector database size depends on document volume

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

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Check the documentation
- Review the code examples

---

**Built with ❤️ using modern AI technologies for intelligent document management and retrieval.**
