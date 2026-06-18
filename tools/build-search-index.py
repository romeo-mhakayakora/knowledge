#!/usr/bin/env python3
"""
Generate search index for MkDocs.
Extracts frontmatter metadata for enhanced search.
"""

import os
import json
import re
import yaml
from pathlib import Path

def extract_frontmatter(filepath):
    """Extract YAML frontmatter from markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return None
        
        lines = content.split('\n')
        closing_idx = None
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                closing_idx = i
                break
        
        if closing_idx is None:
            return None
        
        fm_text = '\n'.join(lines[1:closing_idx])
        return yaml.safe_load(fm_text)
    
    except Exception:
        return None

def build_search_index(content_dir):
    """Build search index with metadata."""
    index = []
    
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if not file.endswith('.md') or file.startswith('_') or file == 'README.md':
                continue
            
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, content_dir)
            
            try:
                frontmatter = extract_frontmatter(filepath)
                if not frontmatter:
                    continue
                
                entry = {
                    'path': rel_path,
                    'title': frontmatter.get('title', file),
                    'subject': frontmatter.get('subject', ''),
                    'tags': frontmatter.get('tags', []),
                    'difficulty': frontmatter.get('difficulty', 'intermediate'),
                    'status': frontmatter.get('status', 'draft')
                }
                index.append(entry)
            
            except Exception as e:
                print(f"Warning: Could not index {filepath}: {e}")
    
    return index

def save_index(index, output_path):
    """Save search index as JSON."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Search index saved to {output_path}")
    print(f"   Total entries: {len(index)}")

if __name__ == '__main__':
    content_dir = 'content'
    output_path = 'config/search-index.json'
    
    print("Building search index...")
    index = build_search_index(content_dir)
    save_index(index, output_path)
