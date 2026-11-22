# Agent Audit

Projet multi-agents d'audit automatisé de la qualité des données.

## Stack technique

- Python
- LangGraph
- Ollama
- Docker

## Objectif

Automatiser le profiling, le contrôle qualité et l'analyse métier de fichiers de données.

## Etapes
1. Créer arborescence projet
2. Compléter fichier "requirements.txt"
3. python -m venv .venv #creer venv
4. .\.venv\Scripts\Activate.ps1 #activer venv
5. python -m pip install --upgrade pip #installe les bibliotheques
6. pip install -r requirements.txt #installe les bibliotheques
7. python -c "import langgraph; import langchain_ollama; import pandas; import dotenv; print('Toutes les dépendances sont opérationnelles.')" #permet de vérifier les installations
8. Principe à comprendre :
    - Ollama exécute le modèle de langage.
    - LangChain Ollama fournit l'interface Python pour communiquer avec ce modèle.
    - LangGraph organise les étapes et les interactions entre agents.
    - Pandas exécute les opérations de données.
9. Créations d'agents IA :
    - Agent IA "profiler" : explorer un fichier CSV et produire un profil statistique
      - Précision : Pour cette première version, le profiling sera déterministe : nous n'utiliserons pas encore de LLM. Nous allons d'abord construire le workflow LangGraph et valider son fonctionnement. Ensuite, nous ajouterons la capacité de raisonnement avec Ollama.
      - Doit identifier :
        - Le nombre de lignes et de colonnes.
        - Les types de variables.
        - Les valeurs manquantes.
        - Les valeurs distinctes.
        - Les doublons.
        - Quelques valeurs représentatives.
      - compléter tools/data_quality.py (vérifie simplement les données)
      - créer le premier noeud Profiler en complétant agents/profiler.py
      - construire premier workflow LangGraph en complétant orchestrator/graph.py
      - compléter fichier data/samples/clients.csv
      - Préicion : le Profiler ne détectera pas encore que l'email est incorrect ou que l'âge est négatif. Il se contente de décrire les données. C'est précisément le rôle que nous donnerons ensuite à l'agent Quality.
      - Créer le point d'entrée en complétant agent_audit/main.py. Notre application est maintenant exécutable.
      - A la racine, dans le cmd exécute : python main.py