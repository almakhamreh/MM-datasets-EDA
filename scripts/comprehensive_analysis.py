import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import gc

# Configure plotting
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Define output directories (relative to scripts/)
PLOT_DIR = os.path.join("..", "results", "plots")
METRICS_DIR = os.path.join("..", "results", "metrics")

# Ensure output directories exist
os.makedirs(PLOT_DIR, exist_ok=True)
os.makedirs(METRICS_DIR, exist_ok=True)

# Dataset paths
datasets = {
    "Phish360": r"Z:\parquet files\phish360_phish.parquet",
    "PWD2016": r"Z:\parquet files\PWD2016_phish.parquet",
    "PhishIntention": r"Z:\parquet files\PhishIntention_phish.parquet",
    "PILWD-134K": r"Z:\parquet files\PILWD-134K_phish.parquet",
    "VanNL126k": r"Z:\parquet files\VanNL126k_phish.parquet"
}

print("="*80)
print("COMPREHENSIVE ANTI-PHISHING DATASET BENCHMARKING")
print("="*80)

# =============================================================================
# METRIC 1: Content Uniqueness vs URL Uniqueness
# =============================================================================
print("\n[1/7] Analyzing Content Uniqueness...")
uniqueness_metrics = []

for name, path in datasets.items():
    if not os.path.exists(path):
        print(f"  [SKIP] {name} - File not found")
        continue
    
    print(f"  Processing {name}...")
    stats = {"Dataset": name}
    
    # URL analysis
    df = pd.read_parquet(path, columns=['URL'])
    stats["Total Samples"] = len(df)
    stats["Unique URLs"] = df['URL'].nunique()
    stats["URL Uniqueness %"] = round((stats["Unique URLs"] / stats["Total Samples"]) * 100, 2)
    del df
    gc.collect()
    
    # Text analysis
    df = pd.read_parquet(path, columns=['BeautifulSoup_text'])
    stats["Unique Content (Text)"] = df['BeautifulSoup_text'].nunique()
    stats["Content Uniqueness %"] = round((stats["Unique Content (Text)"] / stats["Total Samples"]) * 100, 2)
    del df
    gc.collect()
    
    uniqueness_metrics.append(stats)

df_uniqueness = pd.DataFrame(uniqueness_metrics)
print("\n" + df_uniqueness.to_markdown(index=False))

# Visualization
plot_data = df_uniqueness.melt(id_vars="Dataset", 
                               value_vars=["Total Samples", "Unique Content (Text)"], 
                               var_name="Metric", value_name="Count")

plt.figure(figsize=(14, 7))
ax = sns.barplot(data=plot_data, x="Dataset", y="Count", hue="Metric", palette="viridis")
plt.title("Dataset Size vs. True Content Uniqueness", fontsize=16, fontweight='bold')
plt.ylabel("Number of Samples", fontsize=12)
plt.xlabel("Dataset", fontsize=12)
for container in ax.containers:
    ax.bar_label(container, fmt='%d')
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "plot1_uniqueness.png"), dpi=300)
print(f"  ✓ Saved: {os.path.join(PLOT_DIR, 'plot1_uniqueness.png')}")
plt.close()

# =============================================================================
# METRIC 2: Brand Coverage
# =============================================================================
print("\n[2/7] Analyzing Brand Coverage...")
brand_metrics = []

for name, path in datasets.items():
    if not os.path.exists(path):
        continue
    
    print(f"  Processing {name}...")
    df = pd.read_parquet(path, columns=['brand'])
    
    unique_brands = df['brand'].nunique()
    top_brands = df['brand'].value_counts().head(5).to_dict()
    
    brand_metrics.append({
        "Dataset": name,
        "Unique Brands": unique_brands,
        "Top Brands": top_brands
    })
    
    del df
    gc.collect()

df_brands = pd.DataFrame(brand_metrics)
print("\n" + df_brands[['Dataset', 'Unique Brands']].to_markdown(index=False))

