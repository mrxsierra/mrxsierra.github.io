---
date:
  created: 2025-05-14
tags:
  - Machine Learning
  - Binary Classification
  - Python
  - Data Science
  - Hackathon
description: >
  National-level hackathon finalist machine learning pipeline analyzing 900,000+ real-world GST records with XGBoost, LightGBM, and SHAP explainability.
---

# GSTN Predictive Binary Classification

<div class="project-header-card">
  <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px;">
    <div>
      <span class="project-category-badge">Machine Learning • Competition Finalist</span>
      <h2 style="margin: 6px 0 0 0; font-size: 22px; font-weight: 700;">GSTN AI/ML Analytics Challenge</h2>
    </div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
      <a href="https://github.com/mrxsierra/gstn_dsp_pbc" target="_blank" rel="noopener" class="btn btn-primary">
        <i class="fab fa-github"></i> Repository
      </a>
      <a href="../../cert/GSTN_Team_137.jpg" class="btn btn-secondary" target="_blank">
        <i class="fas fa-award"></i> Certificate
      </a>
    </div>
  </div>

  <div class="project-meta-grid">
    <div class="project-meta-item">
      <span class="project-meta-label">Role</span>
      <span class="project-meta-val">Solo ML Engineer &amp; Lead</span>
    </div>
    <div class="project-meta-item">
      <span class="project-meta-label">Timeline</span>
      <span class="project-meta-val">Aug 2024 – Oct 2024 (45 Days)</span>
    </div>
    <div class="project-meta-item">
      <span class="project-meta-label">Dataset Scale</span>
      <span class="project-meta-val">900,000+ Records (21 Attributes)</span>
    </div>
    <div class="project-meta-item">
      <span class="project-meta-label">Primary Stack</span>
      <span class="project-meta-val">Python, XGBoost, LightGBM, SHAP</span>
    </div>
  </div>

  <div class="project-impact-box">
    <i class="fas fa-trophy"></i>
    <span><strong>Finalist Selection:</strong> Ranked among the top 17 finalist teams out of 200+ national participating teams as a single-member solo developer.</span>
  </div>
</div>

---

## Architecture &amp; ML Pipeline Flow

```mermaid
graph TD
    A["900,000+ Anonymized GST Records"] --> B["Data Integrity Validation (SHA256)"]
    B --> C["Pre-processing &amp; Imputation (Median / Winsorization)"]
    C --> D["Class Imbalance Remediation (RUS + scale_pos_weight)"]
    D --> E["Stratified 5-Fold Nested Cross-Validation"]
    E --> F["Ensemble Modeling (XGBoost + LightGBM)"]
    F --> G["Threshold Tuning for F1 Optimization"]
    G --> H["SHAP Feature Interpretability Analysis"]
    H --> I["Competition-Compliant Model Artifact"]
```

---

## Executive Overview

Developed for the **Goods and Services Tax Network (GSTN) AI/ML Hackathon** organized by the Government of India, this project engineered a high-throughput, interpretable binary classification pipeline for GST financial tax analytics.

The challenge required building an accurate predictive model $F_\theta(X) \to Y_{\text{pred}}$ over 900,000 real-world records characterized by severe class imbalance (91% majority / 9% minority) and extreme feature skewness, while adhering to strict zero-data-leakage compliance protocols.

---

## Technical Challenges &amp; Architectural Solutions

### 1. Severe Class Imbalance (91% / 9%)
- **Challenge:** Standard loss functions biased predictions toward the majority class, causing unacceptably low minority recall.
- **Solution:** Evaluated Random Under-Sampling (RUS), SMOTE, and tuned gradient boosted `scale_pos_weight` parameters to systematically optimize the Precision-Recall trade-off, maximizing both F1 and Matthews Correlation Coefficient (MCC).

### 2. Extreme Missingness &amp; Heavy-Tailed Skewness
- **Challenge:** Multiple tax feature columns exhibited >50% missing values and extreme financial outliers.
- **Solution:** Applied strict feature pruning thresholds, robust median imputation, and two-sided Winsorization to normalize distribution tails without sacrificing variance.

### 3. Data Leakage &amp; Generalization Safeguards
- **Challenge:** Risk of subtle data leakage across feature engineering and hyperparameter search.
- **Solution:** Enforced strict nested cross-validation and pipeline encapsulation (scikit-learn `Pipeline`) ensuring preprocessing transformations were fitted exclusively on training splits.

---

## Performance &amp; Evaluation Metrics

| Evaluation Metric | Cross-Validation Score | Test Partition Score | Objective |
|:---|:---|:---|:---|
| **Accuracy** | 97.6% | **~97.8%** | Global classification correctness |
| **F1 Score** | 0.884 | **~0.891** | Harmonic mean of precision and recall |
| **MCC (Matthews Correlation)** | 0.875 | **~0.880** | Balanced quality metric for imbalanced classes |
| **ROC-AUC** | 0.988 | **~0.990** | Separability threshold performance |

---

## Diagnostic Visualizations

<div class="card-grid-2" style="margin: 20px 0;">
  <div>
    <h4 style="margin: 0 0 8px 0;">Precision-Recall Curve</h4>
    <img src="https://raw.githubusercontent.com/mrxsierra/gstn_dsp_pbc/main/3-submission/static/prc.png" alt="Precision-Recall Curve" style="border-radius: 8px; border: 1px solid var(--color-border);" loading="lazy">
  </div>
  <div>
    <h4 style="margin: 0 0 8px 0;">Confusion Matrix</h4>
    <img src="https://raw.githubusercontent.com/mrxsierra/gstn_dsp_pbc/main/3-submission/static/cm.png" alt="Confusion Matrix" style="border-radius: 8px; border: 1px solid var(--color-border);" loading="lazy">
  </div>
</div>

---

## Verified Accreditation

<div style="max-width: 650px; margin: 20px 0;">
  <a href="../../cert/GSTN_Team_137.jpg" class="glightbox" data-gallery="certs" data-title="GSTN National Hackathon Finalist Certificate">
    <img src="../../cert/GSTN_Team_137.jpg" alt="GSTN Hackathon Finalist Certificate" style="border-radius: 8px; border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);" loading="lazy">
  </a>
  <p style="font-size: 12.5px; color: var(--color-text-muted); margin-top: 6px; text-align: center;">
    GSTN AI/ML National Hackathon Finalist • Awarded by Goods &amp; Services Tax Network (GSTN)
  </p>
</div>

---

## Source Repository

- [GitHub Repository — mrxsierra/gstn_dsp_pbc](https://github.com/mrxsierra/gstn_dsp_pbc): Complete reproduction scripts, cross-validation benches, and documentation.

---

<!-- Sequential Case Study Navigation -->
<div class="project-nav-footer">
  <a href="../" class="project-nav-card">
    <span class="project-nav-dir"><i class="fas fa-arrow-left"></i> Portfolio</span>
    <span class="project-nav-title">All Engineering Projects</span>
  </a>
  <a href="../ems-db/" class="project-nav-card" style="text-align: right;">
    <span class="project-nav-dir" style="justify-content: flex-end;">Next Project <i class="fas fa-arrow-right"></i></span>
    <span class="project-nav-title">Examination Management System DB</span>
  </a>
</div>
