import pytest
from unittest.mock import patch, MagicMock, mock_open
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from build_index import get_knowledge_text, create_vector_db, get_embedding, add_document

def test_get_knowledge_text():
    mock_content = "This is some knowledge."
    with patch("builtins.open", mock_open(read_data=mock_content)) as mock_file:
        content = get_knowledge_text("dummy_path.txt")
        assert content == mock_content
        mock_file.assert_called_once_with("dummy_path.txt", "r")

def test_create_vector_db():
    with patch("chromadb.PersistentClient") as mock_client:
        mock_collection = MagicMock()
        mock_client.return_value.get_or_create_collection.return_value = mock_collection
        
        collection = create_vector_db("dummy_path")
        
        mock_client.assert_called_once_with(path="dummy_path")
        mock_client.return_value.get_or_create_collection.assert_called_once_with("knowledge_base")
        assert collection == mock_collection

def test_get_embedding():
    mock_response = {'embedding': [0.1, 0.2, 0.3]}
    with patch("ollama.embeddings", return_value=mock_response) as mock_ollama:
        text = "test text"
        embedding = get_embedding(text)
        
        mock_ollama.assert_called_once_with(model='nomic-embed-text', prompt=text)
        assert embedding == [0.1, 0.2, 0.3]

def test_add_document():
    mock_collection = MagicMock()
    text = "test text"
    embedding = [0.1, 0.2, 0.3]
    
    add_document(mock_collection, text, embedding)
    
    mock_collection.add.assert_called_once_with(
        documents=[text],
        embeddings=[embedding],
        ids=["doc1"]
    )
