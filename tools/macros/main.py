import os
import yaml
from datetime import datetime, date, timedelta

# Explicit allowlist of knowledge-domain folder names under content/.
# Asset folders (stylesheets, javascripts) and underscore-prefixed folders
# (_concepts) are excluded from domain listings and counts.
DOMAIN_FOLDERS = {
    'ai',
    'computer-science',
    'economics',
    'mathematics',
    'systems',
}

# Default metadata for each domain — icon (emoji) and short description.
# These are used as fallbacks when no _domain.yml exists.
DOMAIN_META = {
    'mathematics': {
        'icon': '∑',
        'description': 'Probability, statistics, linear algebra, calculus, and proof techniques.',
    },
    'computer-science': {
        'icon': '⟨⟩',
        'description': 'Algorithms, data structures, operating systems, distributed systems, and databases.',
    },
    'ai': {
        'icon': '◎',
        'description': 'Deep learning, NLP, computer vision, reinforcement learning, and LLMs.',
    },
    'economics': {
        'icon': '↗',
        'description': 'Microeconomics, macroeconomics, game theory, and econometrics.',
    },
    'systems': {
        'icon': '⊞',
        'description': 'Complex systems, network science, and systems thinking.',
    },
}

def parse_frontmatter(filepath):
    """Safely parse YAML frontmatter from a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                return yaml.safe_load(parts[1]) or {}
    except Exception as e:
        print(f"Error parsing frontmatter for {filepath}: {e}")
    return {}

def parse_date(date_val):
    """Parse date from various formats, returning datetime.date."""
    if not date_val:
        return None
    if isinstance(date_val, (datetime, date)):
        if hasattr(date_val, 'date'):
            return date_val.date()
        return date_val
    if isinstance(date_val, str):
        date_str = date_val.strip()
        for fmt in ('%Y-%m-%d', '%Y/%m/%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%dT%H:%M:%SZ'):
            try:
                return datetime.strptime(date_str, fmt).date()
            except ValueError:
                continue
    return None

def define_env(env):
    """Define environment macros for mkdocs-macros-plugin."""
    
    @env.macro
    def total_notes(domain=None):
        """Count markdown files under content, optionally filtered by domain."""
        count = 0
        content_dir = os.path.join(env.project_dir, 'content')
        if domain:
            start_dir = os.path.join(content_dir, domain)
        else:
            start_dir = content_dir
            
        if not os.path.isdir(start_dir):
            return 0
            
        for root, dirs, files in os.walk(start_dir):
            for file in files:
                if file.endswith('.md'):
                    if file == 'index.md' or file.startswith('_'):
                        continue
                    count += 1
        return count

    @env.macro
    def domain_summary():
        """Get summary info for each top-level domain directory under content/."""
        summary = []
        content_dir = os.path.join(env.project_dir, 'content')
        if not os.path.isdir(content_dir):
            return []
            
        # Iterate over sorted directories under content/
        for item in sorted(os.listdir(content_dir)):
            if item not in DOMAIN_FOLDERS:
                continue
            dom_path = os.path.join(content_dir, item)
            if not os.path.isdir(dom_path):
                continue
                
            # Default values from DOMAIN_META
            defaults = DOMAIN_META.get(item, {})
            name = item.replace('-', ' ').title()
            description = defaults.get('description', '')
            icon = defaults.get('icon', '●')
            
            # Check for _domain.yml or _subject.yml metadata
            meta = {}
            for meta_file in ('_domain.yml', '_subject.yml'):
                meta_path = os.path.join(dom_path, meta_file)
                if os.path.isfile(meta_path):
                    try:
                        with open(meta_path, 'r', encoding='utf-8') as f:
                            meta = yaml.safe_load(f) or {}
                        break
                    except Exception as e:
                        print(f"Error reading {meta_path}: {e}")
                        
            name = meta.get('name', name)
            description = meta.get('description', description)
            icon = meta.get('icon', icon)
            
            # Walk files and calculate counts
            note_count = 0
            complete_count = 0
            
            for root, dirs, files in os.walk(dom_path):
                for file in files:
                    if file.endswith('.md'):
                        if file == 'index.md' or file.startswith('_'):
                            continue
                        note_count += 1
                        
                        # Read status from frontmatter
                        filepath = os.path.join(root, file)
                        fm = parse_frontmatter(filepath)
                        status = str(fm.get('status', '')).strip().lower()
                        if status == 'complete':
                            complete_count += 1
                            
            complete_pct = int(round(complete_count / note_count * 100)) if note_count > 0 else 0
            
            summary.append({
                'name': name,
                'slug': item,
                'icon': icon,
                'note_count': note_count,
                'complete_pct': complete_pct,
                'description': description.strip() if description else ""
            })
            
        return summary

    @env.macro
    def recent_updates(n=6):
        """Get the n notes with the most recent updated: date."""
        notes = []
        content_dir = os.path.join(env.project_dir, 'content')
        if not os.path.isdir(content_dir):
            return []
            
        for root, dirs, files in os.walk(content_dir):
            for file in files:
                if file.endswith('.md'):
                    if file == 'index.md' or file.startswith('_'):
                        continue
                    
                    filepath = os.path.join(root, file)
                    fm = parse_frontmatter(filepath)
                    
                    updated_val = fm.get('updated')
                    updated_date = parse_date(updated_val)
                    
                    if updated_date:
                        rel_path = os.path.relpath(filepath, content_dir).replace(os.sep, '/')
                        # Convert .md path to clean directory URL (use_directory_urls behavior)
                        # e.g. "math/prob/notes.md" → "math/prob/notes/"
                        if rel_path.endswith('.md'):
                            clean_url = rel_path[:-3] + '/'
                        else:
                            clean_url = rel_path
                        notes.append({
                            'title': fm.get('title', file[:-3].replace('-', ' ').title()),
                            'url': clean_url,
                            'status': fm.get('status', 'draft'),
                            'difficulty': fm.get('difficulty', 'beginner'),
                            'updated_date': updated_date.strftime('%Y-%m-%d'),
                            'sort_date': updated_date
                        })
                        
        # Sort by sort_date (newest first), then fallback to title
        notes.sort(key=lambda x: (x['sort_date'], x['title']), reverse=True)
        return notes[:n]

    @env.macro
    def total_stats():
        """Return dict with notes, domains, concepts, updated_this_week."""
        content_dir = os.path.join(env.project_dir, 'content')
        if not os.path.isdir(content_dir):
            return {'notes': 0, 'domains': 0, 'concepts': 0, 'updated_this_week': 0}
            
        notes_count = 0
        domains_count = 0
        concepts_count = 0
        updated_this_week_count = 0
        
        today = datetime.now().date()
        seven_days_ago = today - timedelta(days=7)
        
        # Domains are non-hidden top-level directories (excluding _concepts)
        for item in os.listdir(content_dir):
            if item in DOMAIN_FOLDERS and os.path.isdir(os.path.join(content_dir, item)):
                domains_count += 1
                
        # Traverse for notes, concepts and updates
        for root, dirs, files in os.walk(content_dir):
            for file in files:
                if file.endswith('.md'):
                    if file == 'index.md' or file.startswith('_'):
                        continue
                        
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, content_dir).replace(os.sep, '/')
                    
                    if rel_path.startswith('_concepts/'):
                        concepts_count += 1
                    else:
                        notes_count += 1
                        
                    # Parse dates
                    fm = parse_frontmatter(filepath)
                    updated_val = fm.get('updated')
                    updated_date = parse_date(updated_val)
                    if updated_date and seven_days_ago <= updated_date <= today:
                        updated_this_week_count += 1
                        
        return {
            'notes': notes_count,
            'domains': domains_count,
            'concepts': concepts_count,
            'updated_this_week': updated_this_week_count
        }
