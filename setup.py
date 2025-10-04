"""
Setup script for the Genre-Based File Organizer.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="genre-based-file-organizer",
    version="1.0.0",
    author="GenreBasedFileOrganiser",
    description="AI-powered file organizer using NLP and semantic clustering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/combustrrr/GenreBasedFileOrganiser",
    packages=find_packages(),
    py_modules=[
        'main',
        'file_organizer',
        'text_extractor',
        'embedding_generator',
        'clusterer',
        'gui',
        'logger',
        'organize',
        'example',
        'check_deps',
        'test_organizer'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "faiss-cpu>=1.7.4",
        "python-docx>=0.8.11",
        "openpyxl>=3.0.10",
        "python-pptx>=0.6.21",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
    ],
    entry_points={
        'console_scripts': [
            'file-organizer=main:main',
        ],
        'gui_scripts': [
            'file-organizer-gui=main:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
