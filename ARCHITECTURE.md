# Architecture Documentation

## System Overview

The Genre-Based File Organizer is a modular AI-powered system that uses Natural Language Processing (NLP) and clustering algorithms to automatically organize documents by their semantic content.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     Input Layer                              │
│  Office Files (.docx, .xlsx, .pptx) from filesystem          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                  Text Extraction Layer                       │
│                  (text_extractor.py)                         │
│                                                               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                  │
│  │  python- │  │  openpyxl │  │  python- │                  │
│  │   docx   │  │          │  │   pptx   │                  │
│  └──────────┘  └──────────┘  └──────────┘                  │
│                                                               │
│  Extracts: Paragraphs, Tables, Cells, Shapes                │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                Embedding Generation Layer                    │
│               (embedding_generator.py)                       │
│                                                               │
│  ┌──────────────────────────────────────────────┐           │
│  │          DistilBERT Transformer               │           │
│  │    (distilbert-base-uncased)                 │           │
│  │                                               │           │
│  │  Input: Text string                          │           │
│  │  Output: 768-dimensional vector              │           │
│  │  Method: [CLS] token representation          │           │
│  └──────────────────────────────────────────────┘           │
│                                                               │
│  Features: Semantic understanding, contextual embeddings    │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                  Clustering Layer                            │
│                   (clusterer.py)                             │
│                                                               │
│  ┌─────────────┐         ┌──────────────┐                  │
│  │    FAISS    │         │   K-means    │                  │
│  │    Index    │────────▶│  Clustering  │                  │
│  │             │         │              │                  │
│  │  Similarity │         │  Groups docs │                  │
│  │   Search    │         │  by content  │                  │
│  └─────────────┘         └──────────────┘                  │
│                                                               │
│  Operations:                                                 │
│  - Build similarity index                                   │
│  - Perform K-means clustering                               │
│  - Find similar documents                                   │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                 Organization Layer                           │
│                (file_organizer.py)                          │
│                                                               │
│  Operations:                                                 │
│  - Scan directories                                         │
│  - Orchestrate pipeline                                     │
│  - Create group folders                                     │
│  - Copy/move files to groups                               │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                   Output Layer                               │
│     Organized folders (group_0, group_1, ...)               │
└─────────────────────────────────────────────────────────────┘
```

## Module Details

### 1. Text Extractor (`text_extractor.py`)

**Purpose**: Extract text content from Office files

**Key Classes**:
- `TextExtractor`: Main extraction class

**Supported Formats**:
- `.docx` (Word): Extracts from paragraphs and tables
- `.xlsx` (Excel): Extracts from all sheets and cells
- `.pptx` (PowerPoint): Extracts from all shapes in all slides

**Dependencies**:
- `python-docx`: Word document processing
- `openpyxl`: Excel spreadsheet processing
- `python-pptx`: PowerPoint presentation processing

**Methods**:
```python
extract_text(file_path: str) -> str
extract_from_docx(file_path: str) -> str
extract_from_xlsx(file_path: str) -> str
extract_from_pptx(file_path: str) -> str
is_supported(file_path: str) -> bool
```

**Example**:
```python
extractor = TextExtractor()
text = extractor.extract_text("document.docx")
```

### 2. Embedding Generator (`embedding_generator.py`)

**Purpose**: Convert text to semantic embeddings using DistilBERT

**Key Classes**:
- `EmbeddingGenerator`: Wrapper for DistilBERT model

**Model Details**:
- Base model: `distilbert-base-uncased`
- Parameters: ~66M
- Output dimension: 768
- Context window: 512 tokens

**Architecture**:
```
Text Input
    ↓
Tokenizer (WordPiece)
    ↓
DistilBERT Transformer (6 layers)
    ↓
[CLS] Token Embedding (768-dim)
    ↓
