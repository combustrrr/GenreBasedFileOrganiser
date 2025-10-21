# Usage Guide - Genre-Based File Organizer

This guide provides detailed information on how to use the AI-powered file organizer.

## Table of Contents
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Command Line Interface](#command-line-interface)
- [Python API](#python-api)
- [Understanding the Output](#understanding-the-output)
- [Advanced Usage](#advanced-usage)
- [Troubleshooting](#troubleshooting)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- At least 2GB of free RAM (for the ML model)
- At least 500MB of free disk space (for the model)

### Step-by-step Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/combustrrr/GenreBasedFileOrganiser.git
   cd GenreBasedFileOrganiser
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation:**
   ```bash
   python check_deps.py
   ```

   You should see:
   ```
   ✓ torch
   ✓ transformers
   ✓ faiss-cpu
   ✓ python-docx
   ✓ openpyxl
   ✓ python-pptx
   ✓ numpy
   ✓ scikit-learn
   ```

## Quick Start

### Organize Files in a Directory

```bash
python organize.py /path/to/your/files
```

This will:
1. Scan the directory for `.docx`, `.xlsx`, and `.pptx` files
2. Extract text content from each file
3. Generate semantic embeddings using DistilBERT
4. Cluster similar files together
5. Create a new `organized` folder with grouped files

### Example Output

```
=== Scanning directory: ./my_documents ===
Found 9 supported files

=== Extracting Text ===
Extracting (1/9): report.docx
Extracting (2/9): presentation.pptx
...

=== Loading AI Models ===
Loading distilbert-base-uncased model...
Model loaded on cpu

=== Generating Embeddings ===
Processing 9 documents...

=== Clustering Files ===
Auto-determined 3 clusters for 9 documents
Clustered 9 documents into 3 groups
  Cluster 0: 3 documents
  Cluster 1: 4 documents
  Cluster 2: 2 documents

=== Organizing Files ===
Copied: report.docx -> group_0
Copied: budget.xlsx -> group_0
...

=== Organization Complete ===
Files organized into 3 groups at: ./my_documents/organized
```

## Command Line Interface

### Basic Commands

**Organize files (copy mode):**
```bash
python organize.py /path/to/files
```

**Organize files to a specific output directory:**
```bash
python organize.py /path/to/files -o /path/to/output
```

**Organize with a specific number of clusters:**
```bash
python organize.py /path/to/files -n 5
```

**Move files instead of copying:**
```bash
python organize.py /path/to/files --move
```

**Find similar files:**
```bash
python organize.py /path/to/files --similar report.docx -k 10
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `source_dir` | Source directory containing files | Required |
| `-o, --output` | Output directory for organized files | `source_dir/organized` |
| `-n, --clusters` | Number of clusters | Auto-determined |
| `--move` | Move files instead of copying | False (copy) |
| `--similar FILE` | Find files similar to FILE | None |
| `-k, --top-k` | Number of similar files to find | 5 |

### Examples

**Example 1: Basic organization**
```bash
python organize.py ./documents
```

**Example 2: Custom output and cluster count**
```bash
python organize.py ./documents -o ./sorted -n 4
```

**Example 3: Move files with auto-clustering**
```bash
python organize.py ./documents --move
```

**Example 4: Find similar documents**
```bash
python organize.py ./documents --similar ./documents/template.docx -k 10
```

## Python API

### Basic Usage

```python
from file_organizer import GenreBasedFileOrganizer

# Initialize the organizer
organizer = GenreBasedFileOrganizer()

# Organize files
cluster_map = organizer.organize_files(
    source_dir="./my_files",
    output_dir="./organized",
    n_clusters=None,  # Auto-determine
    copy_files=True   # Copy instead of move
)

# Print results
for cluster_id, files in cluster_map.items():
    print(f"Cluster {cluster_id}: {len(files)} files")
```

### Advanced API Usage

**Extract text from files:**
```python
from text_extractor import TextExtractor

extractor = TextExtractor()
text = extractor.extract_text("document.docx")
print(text)
```

**Generate embeddings:**
```python
from embedding_generator import EmbeddingGenerator

generator = EmbeddingGenerator()
embedding = generator.generate_embedding("Your text here")
print(f"Embedding shape: {embedding.shape}")  # (768,)
```

**Cluster documents manually:**
```python
from clusterer import DocumentClusterer
import numpy as np

# Assume you have embeddings as numpy array
embeddings = np.random.randn(10, 768)  # 10 documents

clusterer = DocumentClusterer()
clusters = clusterer.cluster_documents(embeddings, n_clusters=3)
print(clusters)  # Array of cluster labels
```

**Find similar files:**
```python
# After organizing files
similar_files = organizer.find_similar_files("query.docx", k=5)

for file_path, similarity_score in similar_files:
    print(f"{file_path}: {similarity_score:.3f}")
```

## Understanding the Output

### Folder Structure

After running the organizer, you'll see:

```
organized/
├── group_0/
│   ├── report1.docx
│   ├── budget.xlsx
│   └── presentation.pptx
├── group_1/
│   ├── recipe.docx
│   ├── ingredients.xlsx
│   └── cooking_tips.pptx
└── group_2/
    ├── ml_paper.docx
    └── neural_networks.pptx
```

### Interpreting Clusters

- Each `group_X` folder contains semantically similar documents
- Files are grouped by content, not by file type or name
- The cluster IDs (0, 1, 2, ...) are arbitrary labels

### Cluster Quality

The quality of clustering depends on:
- **Content richness**: Documents with more text are easier to cluster
- **Semantic similarity**: Documents on similar topics group together
- **Number of files**: More files generally lead to better clusters
- **Number of clusters**: Auto-determined or manually specified

## Advanced Usage

### Custom Number of Clusters

```python
# Force specific number of clusters
organizer.organize_files(
    source_dir="./files",
    n_clusters=5,  # Force 5 groups
    copy_files=True
)
```

### Scan Subdirectories

The organizer automatically scans all subdirectories:

```python
# This will find all supported files in ./files and all subdirectories
organizer.organize_files(source_dir="./files")
```

### Process Only Specific File Types

Modify the `TextExtractor` to support only certain formats:

```python
from text_extractor import TextExtractor

extractor = TextExtractor()
extractor.supported_formats = {'.docx'}  # Only Word files

# Then use in your organizer
```

### Custom Embeddings

Use the embedding generator separately:

```python
from embedding_generator import EmbeddingGenerator

generator = EmbeddingGenerator()

texts = ["Text 1", "Text 2", "Text 3"]
embeddings = generator.generate_embeddings_batch(texts)

# Use embeddings for custom clustering or similarity search
```

## Troubleshooting

### Common Issues

**Issue: "No module named 'transformers'"**
```bash
# Solution: Install missing dependencies
pip install transformers torch faiss-cpu
```

**Issue: "CUDA out of memory"**
```python
# Solution: The model automatically uses CPU if GPU memory is insufficient
# This is handled automatically, but processing will be slower
```

**Issue: "No files found"**
```bash
# Ensure your directory contains .docx, .xlsx, or .pptx files
# Check file extensions are lowercase
```

**Issue: "Slow processing"**
```
# This is normal - embedding generation takes time
# Processing ~10-20 documents per minute is expected
# Use a machine with GPU for faster processing
```

**Issue: "Bad clustering results"**
```python
# Try adjusting the number of clusters:
organizer.organize_files(source_dir="./files", n_clusters=3)

# Or ensure documents have sufficient text content
```

### Performance Tips

1. **Use GPU**: If available, the model will automatically use GPU for ~10x speedup
2. **Batch processing**: The organizer processes all files in one batch for efficiency
3. **Cache embeddings**: Save embeddings to reuse for multiple clustering attempts
4. **Reduce files**: Process smaller batches if memory is limited

### Getting Help

- Check the README for basic information
- Review the example.py file for usage patterns
- Run `python organize.py --help` for CLI options
- File issues on GitHub for bugs or feature requests

## Best Practices

1. **Start with auto-clustering**: Let the system determine optimal clusters
2. **Review results**: Check if files are grouped logically
3. **Adjust as needed**: Fine-tune cluster count based on results
4. **Keep backups**: Use copy mode first, then switch to move mode
5. **Clean data**: Remove empty or corrupted files before processing
6. **Organize regularly**: Run periodically to keep files organized

## Example Workflows

### Workflow 1: Organize Research Papers

```bash
# Organize academic papers by topic
python organize.py ./research_papers -o ./organized_papers -n 10
```

### Workflow 2: Find Related Documents

```bash
# Find documents similar to a template
python organize.py ./documents --similar template.docx -k 20
```

### Workflow 3: Clean Up Downloads Folder

```bash
# Organize downloads folder
python organize.py ~/Downloads -o ~/Documents/Organized --move
```

### Workflow 4: Programmatic Organization

```python
import os
from file_organizer import GenreBasedFileOrganizer

# Process multiple directories
directories = ["./dir1", "./dir2", "./dir3"]
organizer = GenreBasedFileOrganizer()

for directory in directories:
    if os.path.exists(directory):
        print(f"Processing {directory}...")
        organizer.organize_files(
            source_dir=directory,
            output_dir=f"{directory}_organized",
            copy_files=True
        )
```

## Next Steps

- Explore the Python API for custom workflows
- Integrate with file management scripts
- Automate organization with cron jobs or schedulers
- Extend to support additional file formats
