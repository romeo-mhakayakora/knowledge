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

<h2 class="homepage-section-label">Explore Domains</h2>

<div class="domain-grid">
{% for dom in domain_summary() %}
<a href="{{ dom.slug }}/" class="domain-card">
  <div class="domain-card-icon">{{ dom.icon }}</div>
  <div class="domain-card-body">
    <h3 class="domain-card-title">{{ dom.name }}</h3>
    <p class="domain-card-desc">{{ dom.description }}</p>
  </div>
  <div class="domain-card-footer">
    <span class="domain-card-count">{{ dom.note_count }} notes</span>
    <span class="domain-card-pct">{{ dom.complete_pct }}% complete</span>
  </div>
</a>
{% endfor %}
</div>

<h2 class="homepage-section-label">Recent Activity</h2>

<div class="activity-feed">
{% for update in recent_updates(6) %}
<a href="{{ update.url }}" class="activity-item">
  <div class="activity-dot"></div>
  <div class="activity-content">
    <span class="activity-title">{{ update.title }}</span>
    <span class="activity-meta">{{ update.status | upper }} · {{ update.updated_date }}</span>
  </div>
</a>
{% endfor %}
</div>