Output Vector
```

**Dependencies**:
- `transformers`: Hugging Face transformers library
- `torch`: PyTorch deep learning framework

**Methods**:
```python
generate_embedding(text: str, max_length: int = 512) -> np.ndarray
generate_embeddings_batch(texts: List[str], max_length: int = 512) -> np.ndarray
```

**Example**:
```python
generator = EmbeddingGenerator()
embedding = generator.generate_embedding("Machine learning text")
# Output: array of shape (768,)
```

### 3. Document Clusterer (`clusterer.py`)

**Purpose**: Cluster documents using FAISS and K-means

**Key Classes**:
- `DocumentClusterer`: Clustering and similarity search

**Algorithms**:

1. **FAISS Index (Facebook AI Similarity Search)**:
   - Type: `IndexFlatIP` (Inner Product for cosine similarity)
   - Purpose: Efficient similarity search
   - Normalization: L2 normalization for cosine similarity

2. **K-means Clustering**:
   - Implementation: scikit-learn K-means
   - Initialization: k-means++
   - Iterations: 10 (n_init=10)

**Auto-clustering Heuristic**:
```python
n_clusters = max(2, min(int(sqrt(n_samples / 2)), 10))
```

**Dependencies**:
- `faiss-cpu`: FAISS library for similarity search
- `scikit-learn`: K-means clustering
- `numpy`: Numerical operations

**Methods**:
```python
build_index(embeddings: np.ndarray) -> None
cluster_documents(embeddings: np.ndarray, n_clusters: Optional[int]) -> np.ndarray
find_similar(query_embedding: np.ndarray, k: int) -> Tuple[np.ndarray, np.ndarray]
get_cluster_label(idx: int) -> int
```

**Example**:
```python
clusterer = DocumentClusterer()
clusterer.build_index(embeddings)
clusters = clusterer.cluster_documents(embeddings, n_clusters=3)
```

### 4. File Organizer (`file_organizer.py`)

**Purpose**: Orchestrate the entire pipeline

**Key Classes**:
- `GenreBasedFileOrganizer`: Main orchestration class

**Pipeline**:
```
1. Scan directory
2. Extract text from all files
3. Generate embeddings (lazy load models)
4. Build FAISS index
5. Cluster documents
6. Create group folders
7. Copy/move files to groups
```

**Features**:
- Lazy model loading (load only when needed)
- Progress reporting
- Batch processing
- Similarity search
- Duplicate name handling

**Methods**:
```python
organize_files(source_dir: str, output_dir: Optional[str], 
               n_clusters: Optional[int], copy_files: bool) -> Dict[int, List[str]]
scan_directory(directory_path: str) -> List[str]
extract_texts(file_paths: List[str]) -> List[str]
generate_embeddings(texts: List[str]) -> np.ndarray
cluster_files(embeddings: np.ndarray, n_clusters: Optional[int]) -> np.ndarray
find_similar_files(query_file: str, k: int) -> List[Tuple[str, float]]
```

**Example**:
```python
organizer = GenreBasedFileOrganizer()
cluster_map = organizer.organize_files(
    source_dir="./documents",
    output_dir="./organized",
    n_clusters=None,
    copy_files=True
)
```

## Data Flow

### 1. Organization Flow

```
User Input (directory path)
    ↓
Scan Directory
    ↓
Found Files [file1.docx, file2.xlsx, ...]
    ↓
Extract Text [text1, text2, ...]
    ↓
Generate Embeddings [[0.1, 0.2, ...], [0.3, 0.4, ...], ...]
    ↓
Build FAISS Index
    ↓
K-means Clustering
    ↓
Cluster Labels [0, 1, 0, 2, 1, ...]
    ↓
Create Folders [group_0/, group_1/, group_2/]
    ↓
Copy/Move Files
    ↓
Organized Output
```

### 2. Similarity Search Flow

```
Query File
    ↓
Extract Text
    ↓
Generate Embedding
    ↓
FAISS Search (k-nearest neighbors)
    ↓
