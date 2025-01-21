import pandas as pd
import numpy as np
import soundfile as sf
import os
import matplotlib.pyplot as plt
import sys

if not os.path.exists("clustered_features.csv"):
    print("Erreur : Le fichier 'clustered_features.csv' est introuvable. Veuillez exécuter 'clustering.py' d'abord.")
    sys.exit(1)

# Charger les clusters
df = pd.read_csv("clustered_features.csv")
data_folder = "synthetic_signals"

# Sélectionner aléatoirement un exemple de chaque cluster
unique_clusters = df["kmeans_cluster"].unique()
plt.figure(figsize=(10, 6))

for i, cluster in enumerate(unique_clusters):
    example_file = df[df["kmeans_cluster"] == cluster].sample(1)["file"].values[0]
    file_path = os.path.join(data_folder, example_file)
    signal, sr = sf.read(file_path)
    t = np.linspace(0, len(signal) / sr, num=len(signal))

    plt.subplot(len(unique_clusters), 1, i + 1)
    plt.plot(t, signal)
    plt.title(f"Exemple du cluster {cluster}")
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
