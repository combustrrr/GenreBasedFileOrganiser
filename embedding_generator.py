"""
Text embedding module using DistilBERT for semantic understanding.
"""

from transformers import DistilBertTokenizer, DistilBertModel
import torch
import numpy as np


class EmbeddingGenerator:
    """Generate text embeddings using DistilBERT."""
    
    def __init__(self, model_name='distilbert-base-uncased'):
        """Initialize the embedding generator with DistilBERT.
        
        Args:
            model_name: Name of the DistilBERT model to use
        """
        print(f"Loading {model_name} model...")
        self.tokenizer = DistilBertTokenizer.from_pretrained(model_name)
        self.model = DistilBertModel.from_pretrained(model_name)
        self.model.eval()  # Set to evaluation mode
        
        # Use GPU if available
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
        print(f"Model loaded on {self.device}")
    
    def generate_embedding(self, text, max_length=512):
        """Generate embedding for the given text.
        
        Args:
            text: Input text to embed
            max_length: Maximum sequence length for tokenization
            
        Returns:
            np.ndarray: Embedding vector
        """
        if not text or not text.strip():
            # Return zero vector for empty text
            return np.zeros(768)  # DistilBERT hidden size is 768
        
        # Truncate text if too long (preserve first part as it's usually most relevant)
        if len(text) > max_length * 10:  # Rough character estimate
            text = text[:max_length * 10]
        
        # Tokenize and encode the text
        inputs = self.tokenizer(
            text,
            return_tensors='pt',
            max_length=max_length,
            truncation=True,
            padding=True
        )
        
        # Move inputs to device
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        # Generate embeddings
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Use the [CLS] token embedding (first token) as document representation
        embedding = outputs.last_hidden_state[:, 0, :].cpu().numpy()[0]
        
        return embedding
    
    def generate_embeddings_batch(self, texts, max_length=512):
        """Generate embeddings for multiple texts.
        
        Args:
            texts: List of input texts
            max_length: Maximum sequence length for tokenization
            
        Returns:
            np.ndarray: Array of embedding vectors
        """
        embeddings = []
        
        for i, text in enumerate(texts):
            if (i + 1) % 10 == 0:
                print(f"Processing {i + 1}/{len(texts)} documents...")
            embedding = self.generate_embedding(text, max_length)
            embeddings.append(embedding)
        
        return np.array(embeddings)
