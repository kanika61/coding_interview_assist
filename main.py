from retrieval.ingest import ingest_dsa_docs
from graph import app

def run(problem: str, user_code: str, intent: str, hint_level: int = 1):
    initial_state = {
        "problem":           problem,
        "user_code":         user_code,
        "language":          "python",
        "hint_level":        hint_level,
        "retrieved_context": "",
        "hint_output":       None,
        "evaluation_output": None,
        "complexity_output": None,
        "messages":          [],
        "next_agent":        intent,
    }

    result = app.invoke(initial_state)

    if intent == "hint":
        return result["hint_output"]
    elif intent == "evaluator":
        return result["evaluation_output"]
    elif intent == "complexity":
        return result["complexity_output"]

def get_multiline_input(prompt: str) -> str:
    print(prompt)
    print("(When done, type END on a new line and press Enter)")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    print("\n" + "="*60)
    print("   CODING INTERVIEW AGENT")
    print("="*60)
    print("Powered by Llama 3.2 + ChromaDB — 100% free & offline")
    print("="*60 + "\n")

    # Ingest DSA docs on first run
    ingest_dsa_docs()

    # Get the problem once per session
    problem = get_multiline_input("\nPaste your DSA problem below:")
    print("\nProblem saved!\n")

    while True:
        print("\n" + "-"*40)
        print("What do you want to do?")
        print("  1. Get a hint")
        print("  2. Evaluate my solution")
        print("  3. Analyze complexity")
        print("  4. Change problem")
        print("  5. Exit")
        print("-"*40)

        choice = input("Enter choice (1-5): ").strip()

        if choice == "5":
            print("\nGood luck with your interviews!\n")
            break

        elif choice == "4":
            problem = get_multiline_input("\nPaste your new DSA problem:")
            print("\nProblem updated!\n")

        elif choice in ("1", "2", "3"):
            user_code = get_multiline_input("\nPaste your current code (or just END if you have none):")

            if choice == "1":
                print("\nHint level:")
                print("  1 = Gentle nudge (no spoilers)")
                print("  2 = Name the algorithm")
                print("  3 = Near-solution pseudocode")
                level = input("Choose level (1/2/3): ").strip()
                level = int(level) if level in ("1", "2", "3") else 1

                print("\nThinking...\n")
                output = run(problem, user_code, intent="hint", hint_level=level)
                print("\n HINT ".center(40, "-"))
                print(output)

            elif choice == "2":
                print("\nEvaluating your solution...\n")
                output = run(problem, user_code, intent="evaluator")
                print("\n EVALUATION ".center(40, "-"))
                print(output)

            elif choice == "3":
                print("\nAnalyzing complexity...\n")
                output = run(problem, user_code, intent="complexity")
                print("\n COMPLEXITY ANALYSIS ".center(40, "-"))
                print(output)

        else:
            print("Invalid choice, please enter 1-5.")

if __name__ == "__main__":
    main()
