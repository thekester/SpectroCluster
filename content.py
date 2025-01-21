import os

# Nom du fichier où seront stockés tous les contenus
output_file = "tous_contenus.txt"

# Ouvrir le fichier de sortie en mode écriture
with open(output_file, "w", encoding="utf-8") as outfile:
    # Parcourir récursivement tous les répertoires à partir du répertoire courant
    for root, dirs, files in os.walk("."):
        # Exclure les répertoires nommés "venv"
        if "venv" in dirs:
            dirs.remove("venv")  # Cela empêche os.walk de parcourir ce dossier

        # Parcourir tous les fichiers dans le répertoire courant
        for file in files:
            chemin = os.path.join(root, file)
            try:
                # Lire le contenu du fichier en ignorant les erreurs d'encodage éventuelles
                with open(chemin, "r", encoding="utf-8", errors="ignore") as infile:
                    contenu = infile.read()
                # Écrire dans le fichier de sortie le chemin du fichier et son contenu
                outfile.write(f"--- Début du fichier: {chemin} ---\n")
                outfile.write(contenu)
                outfile.write(f"\n--- Fin du fichier: {chemin} ---\n\n")
            except Exception as e:
                # En cas d'erreur (ex. fichier binaire), on affiche un message et on continue
                print(f"Erreur lors de la lecture de {chemin}: {e}")
