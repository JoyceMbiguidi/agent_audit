
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.profiler import profiler_node
from agents.quality import quality_node

class AgentState(TypedDict, total=False):
    file_path: str #contient le fichier à analyser.
    profile: dict #contient le résultat produit par le Profiler.
    quality_report: dict #contient le rapport produit par le Quality Checker.


def build_graph():

    workflow = StateGraph(AgentState)

    # Déclaration du noeud
    workflow.add_node("profiler", profiler_node)
    workflow.add_node("quality", quality_node)

    # Définition du workflow
    workflow.add_edge(START, "profiler")
    workflow.add_edge("profiler", "quality")
    workflow.add_edge("quality", END)

    # Compilation
    return workflow.compile()


graph = build_graph()
