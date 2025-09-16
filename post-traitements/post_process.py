import spacy
import re

# Charger le modèle spaCy pour le français.
# Ce modèle a été téléchargé et inclus dans l'image Docker lors de la construction.
try:
    nlp = spacy.load("fr_core_news_sm")
except OSError:
    print("Modèle 'fr_core_news_sm' non trouvé. Assurez-vous de l'avoir téléchargé.")
    print("Exécutez : python -m spacy download fr_core_news_sm")
    exit()

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def clean_text(text):
    """Nettoie les espaces superflus dans le texte."""
    return re.sub(r'\s+', ' ', text).strip()


def process_text(file_path):
    """Lit, nettoie et analyse le texte du fichier d'entrée."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()
    except FileNotFoundError:
        print(f"Erreur : Le fichier d'entrée '{file_path}' n'a pas été trouvé.")
        return

    print("--- Texte Original (sortie brute du LM) ---")
    print(raw_text)

    # 1. Étape de nettoyage simple
    cleaned_text = clean_text(raw_text)
    print("\n--- Texte Nettoyé ---")
    print(cleaned_text)

    # 2. Traitement NLP avec spaCy pour l'analyse
    doc = nlp(cleaned_text)

    # 3. Extraction des informations structurées
    print("\n--- Analyse du Texte ---")

    print("\n[Phrases Détectées]")
    for i, sent in enumerate(doc.sents):
        print(f"  Phrase {i + 1}: {sent.text}")

    print("\n[Entités Nommées Détectées]")
    if doc.ents:
        for ent in doc.ents:
            print(f"- Entité: '{ent.text}', Type: {ent.label_}")
    else:
        print("Aucune entité nommée n'a été détectée.")

    # 4. Sauvegarde du résultat traité
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("--- Texte Nettoyé ---\n")
        f.write(cleaned_text + "\n\n")
        f.write("--- Entités Nommées ---\n")
        if doc.ents:
            for ent in doc.ents:
                f.write(f"- Entité: '{ent.text}', Type: {ent.label_}\n")

    print(f"\nLe résultat du post-traitement a été sauvegardé dans '{OUTPUT_FILE}'")


if __name__ == "__main__":
    process_text(INPUT_FILE)
