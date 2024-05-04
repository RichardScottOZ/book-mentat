#!/bin/bash

# Input directory containing the eBooks to be processed
INPUT_DIR="/mnt/usb_mount/books/Calibre Books"

# Output directory where converted EPUBs will be saved
OUTPUT_DIR="/mnt/usb_mount/output/Calibre Books"

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Loop through each file in the input directory
for FILE in "$INPUT_DIR"/*; do
    # Check if the file is a directory
    if [[ -d "$FILE" ]]; then
        # Skip directories
        continue
    fi

    # Extract the filename without extension
    FILENAME=$(basename "$FILE" | cut -d. -f1)
    EXTENSION="${FILE##*.}"

    # Check if the file has an undesirable extension
    if [[ "$EXTENSION" == "json" || "$EXTENSION" == "db" || "$EXTENSION" == "jpeg" ]]; then
        # If the file has an undesirable extension, skip it
        echo "Skipping $FILE - undesirable extension"
        continue
    fi

    # Check if the file is already an EPUB
    if [[ "$EXTENSION" == "epub" ]]; then
        # If the file is already an EPUB, copy it to the output directory
        cp "$FILE" "$OUTPUT_DIR"
        # Print status message
        echo "Copied $FILE to $OUTPUT_DIR"
    else
        # Convert the non-EPUB eBook to EPUB format and save it to the output directory
        ebook-convert "$FILE" "$OUTPUT_DIR/$FILENAME.epub"
        # Print status message
        echo "Converted $FILE to EPUB"
    fi
done
