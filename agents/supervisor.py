"""
supervisor.py

The Supervisor Agent is the entry point of the workflow.

Responsibilities:
1. Validate the input code.
2. Detect the programming language.
3. Initialize the shared state.
"""

from utils.parser import detect_language


def supervisor(state):
    """
    LangGraph node function.

    Parameters
    ----------
    state : dict
        Current graph state.

    Returns
    -------
    dict
        Updated fields to merge into the graph state.
    """

    code = state.get("code", "").strip()

    # Empty input
    if not code:
        return {
            "language": "Unknown",
            "bug_report": "No code provided.",
            "complexity_report": "No code provided.",
            "style_report": "No code provided.",
            "security_report": "No code provided.",
            "final_report": "Error: Please provide valid source code."
        }

    # Detect programming language
    language = detect_language(code)

    print("=" * 50)
    print("Supervisor Agent")
    print("=" * 50)
    print(f"Detected Language : {language}")
    print()

    return {
        "language": language
    }
