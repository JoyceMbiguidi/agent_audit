from tools.data_quality import profile_csv


def profiler_node(state: dict) -> dict:
    """
    Noeud LangGraph responsable du profiling.
    """

    file_path = state["file_path"]

    print(f"\n[PROFILER] Analyse du fichier : {file_path}")

    profile = profile_csv(file_path) #Récupère le chemin du fichier depuis l'état.

    print("[PROFILER] Analyse terminée.")

    return {
        "profile": profile #Retourne le résultat à LangGraph.
    }

