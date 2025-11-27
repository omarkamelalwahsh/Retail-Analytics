import json
from agent.graph_hybrid import LangGraph

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=str, required=True)
    parser.add_argument("--out", type=str, required=True)
    args = parser.parse_args()

    with open(args.batch, "r", encoding="utf-8") as f:
        questions = [json.loads(line) for line in f]

    graph = LangGraph()
    outputs = []

    for q in questions:
        res = graph.run_question(q["question"])
        outputs.append({"id": q["id"], **res})

    with open(args.out, "w", encoding="utf-8") as f:
        for line in outputs:
            f.write(json.dumps(line) + "\n")

    print(f"Outputs written to {args.out}")

if __name__ == "__main__":
    main()
