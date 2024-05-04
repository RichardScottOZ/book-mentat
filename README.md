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
#### comics
- https://linnk.ai/insight/comics-analysis/multimodal-transformer-for-comics-text-cloze-enhancing-narrative-understanding-in-comics-analysis-f7rPlZEc/

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

### Tokenisers
- ?

### Models
- Text
- Multimodal


