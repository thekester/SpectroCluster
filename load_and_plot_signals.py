import os
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

# Dossier contenant les signaux générés
data_folder = "synthetic_signals"
files = sorted(os.listdir(data_folder))  # Trier les fichiers pour les charger dans l'ordre

# Charger un fichier WAV
def load_wav(file_path):
    signal, sr = sf.read(file_path)
    return signal, sr

# Afficher les signaux
def plot_signals(file_list, num_files=3):
    plt.figure(figsize=(10, 6))
    
    for i, file_name in enumerate(file_list[:num_files]):
        file_path = os.path.join(data_folder, file_name)
        signal, sr = load_wav(file_path)
        t = np.linspace(0, len(signal) / sr, num=len(signal))

        plt.subplot(num_files, 1, i+1)
        plt.plot(t, signal, label=f"{file_name}")
        plt.xlabel("Temps (s)")
        plt.ylabel("Amplitude")
        plt.title(f"Signal {file_name}")
        plt.legend()

    plt.tight_layout()
    plt.show()

# Affichage des 3 premiers signaux
plot_signals(files, num_files=3)
