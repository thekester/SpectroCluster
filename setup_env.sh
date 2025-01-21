#!/bin/bash

echo "🔧 Installation des dépendances..."

# Vérifier si Python et pip sont installés
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 n'est pas installé. Installe-le avant de continuer."
    exit 1
fi

if ! command -v pip &> /dev/null
then
    echo "❌ pip n'est pas installé. Installe-le avant de continuer."
    exit 1
fi

# Création et activation d'un environnement virtuel
if [ ! -d "venv" ]; then
    echo "📦 Création d'un environnement virtuel 'venv'..."
    python3 -m venv venv
fi

echo "🔄 Activation de l'environnement virtuel..."
source venv/bin/activate  # Linux/macOS
# Pour Windows : venv\Scripts\activate

echo "📦 Installation des paquets..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Installation terminée !"
echo "🔹 Active l'environnement avec : source venv/bin/activate"
echo "🔹 Puis lance ton script avec : python demo.py"
