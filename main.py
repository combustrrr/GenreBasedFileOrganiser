#!/usr/bin/env python3
"""
Main entry point for the Genre-Based File Organizer GUI application.
"""

import logger
from file_organizer import GenreBasedFileOrganizer
from gui import create_gui


def organize_files_wrapper(source_dir, n_clusters=None, copy_files=True, progress_callback=None):
    """Wrapper function for organizing files with GUI support.
    
    Args:
        source_dir: Source directory containing files to organize
        n_clusters: Number of clusters (None for auto)
        copy_files: Whether to copy (True) or move (False) files
        progress_callback: Callback function for progress updates
        
    Returns:
        dict: Dictionary mapping cluster IDs to file lists
    """
    organizer = GenreBasedFileOrganizer()
    
    result = organizer.organize_files(
        source_dir=source_dir,
        output_dir=None,  # Will create "Sorted" folder in source_dir
        n_clusters=n_clusters,
        copy_files=copy_files,
        progress_callback=progress_callback
    )
    
    return result


if __name__ == "__main__":
    # Setup logging
    logger.setup_logging()
    
    # Create and run GUI
    create_gui(organize_files_wrapper)
