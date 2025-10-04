"""
Main file organizer that combines text extraction, embedding generation,
and clustering to organize files by genre/topic.
"""

import os
import shutil
from pathlib import Path
from text_extractor import TextExtractor
from embedding_generator import EmbeddingGenerator
from clusterer import DocumentClusterer


class GenreBasedFileOrganizer:
    """AI-powered file organizer using NLP and clustering."""
    
    def __init__(self):
        """Initialize the file organizer."""
        self.text_extractor = TextExtractor()
        self.embedding_generator = None  # Lazy loading
        self.clusterer = None
        self.file_paths = []
        self.file_texts = []
        self.embeddings = None
        self.clusters = None
    
    def _load_models(self, progress_callback=None):
        """Load ML models (lazy loading to save resources)."""
        if self.embedding_generator is None:
            msg = "\n=== Loading AI Models ==="
            print(msg)
            if progress_callback:
                progress_callback(msg)
            
            self.embedding_generator = EmbeddingGenerator()
            self.clusterer = DocumentClusterer()
            
            msg = "=== Models Loaded ===\n"
            print(msg)
            if progress_callback:
                progress_callback(msg)
    
    def scan_directory(self, directory_path, progress_callback=None):
        """Scan directory for supported files.
        
        Args:
            directory_path: Path to directory to scan
            progress_callback: Optional callback for progress updates
            
        Returns:
            list: List of file paths found
        """
        directory_path = Path(directory_path)
        
        if not directory_path.exists():
            raise ValueError(f"Directory not found: {directory_path}")
        
        msg = f"\nScanning directory: {directory_path}"
        print(msg)
        if progress_callback:
            progress_callback(msg)
        
        files_found = []
        for file_path in directory_path.rglob('*'):
            if file_path.is_file() and self.text_extractor.is_supported(str(file_path)):
                files_found.append(str(file_path))
        
        msg = f"Found {len(files_found)} supported files"
        print(msg)
        if progress_callback:
            progress_callback(msg)
        
        return files_found
    
    def extract_texts(self, file_paths, progress_callback=None):
        """Extract text from all files.
        
        Args:
            file_paths: List of file paths
            progress_callback: Optional callback for progress updates
            
        Returns:
            list: List of extracted texts
        """
        msg = "\n=== Extracting Text ==="
        print(msg)
        if progress_callback:
            progress_callback(msg)
        
        texts = []
        
        for i, file_path in enumerate(file_paths):
            msg = f"Extracting ({i + 1}/{len(file_paths)}): {os.path.basename(file_path)}"
            print(msg)
            if progress_callback:
                progress_callback(msg)
            
            text = self.text_extractor.extract_text(file_path)
            texts.append(text)
        
        msg = f"Extracted text from {len(texts)} files\n"
        print(msg)
        if progress_callback:
            progress_callback(msg)
        
        return texts
    
    def generate_embeddings(self, texts, progress_callback=None):
        """Generate embeddings for texts.
        
        Args:
            texts: List of text strings
            progress_callback: Optional callback for progress updates
            
        Returns:
            np.ndarray: Array of embeddings
        """
        self._load_models(progress_callback)
        
        msg = "=== Generating Embeddings ==="
        print(msg)
        if progress_callback:
            progress_callback(msg)
        
        embeddings = self.embedding_generator.generate_embeddings_batch(texts)
        
        msg = f"Generated {len(embeddings)} embeddings\n"
        print(msg)
        if progress_callback:
            progress_callback(msg)
        
        return embeddings
    
    def cluster_files(self, embeddings, n_clusters=None, progress_callback=None):
        """Cluster files based on embeddings.
        
        Args:
            embeddings: Array of embedding vectors
            n_clusters: Number of clusters (None for auto)
            progress_callback: Optional callback for progress updates
            
        Returns:
            np.ndarray: Cluster labels
        """
        msg = "=== Clustering Files ==="
        print(msg)
        if progress_callback:
            progress_callback(msg)
        
        self.clusterer.build_index(embeddings)
        clusters = self.clusterer.cluster_documents(embeddings, n_clusters)
        
        if progress_callback:
            progress_callback("")
        print()
        
        return clusters
    
    def organize_files(self, source_dir, output_dir=None, n_clusters=None, copy_files=True, progress_callback=None):
        """Organize files from source directory into clustered folders.
        
        Args:
            source_dir: Source directory containing files to organize
            output_dir: Output directory for organized files (default: source_dir/organized)
            n_clusters: Number of clusters (None for auto-determination)
            copy_files: If True, copy files; if False, move files
            progress_callback: Optional callback for progress updates
            
        Returns:
            dict: Dictionary mapping cluster IDs to file lists
        """
        # Setup paths
        source_path = Path(source_dir)
        if output_dir is None:
            output_dir = source_path / "Sorted"
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True, parents=True)
        
        # Scan and extract
        self.file_paths = self.scan_directory(source_dir, progress_callback)
        
        if not self.file_paths:
            msg = "No supported files found!"
            print(msg)
            if progress_callback:
                progress_callback(msg)
            return {}
        
        self.file_texts = self.extract_texts(self.file_paths, progress_callback)
        
        # Generate embeddings and cluster
        self.embeddings = self.generate_embeddings(self.file_texts, progress_callback)
        self.clusters = self.cluster_files(self.embeddings, n_clusters, progress_callback)
        
        # Organize files into folders
        msg = "=== Organizing Files ==="
        print(msg)
        if progress_callback:
            progress_callback(msg)
        
        cluster_map = {}
        
        for file_path, cluster_id in zip(self.file_paths, self.clusters):
            # Create cluster folder
            cluster_folder = output_path / f"Cluster_{cluster_id}"
            cluster_folder.mkdir(exist_ok=True)
            
            # Copy or move file
            file_name = os.path.basename(file_path)
            dest_path = cluster_folder / file_name
            
            # Handle duplicate names
            counter = 1
            while dest_path.exists():
                name, ext = os.path.splitext(file_name)
                dest_path = cluster_folder / f"{name}_{counter}{ext}"
                counter += 1
            
            action = "Copied" if copy_files else "Moved"
            msg = f"{action}: {file_name} -> {cluster_folder.name}"
            
            if copy_files:
                shutil.copy2(file_path, dest_path)
            else:
                shutil.move(file_path, dest_path)
            
            print(msg)
            if progress_callback:
                progress_callback(msg)
            
            # Track cluster mapping
            if cluster_id not in cluster_map:
                cluster_map[cluster_id] = []
            cluster_map[cluster_id].append(file_name)
        
        msg = f"\n=== Organization Complete ==="
        print(msg)
        if progress_callback:
            progress_callback(msg)
        
        msg = f"Files organized into {len(cluster_map)} groups at: {output_path}"
        print(msg)
        if progress_callback:
            progress_callback(msg)
        
        # Print summary
        for cluster_id, files in sorted(cluster_map.items()):
            msg = f"\nCluster {cluster_id} ({len(files)} files):"
            print(msg)
            if progress_callback:
                progress_callback(msg)
            
            for file in files[:5]:  # Show first 5 files
                msg = f"  - {file}"
                print(msg)
                if progress_callback:
                    progress_callback(msg)
            
            if len(files) > 5:
                msg = f"  ... and {len(files) - 5} more"
                print(msg)
                if progress_callback:
                    progress_callback(msg)
        
        return cluster_map
    
    def find_similar_files(self, query_file, k=5):
        """Find files similar to the query file.
        
        Args:
            query_file: Path to query file
            k: Number of similar files to find
            
        Returns:
            list: List of (file_path, similarity_score) tuples
        """
        if self.embeddings is None:
            raise ValueError("No files have been organized yet. Run organize_files first.")
        
        # Extract and embed query file
        print(f"\nFinding files similar to: {query_file}")
        query_text = self.text_extractor.extract_text(query_file)
        query_embedding = self.embedding_generator.generate_embedding(query_text)
        
        # Find similar
        distances, indices = self.clusterer.find_similar(query_embedding, k)
        
        results = []
        for dist, idx in zip(distances, indices):
            results.append((self.file_paths[idx], float(dist)))
        
        print("\nSimilar files:")
        for file_path, score in results:
            print(f"  {os.path.basename(file_path)} (similarity: {score:.3f})")
        
        return results
