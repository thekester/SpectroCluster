import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Charger les features extraites
features_file = "features.csv"
df = pd.read_csv(features_file)

# Supprimer la colonne "file" et normaliser les données
X = df.drop(columns=["file"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 📌 Appliquer K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["kmeans_cluster"] = kmeans.fit_predict(X_scaled)

# 📌 Appliquer DBSCAN
dbscan = DBSCAN(eps=1.5, min_samples=2)
df["dbscan_cluster"] = dbscan.fit_predict(X_scaled)

# 📌 Appliquer GMM
gmm = GaussianMixture(n_components=3, random_state=42)
df["gmm_cluster"] = gmm.fit_predict(X_scaled)

# 📌 Réduction de dimension pour visualisation avec PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
df["pca1"] = X_pca[:, 0]
df["pca2"] = X_pca[:, 1]

# 📌 Visualisation des clusters (K-Means)
plt.figure(figsize=(8, 6))
plt.scatter(df["pca1"], df["pca2"], c=df["kmeans_cluster"], cmap="viridis", alpha=0.7)
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.title("Clustering des signaux vibratoires (K-Means)")
plt.colorbar(label="Cluster ID")
plt.show()

# Sauvegarder les résultats des clusters
df.to_csv("clustered_features.csv", index=False)
print("Clustering terminé. Résultats sauvegardés dans clustered_features.csv")
