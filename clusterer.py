"""
Clustering module using FAISS for similarity-based grouping.
"""

import faiss
import numpy as np
from sklearn.cluster import KMeans


class DocumentClusterer:
    """Cluster documents based on their embeddings using FAISS."""
    
    def __init__(self, dimension=768):
        """Initialize the document clusterer.
        
        Args:
            dimension: Dimension of the embedding vectors (768 for DistilBERT)
        """
        self.dimension = dimension
        self.index = None
        self.clusters = None
        self.n_clusters = None
    
    def build_index(self, embeddings):
        """Build FAISS index for efficient similarity search.
        
        Args:
            embeddings: numpy array of embedding vectors (n_samples, dimension)
        """
        embeddings = embeddings.astype('float32')
        
        # Normalize embeddings for cosine similarity
        faiss.normalize_L2(embeddings)
        
        # Create FAISS index
        self.index = faiss.IndexFlatIP(self.dimension)  # Inner Product for cosine similarity
        self.index.add(embeddings)
        
        print(f"Built FAISS index with {self.index.ntotal} vectors")
    
    def cluster_documents(self, embeddings, n_clusters=None, auto_clusters=True):
        """Cluster documents based on their embeddings.
        
        Args:
            embeddings: numpy array of embedding vectors (n_samples, dimension)
            n_clusters: Number of clusters (if None, will be auto-determined)
            auto_clusters: Whether to automatically determine optimal clusters
            
        Returns:
            np.ndarray: Cluster labels for each document
        """
        n_samples = len(embeddings)
        
        # Auto-determine number of clusters if not specified
        if n_clusters is None and auto_clusters:
            # Use heuristic: sqrt(n/2) as a starting point
            n_clusters = max(2, min(int(np.sqrt(n_samples / 2)), 10))
            print(f"Auto-determined {n_clusters} clusters for {n_samples} documents")
        elif n_clusters is None:
            n_clusters = max(2, min(5, n_samples // 2))
        
        # Ensure we don't have more clusters than samples
        n_clusters = min(n_clusters, n_samples)
        
        self.n_clusters = n_clusters
        
        # Perform K-means clustering
        embeddings_normalized = embeddings.astype('float32')
        faiss.normalize_L2(embeddings_normalized)
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        self.clusters = kmeans.fit_predict(embeddings_normalized)
        
        print(f"Clustered {n_samples} documents into {n_clusters} groups")
        
        # Print cluster distribution
        unique, counts = np.unique(self.clusters, return_counts=True)
        for cluster_id, count in zip(unique, counts):
            print(f"  Cluster {cluster_id}: {count} documents")
        
        return self.clusters
    
    def find_similar(self, query_embedding, k=5):
        """Find k most similar documents to the query.
        
        Args:
            query_embedding: Query embedding vector
            k: Number of similar documents to retrieve
            
        Returns:
            tuple: (distances, indices) of similar documents
        """
        if self.index is None:
            raise ValueError("Index not built. Call build_index first.")
        
        query_embedding = query_embedding.astype('float32').reshape(1, -1)
        faiss.normalize_L2(query_embedding)
        
        distances, indices = self.index.search(query_embedding, k)
        
        return distances[0], indices[0]
    
    def get_cluster_label(self, idx):
        """Get cluster label for a document.
        
        Args:
            idx: Document index
            
        Returns:
            int: Cluster label
        """
        if self.clusters is None:
            raise ValueError("Clustering not performed. Call cluster_documents first.")
        
        return self.clusters[idx]
