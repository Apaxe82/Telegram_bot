import os
import zipfile

# Estrutura de diretórios
base_dir = "plan-francais-45j"
trello_dir = os.path.join(base_dir, "trello")
notion_dir = os.path.join(base_dir, "notion")

# Criar pastas
os.makedirs(trello_dir, exist_ok=True)
os.makedirs(notion_dir, exist_ok=True)

# --- Conteúdo Trello (simplificado) ---
trello_json = """{
  "name": "Plan Français 45 Jours",
  "desc": "Programme intensif pour atteindre un niveau avancé de français (expression orale et écrite).",
  "lists": [
    {"name": "Phase 1 – Immersion et Structure (Jours 1–15)", "cards": []},
    {"name": "Phase 2 – Simulation et Intensification (Jours 16–30)", "cards": []},
    {"name": "Phase 3 – Maîtrise et Immersion Totale (Jours 31–45)", "cards": []}
  ]
}
"""
with open(os.path.join(trello_dir, "plan-francais-45j-trello.json"), "w", encoding="utf-8") as f:
    f.write(trello_json)

# --- Conteúdo Notion (Markdown) ---
notion_md = """# 📘 Plan Intensif de Français – 45 Jours

## 🎯 Objectif
Atteindre un niveau avancé en français oral et écrit en 45 jours grâce à un apprentissage structuré, une immersion et une pratique active.

---

## 🗓 Structure
- **Phase 1 (Jours 1–15)** : Grammaire avancée, vocabulaire thématique, écoute et répétition.
- **Phase 2 (Jours 16–30)** : Débats, production écrite, immersion média et simulations professionnelles.
- **Phase 3 (Jours 31–45)** : Pensée en français, rédaction d’articles, débats rapides et test DALF C1.

---

## ✅ Suivi quotidien
Chaque jour :
- 📚 **Vocabulaire**
- 🎧 **Compréhension orale**
- ✍ **Écriture**
- 🗣 **Conversation**
- 🎭 **Immersion culturelle**

---

## 🔗 Ressources principales
- [RFI – Journal en français facile](https://www.rfi.fr/fr/podcasts/journal-en-fran%C3%A7ais-facile/)
- [Le Monde](https://www.lemonde.fr/)
- [Le Figaro](https://www.lefigaro.fr/)
- [Quizlet – Vocabulaire](https://quizlet.com/subject/french/)
- [Tandem](https://www.tandem.net/)
- [Italki](https://www.italki.com/)
- [LanguageTool](https://languagetool.org/)

---

## 🧭 Conseils
- Pensez, écrivez et parlez en français chaque jour.
- Corrigez vos erreurs avec LanguageTool ou un natif.
- Écoutez des podcasts pendant vos déplacements.
- Notez 10 nouveaux mots chaque jour.
"""

with open(os.path.join(notion_dir, "plan-francais-45j-notion.md"), "w", encoding="utf-8") as f:
    f.write(notion_md)

# --- Instruções de importação ---
instructions = """📘 Instructions d'importation

1. **Trello :**
   - Ouvrez Trello → Créer un tableau vide.
   - Installez l’extension “Trello JSON Importer” (ou utilisez l’API).
   - Importez le fichier `plan-francais-45j-trello.json`.

2. **Notion :**
   - Ouvrez Notion → Créez une nouvelle page.
   - Cliquez sur “Importer” → “Markdown & CSV”.
   - Sélectionnez `plan-francais-45j-notion.md`.
   - Le modèle complet sera importé (vous pouvez le dupliquer).

3. **Profitez du plan !**
   - Cochez vos tâches chaque jour.
   - Ajoutez vos notes et votre progression.
"""

with open(os.path.join(notion_dir, "instructions-importation.txt"), "w", encoding="utf-8") as f:
    f.write(instructions)

# --- README ---
readme = """# 📦 Plan Français 45 Jours

Ce dossier contient le plan complet pour progresser rapidement en français :
- Fichiers pour Trello et Notion
- Ressources utiles
- Instructions d'importation

Auteur : André Paxe
Langue : Français
Durée : 45 jours
Objectif : Niveau avancé oral + écrit
"""

with open(os.path.join(base_dir, "README.txt"), "w", encoding="utf-8") as f:
    f.write(readme)

# --- Compactar em ZIP ---
zip_name = "plan-francais-45j.zip"
with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(base_dir):
        for file in files:
            path = os.path.join(root, file)
            zipf.write(path, os.path.relpath(path, base_dir))

print(f"✅ Fichier '{zip_name}' créé avec succès dans le répertoire courant.")
