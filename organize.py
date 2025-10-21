#!/usr/bin/env python3
"""
Command-line interface for the Genre-Based File Organizer.
"""

import argparse
import sys
from pathlib import Path
from file_organizer import GenreBasedFileOrganizer


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description='AI-powered file organizer using NLP and clustering',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Organize files in current directory
  python organize.py ./my_files

  # Organize with custom output directory
  python organize.py ./my_files -o ./sorted_files

  # Organize with specific number of clusters
  python organize.py ./my_files -n 5

  # Move files instead of copying
  python organize.py ./my_files --move

  # Find files similar to a specific file
  python organize.py ./my_files --similar example.docx -k 10
        """
    )
    
    parser.add_argument(
        'source_dir',
        type=str,
        help='Source directory containing files to organize'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        default=None,
        help='Output directory for organized files (default: source_dir/organized)'
    )
    
    parser.add_argument(
        '-n', '--clusters',
        type=int,
        default=None,
        help='Number of clusters (default: auto-determined)'
    )
    
    parser.add_argument(
        '--move',
        action='store_true',
        help='Move files instead of copying them'
    )
    
    parser.add_argument(
        '--similar',
        type=str,
        default=None,
        help='Find files similar to the specified file'
    )
    
    parser.add_argument(
        '-k', '--top-k',
        type=int,
        default=5,
        help='Number of similar files to find (default: 5)'
    )
    
    args = parser.parse_args()
    
    # Validate source directory
    source_path = Path(args.source_dir)
    if not source_path.exists():
        print(f"Error: Source directory '{args.source_dir}' not found.", file=sys.stderr)
        sys.exit(1)
    
    # Initialize organizer
    organizer = GenreBasedFileOrganizer()
    
    try:
        if args.similar:
            # Find similar files mode
            query_file = args.similar
            if not Path(query_file).exists():
                # Try relative to source directory
                query_file = source_path / query_file
                if not query_file.exists():
                    print(f"Error: Query file '{args.similar}' not found.", file=sys.stderr)
                    sys.exit(1)
            
            # First organize to build index
            print("Building index...")
            organizer.organize_files(
                source_dir=args.source_dir,
                output_dir=args.output,
                n_clusters=args.clusters,
                copy_files=not args.move
            )
            
            # Find similar files
            similar_files = organizer.find_similar_files(str(query_file), k=args.top_k)
            
        else:
            # Normal organization mode
            cluster_map = organizer.organize_files(
                source_dir=args.source_dir,
                output_dir=args.output,
                n_clusters=args.clusters,
                copy_files=not args.move
            )
            
            if cluster_map:
                print("\n✓ Organization complete!")
                total_files = sum(len(files) for files in cluster_map.values())
                print(f"  {total_files} files organized into {len(cluster_map)} groups")
            else:
                print("\n⚠ No files were organized. Check if the directory contains supported files.")
    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
