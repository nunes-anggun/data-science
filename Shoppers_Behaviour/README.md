# Shoppers Behavior Clustering with HDBSCAN

This project applies unsupervised machine learning techniques to identify patterns in online shopper behavior. By using clustering algorithms like K-Means, DBSCAN, and HDBSCAN along with dimensionality reduction techniques (PCA, t-SNE, UMAP), we uncover natural groupings in customer session data.

A simple interactive dashboard is built using **Streamlit** to explore clusters and feature patterns.

---

## Project Highlights

- ✅ Unsupervised Learning with clustering
- ✅ Compared multiple methods: K-Means, DBSCAN, HDBSCAN
- ✅ Best performance: **HDBSCAN with Silhouette Score = 0.754**
- ✅ Applied dimensionality reduction: PCA, t-SNE, UMAP
- ✅ Built a dashboard with **Streamlit** to visualize clusters

---

## 🔍 Dataset Overview

The dataset is from Kaggle.
The dataset contains online shopping session data with the following features:

- **Numerical**: Page durations, BounceRates, ExitRates, PageValues
- **Categorical**: VisitorType, Browser, Region, TrafficType
- **Target (for EDA)**: `Revenue` (not used in clustering)

Total features used after encoding: **~60**

---

## Clustering Techniques Used

| Algorithm  | Description                     | Clusters Found | Silhouette Score |
|------------|---------------------------------|----------------|------------------|
| K-Means    | Centroid-based, fixed `k`       | 4              | 0.373            |
| DBSCAN     | Density-based, auto cluster num | 109            | 0.551            |
| HDBSCAN    | Hierarchical DBSCAN             | 308            | **0.754** ✅      |

---

## Dashboard (Streamlit)

An interactive web app was built using Streamlit to:

- Explore cluster profiles
- Visualize UMAP-reduced clusters in 2D
- View top features for each cluster

To run the dashboard:

```bash
streamlit run hdbscan_dashboard.py
```

## How to Reproduce

1. Clone the repo

2. Install dependencies: pip install -r requirements.txt

3. Run hdbscan_dashboard.py with Streamlit

4. Explore clustering results in your browser!


 ## About Me 

I'm a data enthusiast with a background in mathematics and data science, passionate about turning raw data into meaningful insights through machine learning and visualization.

Connect with me on LinkedIn or check out more projects on my GitHub.

## License 

This project is licensed under the MIT License.

