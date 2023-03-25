# autofill_brevet
remplissage automatique de documents PDF

> Documents pdf en question :
> - 34formexa : Epreuve sol
> - 35formexa : Epreuve vol
> - 134iFormlic : Attestation début formation
> - Attestation_provisoire_ULM_133_FormExa : Attestation provisoire

<Br>

# Utilisation en local
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

# Exposition
La webapp dash est comprise dans le dossier src du repo.

L'app Dash est exposée par le biais du site [pyhtonanywhere](https://www.pythonanywhere.com).

Procédure de déploiement : suivre le [tutoriel détaillé](https://towardsdatascience.com/the-easiest-way-to-deploy-your-dash-app-for-free-f92c575bb69e).

Une fois que les fichiers sont uploadés sur pythonanywhere, ne pas oublier les quelques modifications nécessaires :
- Dans le fichier **autofill_functions.py** : il faut modifier la variable `ROOT_DIR` :
```python 
ROOT_DIR = "/home/amoreau/mysite/docs/"
```
- Dans le fichier app.py : ne pas oublier de supprimer `debug=True,` dans la commade suivante :
```python
# before : 
app.run_server(debug=True, host="0.0.0.0", port=8110)
# after : 
app.run_server(host="0.0.0.0", port=8110)
```

# GUI et standalone : 

Il est aussi possible de créer une application mac standalone pour ce projet.

Pour cela il faut créer une interface graphique. J'ai choisi le framework **customtkinter**. Cette iterface graphique permet d'apporter le support nécessaire afin de remplir les informations.
L'interface graphique est créée dans le fichier **gui_autofill.py**.

Les fonctions nécessaires à l'annotation des documents sont localisées dans le fichier **autofill_functions_tk.py**

Les fichiers principalement nécessaires sont donc localisées à la racine du repo (les documents nécessaires sont toujours localisés dans le dossier `"docs/"`).

> Bibliothèque choisie pour créer le standalone : `pyinstaller`

<Br>

## Procédure pour la création de l'app mac :

Installer la bibliothèque dans l'environnement si ce n'est pas déjà fait :
```bash
pip install pyinstaller
```
<Br>

### Création d'un fichier de spécifications `.spec` :

Le fichier .spec permet donner les spécification nécessaires à la création de l'app. Ce fichier évite notamment de passer une large liste d'options lors de la création.

Création du squelette du fichier .spec (dans un terminal):
```bash
pyinstaller --name=Brevet_ulm --windowed gui_autofill.py
```
Un fichier nommé **Brevet_ulm.spec** a du faire son apparition dans le dossier de travail.

<Br>

### Modifications du fichier **Brevet_ulm.spec** :

Après sa création, le fichier Brevet_ulm.spec doit être modifié pour mes besoins :
- Identifier la localisation de la bibliothèque customtkinter. En effet, il y a une spécificité avec cette bibliothèque : [explication ici](https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging#windows-pyinstaller-auto-py-to-exe). Pour cela il suffit donc de récupérer le chemin qui est proposé par la commande suivante :
```bash
pip show customtkinter
```
- Ajouter la liste des fichiers nécessaires au bon fonctionnemen de l'app. Ces fichiers contiennent les documents contenus dans le dossier `docs/`, les icones et la bibliothèque customtkinter :
```python
# une liste de tuples : (fichier/dosier source, cible).
added_files = [
    ('docs', 'docs'),
    ('logo0.ico', '.'), 
    ('logo0.jpg', '.'), 
    ('/Users/Adrien/Documents/paramoteur/autofill_brevet/autofill_brevet/lib/python3.9/site-packages/customtkinter', 'customtkinter'),
]

# Il faut alors aussi renseigner added_files dans le champ datas.
a = Analysis(
    ...
    datas=added_files,
    ...
)
```
- Pour ma part j'ai souhaité supprimer des dépendances présentes dans mon venv pour alléger l'app. J'ai donc créé une liste de dépendances non souhaitées et je l'ai indiqué dans le champ excludes :
```python
# Packages que j'ai choisi d'exclure
exclude_libs = [
    'black', 'IPython', 'fitz', 'jedi', 'lib2to3', 
    'markupsafe', 'parso', 'psutil', 'tornado', 'zmq'
]
# Il faut alors aussi renseigner added_files dans le champ datas.
a = Analysis(
    ...
    datas=added_files,
    ...
    excludes=exclude_libs,
    ...
)
```
- Ajout de l'icone de l'app :
```python
app = BUNDLE(
    coll,
    name='Brevet_ulm.app',
    icon='logo0.ico', # Indiquer ici le nom de l'image a utiliser.
    bundle_identifier=None,
)
```

### Créer l'application :
Une fois que toutes ces opérations réalisées, il ne reste qu'à créer l'app.
Pour cela, il suffit de lancer dans le terminal :
```bash
pyinstaller Brevet_ulm.spec
```

A ce stade 2 nouveaux dossiers sont créés : 
- build
- dist

Le dossier `dist` contient donc une app nommé `Brevet_ulm.app` dans mon cas.
Il s'agit de ce dernier fichier qui peut être distribué de manière autonome. :-).