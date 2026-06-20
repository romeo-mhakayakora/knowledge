---
title: Welcome
hide:
  - navigation
  - toc
---

# Knowledge Base

Welcome to your centralized knowledge management system. Explore domains, subjects, and concepts organized hierarchically for continuous learning.

{% set stats = total_stats() %}
<div class="meta-line homepage-stats">
  {{ stats.notes }} notes &middot; {{ stats.domains }} domains &middot; {{ stats.concepts }} concepts &middot; updated {{ stats.updated_this_week }} this week
</div>

<h2 class="homepage-section-label">Domains</h2>

<div class="domain-list">
{% for dom in domain_summary() %}
<div class="domain-row">
  <a href="{{ dom.slug }}/" class="domain-link">{{ dom.name }}</a>
  <span class="domain-count">{{ dom.note_count }} notes</span>
</div>
{% endfor %}
</div>

<h2 class="homepage-section-label">Recently Updated</h2>

<div class="recent-updates-list">
{% for update in recent_updates(6) %}
<div class="recent-update-row">
  <div class="recent-update-left">
    <a href="{{ update.url }}" class="recent-update-link">{{ update.title }}</a>
    <span class="recent-update-meta">({{ update.status | upper }} &middot; {{ update.difficulty | upper }})</span>
  </div>
  <span class="recent-update-date">Updated {{ update.updated_date }}</span>
</div>
{% endfor %}
</div>
