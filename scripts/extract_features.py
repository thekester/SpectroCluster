import os
import numpy as np
import soundfile as sf
from scipy.fft import fft, fftfreq
from scipy.stats import kurtosis, skew
from scipy.signal import welch
import pandas as pd

# Dossier contenant les signaux générés
data_folder = "data/synthetic_signals"
files = sorted(os.listdir(data_folder))  # Trier les fichiers

# Charger un fichier WAV
def load_wav(file_path):
    signal, sr = sf.read(file_path)
    return signal, sr

# Fonction d'extraction de features
def extract_features(signal, sr):
    """
    Extrait des features temporelles et fréquentielles d'un signal vibratoire.
    """
    features = {}

    # 📌 Features temporelles
    features["mean"] = np.mean(signal)
    features["std"] = np.std(signal)
    features["rms"] = np.sqrt(np.mean(signal**2))  # Root Mean Square (RMS)
    features["kurtosis"] = kurtosis(signal)
    features["skewness"] = skew(signal)

    # 📌 Analyse fréquentielle avec FFT
    N = len(signal)
    yf = np.abs(fft(signal))[:N // 2]  # Magnitude de la FFT
    xf = fftfreq(N, 1 / sr)[:N // 2]  # Fréquences associées
    features["max_freq"] = xf[np.argmax(yf)]  # Fréquence dominante
    features["mean_freq"] = np.sum(xf * yf) / np.sum(yf)  # Moyenne spectrale

    # 📌 Analyse spectrale avec PSD (densité spectrale de puissance)
    f, Pxx = welch(signal, sr, nperseg=1024)
    features["peak_psd_freq"] = f[np.argmax(Pxx)]  # Fréquence du pic spectral
    features["mean_psd"] = np.mean(Pxx)  # Moyenne de la densité spectrale de puissance

    return features

# Appliquer l'extraction de features à tous les signaux
features_list = []

for file_name in files:
    file_path = os.path.join(data_folder, file_name)
    signal, sr = load_wav(file_path)
    features = extract_features(signal, sr)
    features["file"] = file_name  # Ajouter le nom du fichier pour tracking
    features_list.append(features)

# Convertir en DataFrame
df_features = pd.DataFrame(features_list)

# Sauvegarder dans un fichier CSV
output_csv = "results/features.csv"
df_features.to_csv(output_csv, index=False)
print(f"Extraction terminée. Features sauvegardées dans {output_csv}")
