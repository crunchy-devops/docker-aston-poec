# Étape 1: Utiliser une image Python de base, légère et optimisée.
FROM python:3.10-slim

# Étape 2: Définir le répertoire de travail dans le conteneur.
WORKDIR /app

# Étape 3: Copier le fichier des dépendances et les installer.
# Cette copie séparée permet de profiter du cache de Docker : si requirements.txt ne change pas,
# cette étape (qui peut être longue) n'est pas ré-exécutée lors des builds suivants.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 4: Télécharger le modèle linguistique spaCy requis.
# Cette étape est cruciale pour inclure le modèle directement dans l'image,
# la rendant ainsi totalement autonome.
RUN python -m spacy download fr_core_news_sm

# Étape 5: Copier le reste du code de l'application (le script et ses données).
COPY post_process.py .
COPY input.txt .

# Étape 6: Définir la commande par défaut qui sera exécutée au lancement du conteneur.
CMD ["python", "post_process.py"]
