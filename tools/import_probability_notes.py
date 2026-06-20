import os
import re
import subprocess
import yaml

# Path configurations
PROB_NOTES_DIR = r"C:\Users\romeo\.gemini\antigravity-ide\scratch\probability-notes"
KNOWLEDGE_CONTENT_DIR = r"C:\Users\romeo\.gemini\antigravity-ide\scratch\knowledge\content"

chapter_mapping = {
    'ch01-probability-counting': '02-probability-counting',
    'ch02-conditional-probability': '03-conditional-probability',
    'ch03-random-variables': '04-random-variables',
    'ch04-expectation': '05-expectation',
    'ch05-continuous-rvs': '06-continuous-random-variables',
    'ch06-moments': '07-moments',
    'ch07-joint-distributions': '08-joint-distributions',
    'ch08-transformations': '09-transformations',
    'ch09-conditional-expectation': '10-conditional-expectation',
    'ch10-inequalities-limit-theorems': '11-inequalities-limit-theorems',
    'ch11-markov-chains': '12-markov-chains',
    'ch12-markov-chain-monte-carlo': '13-markov-chain-monte-carlo',
    'ch13-poisson-processes': '14-poisson-processes'
}

def run_git_cmd(args):
    """Run a git command in the probability-notes directory and return output."""
    result = subprocess.run(
        ['git'] + args,
        cwd=PROB_NOTES_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8'
    )
    if result.returncode != 0:
        raise RuntimeError(f"Git command failed: {result.stderr}")
    return result.stdout

def get_frontmatter_and_clean_content(content, default_title, subject, chapter, status_val):
    """Generate frontmatter and strip the first H1 header from the markdown body."""
    title = default_title
    
    # Try to find first H1 header
    h1_match = re.search(r'^#\s+(.*)$', content, re.MULTILINE)
    if h1_match:
        extracted_title = h1_match.group(1).strip()
        # Clean any markdown links/formatting from header title
        extracted_title = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', extracted_title)
        extracted_title = extracted_title.replace('**', '').replace('*', '').replace('`', '')
        # Handle Blitzstein book subtitle or chapter number formatting in H1
        if '—' in extracted_title:
            extracted_title = extracted_title.split('—')[-1].strip()
        elif 'Lecture' in extracted_title and '—' in extracted_title:
            extracted_title = extracted_title.split('—')[-1].strip()
        
        if extracted_title:
            title = extracted_title
            
        # Strip the H1 header from the content to avoid double titles in MkDocs Material
        # We replace the first H1 header line with empty string
        content = re.sub(r'^#\s+.*$', '', content, count=1, flags=re.MULTILINE)
        
    frontmatter = {
        'title': title,
        'subject': subject,
        'chapter': chapter,
        'tags': ['probability', 'mathematics'],
        'date': '2026-06-18',
        'updated': '2026-06-19',
        'status': status_val,
        'difficulty': 'intermediate'
    }
    
    # Special tags/status rules
    if 'exercise' in default_title.lower() or 'ps' in default_title.lower():
        frontmatter['tags'] = ['probability', 'exercises']
    elif chapter == '_concepts':
        frontmatter['tags'] = ['probability', 'concept-guide']
        
    fm_str = "---\n" + yaml.dump(frontmatter, default_flow_style=False, sort_keys=False) + "---\n"
    return fm_str + content.strip()

def sanitize_filename(filename):
    """Sanitize filename to follow kebab-case and be Windows compatible."""
    # Sanitize colons and special characters for Windows compatibility
    filename = filename.replace(':', ' -').replace('&', 'and').replace(' ', '-')
    filename = filename.lower()
    # Replace multiple hyphens with a single hyphen
    filename = re.sub(r'-+', '-', filename)
    return filename

def main():
    print("Listing files in probability-notes commit history...")
    files_list_str = run_git_cmd(['ls-tree', '-r', 'HEAD', '--name-only'])
    git_files = [f.strip() for f in files_list_str.split('\n') if f.strip()]
    
    imported_count = 0
    
    for git_path in git_files:
        if git_path in ('.gitignore', 'README.md') or git_path.endswith('.R'):
            # Skip non-content files
            continue
            
        print(f"Processing: {git_path}")
        
        # Get file contents
        file_content = run_git_cmd(['show', f'HEAD:{git_path}'])
        
        # Determine paths and categories
        parts = git_path.split('/')
        folder = parts[0]
        filename = parts[-1]
        
        # Status determined by size of content
        status_val = 'complete' if len(file_content) > 5000 else 'draft'
        
        # Destination file resolution
        if folder in chapter_mapping:
            target_chap = chapter_mapping[folder]
            dest_dir = os.path.join(KNOWLEDGE_CONTENT_DIR, 'mathematics', 'probability', target_chap)
            
            # If subfolder like lectures or problem-sets
            if len(parts) > 2:
                # E.g. lectures/L01-...
                subfolder = parts[1]
                dest_dir = os.path.join(dest_dir, subfolder)
                
            os.makedirs(dest_dir, exist_ok=True)
            
            # Rename notes.md to match the chapter slug to prevent global duplicate slugs
            if filename == 'notes.md':
                filename = f"{target_chap[3:]}-notes.md"
                
            filename = sanitize_filename(filename)
            
            dest_path = os.path.join(dest_dir, filename)
            
            # Determine default title
            clean_name = os.path.splitext(filename)[0].replace('-', ' ').title()
            
            processed_content = get_frontmatter_and_clean_content(
                file_content, clean_name, 'probability', target_chap, status_val
            )
            
        elif folder == 'concepts':
            dest_dir = os.path.join(KNOWLEDGE_CONTENT_DIR, '_concepts')
            os.makedirs(dest_dir, exist_ok=True)
            filename = sanitize_filename(filename)
            dest_path = os.path.join(dest_dir, filename)
            clean_name = os.path.splitext(filename)[0].replace('-', ' ').title()
            
            processed_content = get_frontmatter_and_clean_content(
                file_content, clean_name, 'concepts', '_concepts', status_val
            )
            
        elif folder == 'problem-sets':
            dest_dir = os.path.join(KNOWLEDGE_CONTENT_DIR, 'mathematics', 'probability', 'problem-sets')
            os.makedirs(dest_dir, exist_ok=True)
            filename = sanitize_filename(filename)
            dest_path = os.path.join(dest_dir, filename)
            clean_name = os.path.splitext(filename)[0].replace('-', ' ').title()
            
            processed_content = get_frontmatter_and_clean_content(
                file_content, clean_name, 'probability', 'problem-sets', status_val
            )
            
        else:
            print(f"Skipping unknown folder: {folder}")
            continue
            
        # Write file
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(processed_content)
        print(f"[Imported] {dest_path}")
        imported_count += 1
        
    # Write _chapter.yml for each mapping to make navigation robust
    print("Generating _chapter.yml meta files...")
    for folder, target_chap in chapter_mapping.items():
        chap_dir = os.path.join(KNOWLEDGE_CONTENT_DIR, 'mathematics', 'probability', target_chap)
        if os.path.isdir(chap_dir):
            chap_title = target_chap[3:].replace('-', ' ').title()
            # If the title is "Continuous Rvs", clean it up
            if chap_title == "Continuous Rvs":
                chap_title = "Continuous Random Variables"
            
            chap_meta = {
                'title': chap_title,
                'chapter': target_chap
            }
            with open(os.path.join(chap_dir, '_chapter.yml'), 'w', encoding='utf-8') as f:
                yaml.dump(chap_meta, f, default_flow_style=False)
                
    print(f"Import process complete! Successfully migrated {imported_count} files.")

if __name__ == '__main__':
    main()
