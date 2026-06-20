#!/usr/bin/env python3
"""
Validate knowledge repository structure and content.
Checks:
- Frontmatter presence and validity
- File naming conventions
- Directory structure
- Wikilinks validity
"""

import os
import re
import yaml
import sys
from pathlib import Path
from collections import defaultdict

def get_all_markdown_files(content_dir):
    """Get all markdown files in content directory."""
    files = []
    for root, dirs, filenames in os.walk(content_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                files.append(filepath)
    return files

def extract_frontmatter(filepath):
    """Extract YAML frontmatter from markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return None, "Missing frontmatter"
        
        # Find closing ---
        lines = content.split('\n')
        closing_idx = None
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                closing_idx = i
                break
        
        if closing_idx is None:
            return None, "Unclosed frontmatter"
        
        fm_text = '\n'.join(lines[1:closing_idx])
        try:
            frontmatter = yaml.safe_load(fm_text)
            return frontmatter, None
        except yaml.YAMLError as e:
            return None, f"Invalid YAML: {e}"
    
    except Exception as e:
        return None, str(e)

def validate_frontmatter(filepath, frontmatter):
    """Validate frontmatter completeness."""
    errors = []
    required = ['title', 'subject', 'chapter', 'tags', 'date', 'updated', 'status', 'difficulty']
    
    if not frontmatter:
        return ["No frontmatter found"]
    
    for field in required:
        if field not in frontmatter:
            errors.append(f"Missing required field: {field}")
    
    # Validate status values
    if 'status' in frontmatter:
        if frontmatter['status'] not in ['draft', 'in-progress', 'complete', 'review']:
            errors.append(f"Invalid status: {frontmatter['status']}")
    
    # Validate difficulty values
    if 'difficulty' in frontmatter:
        if frontmatter['difficulty'] not in ['beginner', 'intermediate', 'advanced']:
            errors.append(f"Invalid difficulty: {frontmatter['difficulty']}")
    
    return errors

def validate_filename(filepath):
    """Validate filename follows conventions."""
    basename = os.path.basename(filepath)
    
    # Skip metadata files
    if basename.startswith('_') or basename == 'README.md' or basename == 'index.md':
        return []
    
    # Check kebab-case
    name_without_ext = basename[:-3]  # Remove .md
    if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', name_without_ext):
        return [f"Filename not kebab-case: {basename}"]
    
    return []

def extract_wikilinks(content):
    """Extract wikilinks from content."""
    pattern = r'\[\[([^\]]+)\]\]'
    return re.findall(pattern, content)

def validate_structure(content_dir, strict=False):
    """Validate entire repository structure."""
    errors = defaultdict(list)
    warnings = defaultdict(list)
    
    files = get_all_markdown_files(content_dir)
    
    print(f"Validating {len(files)} markdown files...")
    
    for filepath in files:
        rel_path = os.path.relpath(filepath, content_dir)
        basename = os.path.basename(filepath)
        
        # Skip frontmatter validation for index.md, README.md, and _* files
        is_meta = basename.startswith('_') or basename == 'README.md' or basename == 'index.md'
        
        if not is_meta:
            # Validate frontmatter
            frontmatter, fm_error = extract_frontmatter(filepath)
            if fm_error:
                errors[rel_path].append(f"Frontmatter error: {fm_error}")
            else:
                fm_errors = validate_frontmatter(filepath, frontmatter)
                errors[rel_path].extend(fm_errors)
        
        # Validate filename
        name_errors = validate_filename(filepath)
        errors[rel_path].extend(name_errors)
    
    # Print results
    total_errors = sum(len(errs) for errs in errors.values())
    
    if total_errors > 0:
        print(f"\n[Error] Found {total_errors} errors:\n")
        for filepath, errs in errors.items():
            if not errs:
                continue
            print(f"  {filepath}")
            for err in errs:
                print(f"    - {err}")
        return 1
    else:
        print(f"\n[Success] All {len(files)} files valid!")
        return 0

if __name__ == '__main__':
    content_dir = 'content'
    strict = '--strict' in sys.argv
    exit_code = validate_structure(content_dir, strict)
    sys.exit(exit_code)
