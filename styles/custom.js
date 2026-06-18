/* Custom JavaScript for enhanced functionality */

document.addEventListener('DOMContentLoaded', function() {
  
  // Process wikilinks
  const content = document.querySelector('article');
  if (content) {
    processWikilinks(content);
  }
  
  // Add copy buttons to code blocks
  addCopyButtons();
  
  // Enhance table of contents
  enhanceTOC();
});

function processWikilinks(element) {
  // Find all potential wikilinks in the text
  const walker = document.createTreeWalker(
    element,
    NodeFilter.SHOW_TEXT,
    null,
    false
  );
  
  const textNodes = [];
  let node;
  while (node = walker.nextNode()) {
    if (node.textContent.includes('[[')) {
      textNodes.push(node);
    }
  }
  
  // Process wikilinks in text nodes
  textNodes.forEach(node => {
    const span = document.createElement('span');
    span.innerHTML = node.textContent
      .replace(/\[\[([^\]]+)\]\]/g, '<a class="wikilink" href="#$1">$1</a>');
    node.parentNode.replaceChild(span, node);
  });
}

function addCopyButtons() {
  document.querySelectorAll('pre').forEach(pre => {
    const button = document.createElement('button');
    button.className = 'copy-button';
    button.textContent = 'Copy';
    button.style.position = 'absolute';
    button.style.top = '0.5rem';
    button.style.right = '0.5rem';
    button.style.padding = '0.25rem 0.5rem';
    button.style.fontSize = '0.75rem';
    button.style.cursor = 'pointer';
    
    button.addEventListener('click', function() {
      const code = pre.textContent;
      navigator.clipboard.writeText(code).then(() => {
        button.textContent = 'Copied!';
        setTimeout(() => {
          button.textContent = 'Copy';
        }, 2000);
      });
    });
    
    pre.style.position = 'relative';
    pre.appendChild(button);
  });
}

function enhanceTOC() {
  const toc = document.querySelector('nav.toc');
  if (toc) {
    toc.addEventListener('click', function(e) {
      if (e.target.tagName === 'A') {
        // Smooth scroll
        const target = document.querySelector(e.target.hash);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  }
}
