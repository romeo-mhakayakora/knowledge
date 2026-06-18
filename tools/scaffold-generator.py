#!/usr/bin/env python3
"""
Scaffold new subject directory structure.
Usage: python scaffold-generator.py --domain mathematics --subject probability --chapters 5
"""

import os
import argparse
import yaml
from datetime import datetime

def create_directory(path):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)

def create_subject_structure(domain, subject, num_chapters=3, title=None):
    """Create subject directory structure."""
    subject_dir = f"content/{domain}/{subject}"
    create_directory(subject_dir)
    
    # Create subject metadata
    subject_yml = {
        'name': title or subject.replace('-', ' ').title(),
        'slug': subject,
        'domain': domain,
        'description': f'Subject: {subject}',
        'chapters': [f'{i:02d}-chapter-{i}' for i in range(1, num_chapters + 1)],
        'difficulty': 'beginner',
        'learning_outcomes': ['Learning outcome 1', 'Learning outcome 2'],
        'prerequisites': [],
        'related_subjects': []
    }
    
    with open(f'{subject_dir}/_subject.yml', 'w') as f:
        yaml.dump(subject_yml, f, default_flow_style=False)
    
    # Create chapters
    for i in range(1, num_chapters + 1):
        chapter_name = f'{i:02d}-chapter-{i}'
        chapter_dir = f'{subject_dir}/{chapter_name}'
        create_directory(chapter_dir)
        
        # Chapter metadata
        chapter_yml = {
            'title': f'Chapter {i}',
            'chapter': chapter_name,
            'topics': ['topic-1', 'topic-2']
        }
        
        with open(f'{chapter_dir}/_chapter.yml', 'w') as f:
            yaml.dump(chapter_yml, f, default_flow_style=False)
        
        # Chapter README
        with open(f'{chapter_dir}/README.md', 'w') as f:
            f.write(f"""---
title: Chapter {i}
---

# Chapter {i}

Chapter overview and learning objectives.

## Topics

- [[topic-1]] — Description
- [[topic-2]] — Description

## Learning Objectives

- [ ] Learning objective 1
- [ ] Learning objective 2
""")
    
    # Create concepts folder
    concepts_dir = f'{subject_dir}/concepts'
    create_directory(concepts_dir)
    with open(f'{concepts_dir}/README.md', 'w') as f:
        f.write("""---
title: Concepts
---

# Concepts

Subject-specific concepts and definitions.
""")
    
    # Subject README
    with open(f'{subject_dir}/README.md', 'w') as f:
        f.write(f"""---
title: {subject.replace('-', ' ').title()}
---

# {subject.replace('-', ' ').title()}

Subject overview and learning guide.

## Overview

Description of this subject.

## Chapters

""")
        for i in range(1, num_chapters + 1):
            f.write(f"- **Chapter {i}:** [[[{i:02d}-chapter-{i}|Chapter {i}]]]\n")
    
    print(f"✅ Created subject structure: {subject_dir}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scaffold new knowledge subject')
    parser.add_argument('--domain', required=True, help='Domain (e.g., mathematics)')
    parser.add_argument('--subject', required=True, help='Subject (e.g., probability)')
    parser.add_argument('--chapters', type=int, default=3, help='Number of chapters')
    parser.add_argument('--title', help='Full subject title')
    
    args = parser.parse_args()
    
    create_subject_structure(args.domain, args.subject, args.chapters, args.title)
