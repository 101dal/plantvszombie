#!/bin/bash

# Vérifier si le nombre d'arguments est correct
if [ "$#" -ne 1 ]; then
    echo "Utilisation : $0 <répertoire>"
    exit 1
fi

# Vérifier si le répertoire existe
if [ ! -d "$1" ]; then
    echo "Erreur : Le répertoire '$1' n'existe pas."
    exit 1
fi

# Créer le fichier de sortie (ou écraser son contenu s'il existe déjà)
> all_files.txt

# Parcourir récursivement le répertoire et lister les fichiers Python (sauf all.sh et .git)
find "$1" -type f \( -name "*.py" ! -name "all.sh" ! -name "all_files.txt" ! -path "*/.git/*" ! -path "*/assets/*" \) -exec bash -c '
    echo "nom: $(basename "$0")" >> all_files.txt
    echo "-----" >> all_files.txt
    cat "$0" >> all_files.txt
    echo "" >> all_files.txt
    echo "-----" >> all_files.txt
' {} \;

echo "La liste des fichiers Python et leur contenu ont été enregistrés dans 'all_files.txt'."
