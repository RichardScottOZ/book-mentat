# book-mentat
Considering how to analyse book collections, Large Language Model style

# Motivation
- Get all the good spaceship names
- Finding old stories you have forgotten
- References found
- State of the art models for a current mineral exploration problem

# Problem
## Library
- Consider an extensive ebook library that is decades old
### Formats
    - text
    - html
    - rtf
    - prc
    - mobipocket
    - epub
    - pdf
    - cbz / cbr

### Origin
    - Not all digital native
        - Failure OCR - what is open source state of the art
        - If on windows - robocopy multithreaded is useful robocopy "C:\Users\bananasplits\OneDrive\Calibre Books" "D:\books\Calibre Books" /MIR /MT:16

### Type
- Fiction
- Non-fiction
- Games
- Academic
    - Papers etc    
- Code
    - Many languages

### Modality
- Do you want covers?
- Diagrams from non-fiction
- Pictures [or comic strips] from games
- Actual comics
    - 2000 AD, Image, Humble Bundles have CBR/CBZ possibilities

### Current State
- Calibre https://calibre-ebook.com/

### Prior Art
#### epub
- https://huggingface.co/learn/cookbook/en/rag_llamaindex_librarian
- https://github.com/huggingface/cookbook/blob/main/notebooks/en/rag_llamaindex_librarian.ipynb
- https://www.bitsgalore.org/2023/03/09/extracting-text-from-epub-files-in-python
    - https://github.com/RichardScottOZ/textExtractDemo
#### comics
- https://linnk.ai/insight/comics-analysis/multimodal-transformer-for-comics-text-cloze-enhancing-narrative-understanding-in-comics-analysis-f7rPlZEc/
    - paper https://arxiv.org/pdf/2403.03719

# Approach
- Clearly will need some sort of Retrieval Augmented Generation

## Data
### Calibre Libraries
- Currently a folder with metadata, db and a folder per 'author' - which is not important, but is the structure

## Technology
### Storage
- Is in memory ok if run on a decent server
- A books library example
```bash
.azw: 12
.azw3: 234
.azw4: 2
.db: 2
.doc: 1
.docx: 1
.epub: 1567
.htmlz: 6
.jpg: 9829
.json: 1
.lit: 2
.lrf: 2
.mobi: 10054
.opf: 10891
.original_epub: 20
.pdb: 9
.pdf: 102
.prc: 315
.rar: 18
.rtf: 9
.txt: 28
.zip: 17
```
### Calibre
- use this for conversion 
    - ubuntu has an apt package

### ollama
- install https://ollama.com/download/linux
    - curl -fsSL https://ollama.com/install.sh | sh
- models: https://ollama.com/library    
- operation https://github.com/ollama/ollama/issues/707
```bash
>>> Creating ollama user...
>>> Adding ollama user to render group...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
>>> Enabling and starting ollama service...
Created symlink /etc/systemd/system/default.target.wants/ollama.service → /etc/systemd/system/ollama.service.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
WARNING: No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode.
```

### Llamaindex
#### Simple Directory Reader
- https://docs.llamaindex.ai/en/v0.9.48/examples/data_connectors/simple_directory_reader.html
- Readers https://github.com/run-llama/llama_index/tree/main/llama-index-integrations/readers/llama-index-readers-file
- Vector Stores https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/

### Chroma
- https://docs.trychroma.com/
    - is multimodal
- installation https://docs.trychroma.com/getting-started
- vector store installation pip install llama-index-vector-stores-chroma
- embedding speed https://www.youtube.com/watch?v=7FvdwwvqrD4&ab_channel=JohnnyCode

### Tokenisers
- ?

### Models
- Text
- Multimodal - Llava?
- https://ollama.com/library

- ollama pull llama2
- ollama run llama3
- etc



# Errors
## bind address already in use
- https://github.com/ollama/ollama/issues/707
- Hey all, not seeing ollama in the output of lsof could be a permissions issue. When you install ollama on linux via the install script it creates a service user for the background process. You may need to stop the process via systemctl in that case.

Here is some troubleshooting steps that will hopefully help:

Stop the background service: sudo systemctl stop ollama
Run lsof as sudo to rule out permissions issues: sudo lsof -i :11434