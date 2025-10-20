import os
import zipfile

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# === Conteúdo base ===
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

# --- Notion (FR) ---
notion_md_fr = """# 📘 Plan Intensif de Français – 45 Jours

## 🎯 Objectif
Atteindre un niveau avancé en français oral et écrit en 45 jours grâce à un apprentissage structuré, une immersion et une pratique active.

## 🗓 Structure
- **Phase 1 (Jours 1–15)** : Grammaire avancée, vocabulaire thématique, écoute et répétition.
- **Phase 2 (Jours 16–30)** : Débats, production écrite, immersion média et simulations professionnelles.
- **Phase 3 (Jours 31–45)** : Pensée en français, rédaction d’articles, débats rapides et test DALF C1.

## ✅ Suivi quotidien
- 📚 Vocabulaire
- 🎧 Compréhension orale
- ✍ Écriture
- 🗣 Conversation
- 🎭 Immersion culturelle

## 🔗 Ressources
- [RFI – Journal en français facile](https://www.rfi.fr/fr/podcasts/journal-en-fran%C3%A7ais-facile/)
- [Le Monde](https://www.lemonde.fr/)
- [Quizlet – Vocabulaire](https://quizlet.com/subject/french/)
- [Tandem](https://www.tandem.net/)
- [LanguageTool](https://languagetool.org/)
"""

# --- Notion (FR+PT) ---
notion_md_frpt = """# 📘 Plano Intensivo de Francês – 45 Dias / Plan Intensif de Français – 45 Jours

## 🎯 Objectivo / Objectif
Atingir um nível avançado em francês falado e escrito em 45 dias.  
Atteindre un niveau avancé en français oral et écrit en 45 jours.

## 🗓 Estrutura / Structure
1️⃣ **Fase 1 / Phase 1 (Dias 1–15)** – Gramática avançada, vocabulário, escuta.  
2️⃣ **Fase 2 / Phase 2 (Dias 16–30)** – Debates, escrita, imersão e simulações.  
3️⃣ **Fase 3 / Phase 3 (Dias 31–45)** – Pensar em francês, artigos, debates rápidos.

## ✅ Rotina diária / Suivi quotidien
- 📚 Vocabulário / Vocabulaire  
- 🎧 Compreensão oral / Compréhension orale  
- ✍ Escrita / Écriture  
- 🗣 Conversação / Conversation  
- 🎭 Imersão cultural / Immersion culturelle

## 🔗 Recursos / Ressources
- [RFI – Jornal em francês fácil](https://www.rfi.fr/fr/podcasts/journal-en-fran%C3%A7ais-facile/)
- [Le Monde](https://www.lemonde.fr/)
- [Tandem – Conversas com nativos](https://www.tandem.net/)
- [LanguageTool – Correções automáticas](https://languagetool.org/)
"""

# --- Instruções (FR e PT) ---
instr_fr = """📘 Instructions d'importation

1. **Trello :** Importez `plan-francais-45j-trello.json` dans un tableau vide.
2. **Notion :** Importez `plan-francais-45j-notion.md` via “Importer → Markdown”.
3. Cochez vos tâches, suivez votre progression, et notez vos erreurs.
"""

instr_pt = """📘 Instruções de importação

1. **Trello:** Importe o ficheiro `plan-francais-45j-trello.json` num quadro novo.
2. **Notion:** Vá a “Importar → Markdown & CSV” e seleccione `plan-francais-45j-notion.md`.
3. Use as checklists e registe as suas anotações diariamente.
"""

# --- README (FR e PT) ---
readme_fr = """# 📦 Plan Français 45 Jours
Programme complet pour atteindre un niveau avancé en 45 jours.
Inclut Trello, Notion et ressources utiles.
"""
readme_pt = """# 📦 Plano Francês 45 Dias
Plano completo para atingir um nível avançado em 45 dias.
Inclui Trello, Notion e recursos úteis.
"""

# === Criação dos ficheiros ===
paths = {
    "fr/trello/plan-francais-45j-trello.json": trello_json,
    "fr/notion/plan-francais-45j-notion.md": notion_md_fr,
    "fr/notion/instructions-importation.txt": instr_fr,
    "fr/README.txt": readme_fr,
    "fr-pt/trello/plan-francais-45j-trello.json": trello_json,
    "fr-pt/notion/plan-francais-45j-notion.md": notion_md_frpt,
    "fr-pt/notion/instrucoes-importacao.txt": instr_pt,
    "fr-pt/README.txt": readme_pt,
}

for path, content in paths.items():
    write_file(os.path.join("plan-francais-45j", path), content)

# === Compactar ZIP ===
zip_name = "plan-francais-45j.zip"
with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk("plan-francais-45j"):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, "plan-francais-45j"))

print(f"✅ Arquivo '{zip_name}' criado com sucesso!")
print("Contém as versões FR e FR+PT prontas para Trello e Notion.")
