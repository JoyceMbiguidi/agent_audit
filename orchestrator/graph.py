
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.profiler import profiler_node


class AgentState(TypedDict, total=False):
    file_path: str #contient le fichier à analyser.
    profile: dict #contient le résultat produit par le Profiler.


def build_graph():

    workflow = StateGraph(AgentState)

    # Déclaration du noeud
    workflow.add_node("profiler", profiler_node)

    # Définition du workflow
    workflow.add_edge(START, "profiler")
    workflow.add_edge("profiler", END)

    # Compilation
    return workflow.compile()


graph = build_graph()
