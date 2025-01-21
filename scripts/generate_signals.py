import numpy as np
import soundfile as sf
import os
import time
from progress_table import ProgressTable

# Paramètres de simulation
sample_rate = 2000      # en Hz (> 1 kHz comme spécifié)
duration = 5.0          # durée de chaque signal en secondes
num_signals = 10        # nombre de signaux à générer
output_folder = "data/synthetic_signals"

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_folder, exist_ok=True)

def generate_vibratory_signal(sample_rate, duration, freqs, amplitudes, noise_level=0.01):
    """
    Génère un signal vibratoire synthétique.
    - freqs : liste de fréquences sinusoïdales en Hz
    - amplitudes : liste d'amplitudes correspondantes
    - noise_level : niveau du bruit additif
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.zeros_like(t)
    for freq, amp in zip(freqs, amplitudes):
        signal += amp * np.sin(2 * np.pi * freq * t)
    # Ajouter du bruit aléatoire
    noise = noise_level * np.random.normal(0, 1, signal.shape)
    return signal + noise

# Initialisation de ProgressTable
table = ProgressTable(
    pbar_show_progress=True,
    pbar_show_throughput=False,
    pbar_show_eta=True,
    default_column_width=15,
    default_header_color="bold",
)

# Ajout de la colonne de statut
table.add_column("Status", alignment="center", width=30)

# Ajout de lignes vides pour éviter l'erreur
table.add_rows(num_signals, color="blue")

# Création d'une barre de progression principale
main_pbar = table.pbar(
    num_signals, position=1, show_progress=True, style="square clean blue"
)

# Générer plusieurs signaux avec des caractéristiques variées
for i in range(num_signals):
    # Choisir aléatoirement des fréquences et amplitudes
    freqs = np.random.choice(np.linspace(10, 500, 50), size=3, replace=False)
    amplitudes = np.random.uniform(0.5, 1.5, size=len(freqs))
    
    # Générer le signal
    signal = generate_vibratory_signal(sample_rate, duration, freqs, amplitudes, noise_level=0.02)
    
    # Sauvegarder le signal sous forme de fichier WAV
    filename = os.path.join(output_folder, f"signal_{i+1}.wav")
    sf.write(filename, signal, sample_rate)
    
    # Simuler un temps de génération pour voir la barre de progression
    time.sleep(0.1)

    # Mise à jour du statut de la ligne i
    table.update("Status", f"✅ Signal {i+1}/{num_signals} généré", row=i)

    # Mise à jour de la barre principale
    main_pbar.update()

# Finaliser la table de progression
table.close()

# Vérification : Charger et afficher des informations sur un fichier généré
test_file = os.path.join(output_folder, "signal_1.wav")
signal, sr = sf.read(test_file)
print(f"\nFichier '{test_file}' chargé : {len(signal)} échantillons à {sr} Hz.")
