# hdbscan_dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your processed data
# Make sure df_encoded includes 'hdbscan_cluster' column
df = pd.read_csv('clustered_data.csv')  # Or replace with actual df

# --- Sidebar ---
st.sidebar.title("Cluster Dashboard")
clusters = sorted(df['hdbscan_cluster'].unique())
selected_cluster = st.sidebar.selectbox("Choose Cluster", clusters)

# --- Main Title ---
st.title("HDBSCAN Clustering Dashboard")
st.markdown("Explore clusters from UMAP-reduced data and view cluster profiles.")

# --- Cluster Overview ---
st.subheader(f"Cluster {selected_cluster} Summary")
st.write(f"Number of Samples: {df[df['hdbscan_cluster'] == selected_cluster].shape[0]}")

# --- Show mean values of selected cluster ---
cluster_profile = df[df['hdbscan_cluster'] == selected_cluster].mean().sort_values(ascending=False)
st.dataframe(cluster_profile.head(10))

# --- Optional Plot ---
st.subheader("UMAP Cluster Visualization")
umap_data = pd.read_csv('umap_data.csv')  # Or use a saved numpy array if needed
df['umap_1'] = umap_data['umap_1']
df['umap_2'] = umap_data['umap_2']

fig, ax = plt.subplots()
sns.scatterplot(data=df, x='umap_1', y='umap_2', hue='hdbscan_cluster', palette='tab20', s=10, ax=ax, legend=False)
st.pyplot(fig)

