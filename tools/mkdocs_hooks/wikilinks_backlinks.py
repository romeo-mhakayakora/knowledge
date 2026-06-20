import os
import re
import yaml
from collections import defaultdict

# Global state for the hook (cleared on on_files)
SLUG_TO_FILE = {}
SLUG_TO_TITLE = {}
BACKLINKS = defaultdict(list)

# Statistics counters
TOTAL_WIKILINKS_FOUND = 0
TOTAL_RESOLVED = 0
UNRESOLVED_LINKS = []

def get_frontmatter_title(abs_path):
    """Extract title from frontmatter of a markdown file, falling back to None."""
    try:
        with open(abs_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                fm_data = yaml.safe_load(parts[1])
                if fm_data and 'title' in fm_data:
                    return str(fm_data['title'])
    except Exception:
        pass
    return None

def on_files(files, config):
    """Walk every markdown file, build the slug index and title index."""
    global SLUG_TO_FILE, SLUG_TO_TITLE, BACKLINKS, TOTAL_WIKILINKS_FOUND, TOTAL_RESOLVED, UNRESOLVED_LINKS
    
    SLUG_TO_FILE.clear()
    SLUG_TO_TITLE.clear()
    BACKLINKS.clear()
    
    TOTAL_WIKILINKS_FOUND = 0
    TOTAL_RESOLVED = 0
    UNRESOLVED_LINKS = []
    
    # Sort files by src_path to make the indexing order deterministic
    markdown_files = sorted([f for f in files if f.is_documentation_page()], key=lambda f: f.src_path)
    
    for file in markdown_files:
        # Determine slug: filename without extension, lowercased, spaces/underscores normalized to hyphens
        filename = os.path.basename(file.src_path)
        name_without_ext, _ = os.path.splitext(filename)
        slug = name_without_ext.lower().replace(' ', '-').replace('_', '-')
        
        # Check for duplicates
        if slug in SLUG_TO_FILE:
            print(f"Warning: Duplicate slug '{slug}' found. Paths: '{SLUG_TO_FILE[slug].src_path}' and '{file.src_path}'. Keeping first.")
        else:
            SLUG_TO_FILE[slug] = file
            # Cache the frontmatter title (or fallback to clean slug-based title)
            title = get_frontmatter_title(file.abs_src_path)
            if not title:
                title = name_without_ext.replace('-', ' ').replace('_', ' ').title()
            SLUG_TO_TITLE[slug] = title
            
    return files

def on_page_markdown(markdown, page, config, files):
    """Find and replace all [[slug]] and [[slug|Display Text]] patterns."""
    global TOTAL_WIKILINKS_FOUND, TOTAL_RESOLVED, UNRESOLVED_LINKS, BACKLINKS
    
    # Pattern to match [[slug]] or [[slug|Display Text]]
    # Group 1 is target slug, Group 2 is optional display text
    pattern = r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]'
    
    # Find current page slug
    current_filename = os.path.basename(page.file.src_path)
    current_name, _ = os.path.splitext(current_filename)
    current_slug = current_name.lower().replace(' ', '-').replace('_', '-')
    current_title = page.meta.get('title') or SLUG_TO_TITLE.get(current_slug) or page.title or current_slug
    
    def replace_wikilink(match):
        global TOTAL_WIKILINKS_FOUND, TOTAL_RESOLVED, UNRESOLVED_LINKS
        
        TOTAL_WIKILINKS_FOUND += 1
        target_slug_raw = match.group(1).strip()
        display_text = match.group(2)
        if display_text is not None:
            display_text = display_text.strip()
            
        # Normalize slug for matching
        target_slug = target_slug_raw.lower().replace(' ', '-').replace('_', '-')
        
        if target_slug in SLUG_TO_FILE:
            TOTAL_RESOLVED += 1
            target_file = SLUG_TO_FILE[target_slug]
            
            # Calculate relative path from current page's directory to target file's path
            current_dir = os.path.dirname(page.file.abs_src_path)
            rel_path = os.path.relpath(target_file.abs_src_path, current_dir)
            # Normalize to web slashes
            rel_url = rel_path.replace(os.sep, '/')
            
            # Resolve display text
            resolved_display = display_text if display_text else (SLUG_TO_TITLE.get(target_slug) or target_slug_raw)
            
            # Accumulate backlink
            # The current page links to the target_slug page
            # We record current page's title and site-root-relative url
            BACKLINKS[target_slug].append({
                'title': current_title,
                'url': page.file.url
            })
            
            return f"[{resolved_display}]({rel_url})"
        else:
            # Unresolved wikilink
            UNRESOLVED_LINKS.append((target_slug_raw, page.file.src_path))
            print(f"Warning: unresolved wikilink: [[{target_slug_raw}]] in {page.file.src_path}")
            return match.group(0)
            
    resolved_markdown = re.sub(pattern, replace_wikilink, markdown)
    return resolved_markdown

def on_page_context(context, page, config, nav):
    """Attach resolved backlinks list for the current page to the context."""
    # Find current page slug
    current_filename = os.path.basename(page.file.src_path)
    current_name, _ = os.path.splitext(current_filename)
    current_slug = current_name.lower().replace(' ', '-').replace('_', '-')
    
    # Get backlinks for current page
    sources = BACKLINKS.get(current_slug, [])
    
    # Deduplicate backlinks list by URL to avoid duplicates if a page links multiple times
    seen_urls = set()
    unique_backlinks = []
    for src in sources:
        if src['url'] not in seen_urls:
            seen_urls.add(src['url'])
            unique_backlinks.append(src)
            
    context['backlinks'] = unique_backlinks
    return context

def on_post_build(config):
    """Print build stats summary at the end."""
    unique_backlinked_pages = len(BACKLINKS)
    unresolved_list_str = ""
    if UNRESOLVED_LINKS:
        unresolved_list_str = "; Unresolved: " + ", ".join([f"[[{slug}]] in {src}" for slug, src in UNRESOLVED_LINKS])
        
    print(f"Wikilinks Summary: Total found: {TOTAL_WIKILINKS_FOUND}, resolved: {TOTAL_RESOLVED}, unresolved: {len(UNRESOLVED_LINKS)}{unresolved_list_str}, unique pages with backlinks: {unique_backlinked_pages}")
