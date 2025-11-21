# GenAI RAG Engine

A modular Retrieval-Augmented Generation (RAG) engine for building enterprise AI assistants.

## About

GenAI RAG Engine is designed to simplify the creation of advanced AI applications. It supports the entire RAG pipeline, from document ingestion to answer generation, providing an extensible architecture for chatbots, knowledge bases, and AI copilots.

## Features

- **Document Ingestion**: Seamlessly import data from various sources.
- **Chunking**: Intelligent text splitting for optimal retrieval.
- **Embeddings**: Integration with state-of-the-art embedding models.
- **Vector Search**: Efficient similarity search for relevant context.
- **LLM-Based Answer Generation**: Generate accurate responses using Large Language Models.
- **Evaluation Tools**: Built-in metrics to assess performance.
- **Extensible Architecture**: Easy to customize and extend for specific use cases.

## Getting Started

> [!NOTE]
> This project is currently under active development.

### Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/) (for embeddings)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sankarbaseone/genai-rag-engine.git
   cd genai-rag-engine
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory (if needed).

## Usage

### Build the Index

To process the knowledge base and create the vector store:

```bash
python build_index.py
```

This will read `data/knowledge.txt`, generate embeddings using Ollama, and store them in `vector_store`.

### Running Tests

To run the unit tests:

```bash
pytest
```

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).