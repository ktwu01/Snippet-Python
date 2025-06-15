#!/usr/bin/env python3
# Convert Markdown files to Jupyter Notebook format for MATLAB
# This script reads a Markdown file, processes its content, and outputs a Jupyter Notebook (.ipynb) file.
# python3 md_to_ipynb.py input.md output.ipynb
# python3 md_to_ipynb.py input.md MATLAB-Common-Snippets0.ipynb

import json
import sys
import re

def clean_text(text):
    """Remove control characters and clean text for JSON"""
    # Remove control characters except newlines and tabs
    cleaned = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)
    return cleaned

def convert_md_to_ipynb(input_file, output_file):
    """Convert markdown to Jupyter notebook format"""
    
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"❌ Error reading input file: {e}")
        return False
    
    print(f"📝 Processing {len(lines)} lines...")
    
    cells = []
    current_code_block = []
    
    for line_num, line in enumerate(lines, 1):
        # Clean the line
        line = clean_text(line.rstrip())
        
        # Check if line starts with # (heading)
        if re.match(r'^\s*#+\s+', line):
            # Flush any pending code block
            if current_code_block:
                # Remove empty lines from start and end
                while current_code_block and not current_code_block[0].strip():
                    current_code_block.pop(0)
                while current_code_block and not current_code_block[-1].strip():
                    current_code_block.pop()
                
                if current_code_block:
                    cells.append({
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "outputs": [],
                        "source": [line + "\n" for line in current_code_block]
                    })
                current_code_block = []
            
            # Add heading as markdown cell
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [line + "\n"]
            })
        else:
            # Add to code block
            current_code_block.append(line)
    
    # Flush final code block
    if current_code_block:
        # Remove empty lines from start and end
        while current_code_block and not current_code_block[0].strip():
            current_code_block.pop(0)
        while current_code_block and not current_code_block[-1].strip():
            current_code_block.pop()
        
        if current_code_block:
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [line + "\n" for line in current_code_block]
            })
    
    # Create notebook structure
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "MATLAB",
                "language": "matlab",
                "name": "matlab"
            },
            "language_info": {
                "file_extension": ".m",
                "mimetype": "text/x-matlab",
                "name": "matlab",
                "version": "9.13"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Write to file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)
        print(f"✅ Conversion complete!")
        print(f"📍 Output: {output_file}")
        print(f"📋 Created {len(cells)} cells")
        return True
    except Exception as e:
        print(f"❌ Error writing output file: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 md_to_ipynb.py input.md output.ipynb")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if convert_md_to_ipynb(input_file, output_file):
        print("🔧 Open in VS Code for full functionality")
        sys.exit(0)
    else:
        sys.exit(1)