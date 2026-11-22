
import json

from orchestrator.graph import graph


def main():

    initial_state = {
        "file_path": "data/samples/clients.csv"
    }

    print("================================")
    print("       DATAAUDIT AI")
    print("================================")

    result = graph.invoke(initial_state)

    print("\n=== PROFILING RESULT ===")

    print(
        json.dumps(
            result["profile"],
            indent=4,
            ensure_ascii=False
        )
    )
    
    print("\n=== QUALITY REPORT ===")

    print(
       json.dumps(
           result["quality_report"],
           indent=4,
           ensure_ascii=False
       )
    )


if __name__ == "__main__":
    main()
