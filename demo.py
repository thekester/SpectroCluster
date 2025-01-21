import os
import time
from progress_table import ProgressTable

# Liste des scripts à exécuter dans l'ordre
scripts = [
    "generate_signals.py",
    "extract_features.py",
    "clustering.py",
    "validate_clusters.py",
    "test_algorithms.py",
    "detect_outliers.py",
    "visualize_clusters.py"
]

# Initialisation de la table de progression
table = ProgressTable(
    pbar_show_progress=True,
    pbar_show_eta=True,
    default_column_width=30,
    default_header_color="bold",
)

# Ajout des colonnes
table.add_column("Étape", alignment="left", width=40)
table.add_column("Statut", alignment="center", width=20)

# Ajouter les étapes avant de commencer
table.add_rows(len(scripts), color="cyan")

# Barre de progression principale
main_pbar = table.pbar(len(scripts), show_progress=True, style="square clean green")

# Exécution des scripts avec ProgressTable
for i, script in enumerate(scripts):
    table.update("Étape", f"🔄 Exécution de {script}", row=i)
    table.update("Statut", "⏳ En cours...", row=i)

    # Exécuter le script
    os.system(f"python {script}")
    
    # Mise à jour du statut
    table.update("Statut", "✅ Terminé", row=i)
    main_pbar.update()

    # Mettre à jour la ligne dans la table et passer à la suivante
    table.next_row()

    time.sleep(1)

# Finalisation
table.close()
print("\n🎉 Toutes les analyses sont terminées ! Lancez `visualize_clusters.py` pour explorer les résultats.")
