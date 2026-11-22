
from tools.data_quality import run_quality_checks


def quality_node(state: dict) -> dict:
    """
    Noeud LangGraph responsable des contrôles qualité.
    """

    file_path = state["file_path"]

    print("\n[QUALITY] Contrôle de la qualité des données...")

    report = run_quality_checks(file_path)

    print(
        f"[QUALITY] {report['total_issues']} type(s) "
        "d'anomalie détecté(s)."
    )

    return {
        "quality_report": report
    }

