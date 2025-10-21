#!/usr/bin/env python3
"""
Example usage of the Genre-Based File Organizer.
"""

from file_organizer import GenreBasedFileOrganizer
import os


def example_basic_usage():
    """Basic example of organizing files."""
    print("=== Genre-Based File Organizer - Basic Example ===\n")
    
    # Initialize organizer
    organizer = GenreBasedFileOrganizer()
    
    # Organize files from a directory
    source_directory = "./sample_files"  # Change this to your directory
    output_directory = "./organized_files"
    
    if not os.path.exists(source_directory):
        print(f"Error: Directory '{source_directory}' not found.")
        print("Please create a directory with .docx, .xlsx, or .pptx files to organize.")
        return
    
    # Organize files (copy them, don't move)
    cluster_map = organizer.organize_files(
        source_dir=source_directory,
        output_dir=output_directory,
        n_clusters=None,  # Auto-determine number of clusters
        copy_files=True   # Copy instead of moving files
    )
    
    print(f"\n✓ Successfully organized {sum(len(files) for files in cluster_map.values())} files!")


def example_custom_clusters():
    """Example with custom number of clusters."""
    print("=== Genre-Based File Organizer - Custom Clusters ===\n")
    
    organizer = GenreBasedFileOrganizer()
    
    source_directory = "./sample_files"
    output_directory = "./organized_custom"
    
    if not os.path.exists(source_directory):
        print(f"Error: Directory '{source_directory}' not found.")
        return
    
    # Organize with specific number of clusters
    cluster_map = organizer.organize_files(
        source_dir=source_directory,
        output_dir=output_directory,
        n_clusters=3,     # Force 3 clusters
        copy_files=True
    )
    
    print(f"\n✓ Organized into {len(cluster_map)} groups!")


def example_find_similar():
    """Example of finding similar files."""
    print("=== Genre-Based File Organizer - Find Similar Files ===\n")
    
    organizer = GenreBasedFileOrganizer()
    
    source_directory = "./sample_files"
    
    if not os.path.exists(source_directory):
        print(f"Error: Directory '{source_directory}' not found.")
        return
    
    # First, organize files to build index
    organizer.organize_files(
        source_dir=source_directory,
        output_dir="./organized_temp",
        copy_files=True
    )
    
    # Find similar files to a specific file
    query_file = "./sample_files/example.docx"  # Change to an actual file
    if os.path.exists(query_file):
        similar_files = organizer.find_similar_files(query_file, k=5)
    else:
        print(f"Query file '{query_file}' not found.")


if __name__ == "__main__":
    # Run basic example
    example_basic_usage()
    
    # Uncomment to try other examples:
    # example_custom_clusters()
    # example_find_similar()
