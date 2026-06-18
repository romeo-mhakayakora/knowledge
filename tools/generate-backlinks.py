#!/usr/bin/env python3
"""
Generate backlinks map for wikilink resolution.
Outputs: config/backlinks.json
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

def extract_wikilinks(content):
    """Extract all [[wikilink]] references from content."""
    pattern = r'\[\[([^\]]+)\]\]'
    return re.findall(pattern, content)

def build_backlinks_map(content_dir):
    """Build map of wikilinks to files that reference them."""
    backlinks = defaultdict(list)
    
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if not file.endswith('.md') or file.startswith('_'):
                continue
            
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, content_dir)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                links = extract_wikilinks(content)
                for link in links:
                    backlinks[link.lower()].append(rel_path)
            
            except Exception as e:
                print(f"Warning: Could not read {filepath}: {e}")
    
    return backlinks

def save_backlinks(backlinks, output_path):
    """Save backlinks map as JSON."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dict(backlinks), f, indent=2, ensure_ascii=False)
    
    print(f"✅ Backlinks map saved to {output_path}")
    print(f"   Total links: {len(backlinks)}")

if __name__ == '__main__':
    content_dir = 'content'
    output_path = 'config/backlinks.json'
    
    print("Building backlinks map...")
    backlinks = build_backlinks_map(content_dir)
    save_backlinks(backlinks, output_path)
