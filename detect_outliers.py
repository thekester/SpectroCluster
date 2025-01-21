import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Charger les features
df = pd.read_csv("features.csv")
X = df.drop(columns=["file"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Appliquer DBSCAN
dbscan = DBSCAN(eps=1.5, min_samples=2)
labels = dbscan.fit_predict(X_scaled)

# Ajouter les résultats
df["dbscan_cluster"] = labels

# Identifier les outliers (-1 est la classe des anomalies dans DBSCAN)
outliers = df[df["dbscan_cluster"] == -1]
print(f"Nombre d'outliers détectés : {len(outliers)}")

# Visualisation
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap="plasma", alpha=0.7)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Détection des outliers avec DBSCAN")
plt.colorbar(label="Cluster ID")
plt.show()

# Sauvegarde
df.to_csv("outliers_detected.csv", index=False)