# Visualization
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=df_brands, x="Dataset", y="Unique Brands", palette="mako")
plt.title("Brand Diversity Across Datasets", fontsize=16, fontweight='bold')
plt.ylabel("Number of Unique Brands", fontsize=12)
plt.xlabel("Dataset", fontsize=12)
for container in ax.containers:
    ax.bar_label(container, fmt='%d')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "plot2_brands.png"), dpi=300)
print(f"  ✓ Saved: {os.path.join(PLOT_DIR, 'plot2_brands.png')}")
plt.close()

# =============================================================================
# METRIC 3: Linguistic Diversity
# =============================================================================
print("\n[3/7] Analyzing Linguistic Diversity...")
language_metrics = []

for name, path in datasets.items():
    if not os.path.exists(path):
        continue
    
    print(f"  Processing {name}...")
    df = pd.read_parquet(path, columns=['BeautifulSoup_text_language'])
    
    unique_langs = df['BeautifulSoup_text_language'].nunique()
    top_langs = df['BeautifulSoup_text_language'].value_counts().head(5).to_dict()
    
    language_metrics.append({
        "Dataset": name,
        "Unique Languages": unique_langs,
        "Top Languages": top_langs
    })
    
    del df
    gc.collect()

df_languages = pd.DataFrame(language_metrics)
print("\n" + df_languages[['Dataset', 'Unique Languages']].to_markdown(index=False))

# Visualization
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=df_languages, x="Dataset", y="Unique Languages", palette="rocket")
plt.title("Linguistic Diversity Across Datasets", fontsize=16, fontweight='bold')
plt.ylabel("Number of Unique Languages", fontsize=12)
plt.xlabel("Dataset", fontsize=12)
for container in ax.containers:
    ax.bar_label(container, fmt='%d')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "plot3_languages.png"), dpi=300)
print(f"  ✓ Saved: {os.path.join(PLOT_DIR, 'plot3_languages.png')}")
plt.close()

# =============================================================================
# METRIC 4: Data Completeness (Multimodal Integrity)
# =============================================================================
print("\n[4/7] Analyzing Data Completeness...")
completeness_metrics = []

for name, path in datasets.items():
    if not os.path.exists(path):
        continue
    
    print(f"  Processing {name}...")
    
    # Check Image
    df = pd.read_parquet(path, columns=['image_path'])
    total = len(df)
    image_complete = (df['image_path'].notna().sum() / total) * 100
    del df
    gc.collect()
    
    # Check HTML
    df = pd.read_parquet(path, columns=['full_html'])
    html_complete = (df['full_html'].notna().sum() / total) * 100
    del df
    gc.collect()
    
    # Check Text
    df = pd.read_parquet(path, columns=['BeautifulSoup_text'])
    text_complete = (df['BeautifulSoup_text'].notna().sum() / total) * 100
    del df
    gc.collect()
    
    completeness_metrics.append({
        "Dataset": name,
        "Image %": round(image_complete, 2),
        "HTML %": round(html_complete, 2),
        "Text %": round(text_complete, 2)
    })

df_completeness = pd.DataFrame(completeness_metrics)
print("\n" + df_completeness.to_markdown(index=False))

# Heatmap visualization
plt.figure(figsize=(10, 6))
heatmap_data = df_completeness.set_index('Dataset')[['Image %', 'HTML %', 'Text %']]
sns.heatmap(heatmap_data, annot=True, fmt='.1f', cmap='RdYlGn', vmin=0, vmax=100, cbar_kws={'label': 'Completeness %'})
plt.title("Multimodal Data Completeness", fontsize=16, fontweight='bold')
plt.ylabel("Dataset", fontsize=12)
plt.xlabel("Modality", fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "plot4_completeness.png"), dpi=300)
print(f"  ✓ Saved: {os.path.join(PLOT_DIR, 'plot4_completeness.png')}")
plt.close()

# =============================================================================
# METRIC 5: URL Characteristics (TLD, SSL)
# =============================================================================
print("\n[5/7] Analyzing URL Characteristics...")
url_metrics = []