Similar Files + Similarity Scores
```

## Performance Characteristics

### Time Complexity

- Text extraction: O(n × m) where n = files, m = avg file size
- Embedding generation: O(n × t) where t = avg tokens per file
- FAISS index building: O(n × d) where d = embedding dimension (768)
- K-means clustering: O(n × k × i) where k = clusters, i = iterations
- Overall: O(n × (m + t + d + k × i))

### Space Complexity

- Text storage: O(n × m)
- Embeddings: O(n × 768) ≈ 3KB per file
- FAISS index: O(n × 768)
- Model memory: ~1-2GB (DistilBERT)
- Total: ~2GB + O(n)

### Throughput

- Text extraction: ~100-500 files/min
- Embedding generation (CPU): ~10-20 files/min
- Embedding generation (GPU): ~100-200 files/min
- Clustering: ~1000 files/sec

**Bottleneck**: Embedding generation (especially on CPU)

## Design Patterns

### 1. Strategy Pattern
Different extraction strategies for different file types:
```python
if ext == '.docx':
    return self.extract_from_docx(file_path)
elif ext == '.xlsx':
    return self.extract_from_xlsx(file_path)
elif ext == '.pptx':
    return self.extract_from_pptx(file_path)
```

### 2. Lazy Initialization
Models are loaded only when needed:
```python
def _load_models(self):
    if self.embedding_generator is None:
        self.embedding_generator = EmbeddingGenerator()
        self.clusterer = DocumentClusterer()
```

### 3. Facade Pattern
`GenreBasedFileOrganizer` provides a simple interface to complex subsystems:
```python
organizer.organize_files(source_dir, output_dir)
# Hides: extraction, embedding, clustering, file operations
```

## Error Handling

### File-level Errors
- Invalid file formats → Skip with warning
- Corrupted files → Skip with error message
- Empty files → Generate zero embedding

### System-level Errors
- Missing models → Download automatically
- Out of memory → Graceful degradation
- Permission errors → Report and skip

### Recovery Strategies
- Continue processing remaining files on individual failures
- Log errors for debugging
- Provide meaningful error messages

## Extensibility

### Adding New File Formats

1. Add extraction method to `TextExtractor`:
```python
def extract_from_pdf(self, file_path):
    # PDF extraction logic
    return text
```

2. Update supported formats:
```python
self.supported_formats = {'.docx', '.xlsx', '.pptx', '.pdf'}
```

3. Add to extraction dispatcher:
```python
elif ext == '.pdf':
    return self.extract_from_pdf(file_path)
```

### Custom Embedding Models

Replace DistilBERT with another model:
```python
class CustomEmbeddingGenerator(EmbeddingGenerator):
    def __init__(self):
        # Load custom model
        self.model = CustomModel()
```

### Custom Clustering Algorithms

Extend `DocumentClusterer`:
```python
class HierarchicalClusterer(DocumentClusterer):
    def cluster_documents(self, embeddings, n_clusters):
        # Use hierarchical clustering
        return clusters
```

## Testing Strategy

### Unit Tests
- Test each module independently
- Mock external dependencies
- Verify edge cases

### Integration Tests
- Test pipeline end-to-end
- Use sample documents
- Verify clustering quality

### Performance Tests
- Benchmark processing speed
- Monitor memory usage
- Test with large datasets

## Deployment Considerations

### Resource Requirements
- RAM: 2-4GB minimum
- Storage: 500MB for models
- CPU: Multi-core recommended
- GPU: Optional but 10x faster

### Optimization Tips
1. Use GPU for embedding generation
2. Batch process files
3. Cache embeddings for reuse
4. Use FAISS GPU index for large datasets

### Scalability
- Current: Hundreds to thousands of files
- Large scale: Consider distributed processing
- Very large: Use approximate FAISS indices

## Security Considerations

### File Access
- Read-only access to source files
- Write access to output directory
- No network access required (after model download)

### Data Privacy
- All processing is local
- No data sent to external services
- Models run offline after initial download

### Input Validation
- Validate file paths
- Check file extensions
- Handle malicious files gracefully

## Future Enhancements

1. **Additional File Formats**: PDF, TXT, CSV
2. **Hierarchical Clustering**: Multi-level organization
3. **Custom Labels**: User-defined cluster names
4. **Web Interface**: Browser-based UI
5. **Watch Mode**: Automatic organization of new files
6. **Cloud Integration**: S3, Google Drive support
7. **Metadata Extraction**: Authors, dates, keywords
8. **Multi-language Support**: Non-English documents
