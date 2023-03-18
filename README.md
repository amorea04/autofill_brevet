# autofill_brevet
remplissage automatique de documents PDF


## Utilisation en local
Afin d'utiliser en local, il suffit de se créer cloner le repo.
```zsh
git clone https://github.com/amorea04/autofill_brevet.git
```

Ensuite se créer un environnement de travail. (nommé autofill_brevet pour ma part).
```zsh
python3.9 -m venv autofill_brevet
```

Ajouter un kernel jupyter:
```zsh
pip install --user ipykernel         
python -m ipykernel install --user --name=autofill_brevet
```

Activer l'environnement de travail :
```zsh
source /Users/Adrien/Documents/paramoteur/autofill_brevet/autofill_brevet/bin/activate
```

Installer les dépendances :
```zsh
pip install -r requirements.txt
```

petit tips supplémentaire : rechercher les environnements de travail
```zsh
find $HOME -name "*activate" -type f
```

