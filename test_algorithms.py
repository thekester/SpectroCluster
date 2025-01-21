import pandas as pd
import numpy as np
import umap
import hdbscan
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Charger les features
df = pd.read_csv("features.csv")
X = df.drop(columns=["file"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Réduction de dimension avec UMAP
X_umap = umap.UMAP(n_components=2, random_state=42).fit_transform(X_scaled)

# Clustering avec HDBSCAN
clusterer = hdbscan.HDBSCAN(min_cluster_size=3)
labels = clusterer.fit_predict(X_umap)

# Ajouter les résultats
df["hdbscan_cluster"] = labels

# Visualisation
plt.scatter(X_umap[:, 0], X_umap[:, 1], c=labels, cmap="viridis", alpha=0.7)
plt.xlabel("UMAP 1")
plt.ylabel("UMAP 2")
plt.title("Clustering avec HDBSCAN et UMAP")
plt.colorbar(label="Cluster ID")
plt.show()

# Sauvegarde des résultats
df.to_csv("hdbscan_clusters.csv", index=False)
