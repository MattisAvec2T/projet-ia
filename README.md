# Projet IA

## Technologies Utilisées & Prérequis

- Python3
- Ollama (Installer _[ici](https://ollama.com/download)_)

## Setup

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/MattisAvec2T/projet-ia.git
    cd projet-ia
    ```

2. Se déplacer dans /app :
    ```bash
    cd app
    ```

### Construire avec Makefile

1. **Créer et activer l'environnement virtuel :**
    Si vous voulez utiliser un environnement virtuel :
    ```bash
    make venv
    ```
    Pour l'activer, faites :
    ```bash
    source .venv/bin/activate
    ```

2. **Installer les dépendances :**
    ```bash
    make requirement
    ```

3. **Télécharger les modèles Ollama :**
    ```bash
    make ollama
    ```

### Construire sans Makefile

1. **Créer et activer l'environnement virtuel :**
    Si vous voulez utiliser un environnement virtuel :
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. **Installer les dépendances :**
    ```bash
    pip install -r requirement.txt
    pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/nightly/cpu \
        torch \
        torchvision \
        torchaudio
    ```

3. **Télécharger les modèles Ollama :**
    ```bash
    ollama pull llama3
    ollama pull mxbai-embed-large
    ```

## Démarrer le pojet :

```bash
python3 app.py
```

Les options de lancement de app.py
```bash
options:
  -h, --help            show this help message and exit
  --model MODEL         Ollama model to use (default: llama3)
  --rag                 Start script with rag (enabled by default)
  --no-rag              Start script with no rag
  --temperature TEMPERATURE
                        Temperature used by Ollama (0-1, default: 0.1)
```

examples :

```bash
python3 app.py --no-rag
````

```bash
python3 app.py --temperature 0.6
```

### Désactiver le venv :
```bash
deactivate
```

## Auteur

- [Mattis Almeida Lima](https://github.com/MattisAvec2T)