for name, path in datasets.items():
    if not os.path.exists(path):
        continue
    
    print(f"  Processing {name}...")
    
    # TLD analysis
    df = pd.read_parquet(path, columns=['TLD'])
    top_tlds = df['TLD'].value_counts().head(5).to_dict()
    del df
    gc.collect()
    
    # SSL analysis
    df = pd.read_parquet(path, columns=['SSL'])
    total = len(df)
    ssl_ratio = (df['SSL'].sum() / total) * 100 if 'SSL' in df.columns else 0
    del df
    gc.collect()
    
    url_metrics.append({
        "Dataset": name,
        "SSL %": round(ssl_ratio, 2),
        "Top TLDs": top_tlds
    })

df_url = pd.DataFrame(url_metrics)
print("\n" + df_url[['Dataset', 'SSL %']].to_markdown(index=False))

# SSL Visualization
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=df_url, x="Dataset", y="SSL %", palette="Blues_d")
plt.title("SSL Usage in Phishing URLs", fontsize=16, fontweight='bold')
plt.ylabel("% of URLs with HTTPS", fontsize=12)
plt.xlabel("Dataset", fontsize=12)
plt.ylim(0, 100)
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "plot5_ssl.png"), dpi=300)
print(f"  ✓ Saved: {os.path.join(PLOT_DIR, 'plot5_ssl.png')}")
plt.close()

# =============================================================================
# METRIC 6: Text Extraction Quality
# =============================================================================
print("\n[6/7] Analyzing Text Extraction Quality...")
extraction_metrics = []

for name, path in datasets.items():
    if not os.path.exists(path):
        continue
    
    print(f"  Processing {name}...")
    df = pd.read_parquet(path, columns=['BeautifulSoup_text', 'trafilatura_text'])
    
    total = len(df)
    bs_success = (df['BeautifulSoup_text'].notna().sum() / total) * 100
    tf_success = (df['trafilatura_text'].notna().sum() / total) * 100
    
    extraction_metrics.append({
        "Dataset": name,
        "BeautifulSoup %": round(bs_success, 2),
        "Trafilatura %": round(tf_success, 2)
    })
    
    del df
    gc.collect()

df_extraction = pd.DataFrame(extraction_metrics)
print("\n" + df_extraction.to_markdown(index=False))

# Visualization
plot_data = df_extraction.melt(id_vars="Dataset", 
                               value_vars=["BeautifulSoup %", "Trafilatura %"], 
                               var_name="Method", value_name="Success Rate %")

plt.figure(figsize=(12, 6))
ax = sns.barplot(data=plot_data, x="Dataset", y="Success Rate %", hue="Method", palette="Set2")
plt.title("Text Extraction Success Rates", fontsize=16, fontweight='bold')
plt.ylabel("Success Rate (%)", fontsize=12)
plt.xlabel("Dataset", fontsize=12)
plt.ylim(0, 105)
plt.xticks(rotation=15)
plt.legend(title="Extraction Method")
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "plot6_extraction.png"), dpi=300)
print(f"  ✓ Saved: {os.path.join(PLOT_DIR, 'plot6_extraction.png')}")
plt.close()

# =============================================================================
# METRIC 7: Summary Export
# =============================================================================
print("\n[7/7] Generating Summary Report...")

# Save all metrics to CSV
df_uniqueness.to_csv(os.path.join(METRICS_DIR, "metrics_uniqueness.csv"), index=False)
df_brands[['Dataset', 'Unique Brands']].to_csv(os.path.join(METRICS_DIR, "metrics_brands.csv"), index=False)
df_languages[['Dataset', 'Unique Languages']].to_csv(os.path.join(METRICS_DIR, "metrics_languages.csv"), index=False)
df_completeness.to_csv(os.path.join(METRICS_DIR, "metrics_completeness.csv"), index=False)
df_url[['Dataset', 'SSL %']].to_csv(os.path.join(METRICS_DIR, "metrics_ssl.csv"), index=False)
df_extraction.to_csv(os.path.join(METRICS_DIR, "metrics_extraction.csv"), index=False)

print("\n✓ All metrics exported to CSV files")
print("\n" + "="*80)
print("ANALYSIS COMPLETE - 6 plots and 6 CSV files generated")
print(f"  Plots: {PLOT_DIR}")
print(f"  Metrics: {METRICS_DIR}")
print("="*80)
