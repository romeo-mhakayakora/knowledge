---
title: Welcome
hide:
  - navigation
  - toc
---

{% set stats = total_stats() %}

<div class="hero">
  <div class="hero-inner">
    <div class="hero-badge">Personal Knowledge System</div>
    <h1 class="hero-title">Knowledge</h1>
    <p class="hero-subtitle">A multi-domain learning repository spanning mathematics, computer science, AI, economics, physics, systems, and business — organized for deep, connected understanding.</p>
    <div class="hero-stats">
      <div class="hero-stat">
        <span class="hero-stat-value">{{ stats.notes }}</span>
        <span class="hero-stat-label">Notes</span>
      </div>
      <div class="hero-stat">
        <span class="hero-stat-value">{{ stats.domains }}</span>
        <span class="hero-stat-label">Domains</span>
      </div>
      <div class="hero-stat">
        <span class="hero-stat-value">{{ stats.concepts }}</span>
        <span class="hero-stat-label">Concepts</span>
      </div>
    </div>
  </div>
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

<div class="activity-feed">
{% for update in recent_updates(6) %}
<a href="{{ update.url }}" class="activity-item">
  <div class="activity-content">
    <span class="activity-title">{{ update.title }}</span>
    <span class="activity-meta">{{ update.status | upper }} · {{ update.updated_date }}</span>
  </div>
</a>
{% endfor %}
</div>
