"""
Bug Detection Agent

Reviews code for:
- Logical bugs
- Runtime errors
- Edge cases
- Incorrect conditions
- Invalid indexing
"""

from pathlib import Path

from langchain_core.messages import HumanMessage

from llm import llm


def load_prompt() -> str:
    """Load the bug review prompt."""
    prompt_path = Path("prompts") / "bug.txt"

    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()


def bug_agent(state):
    """
    LangGraph node for bug detection.

    Reads:
        code
        language

    Writes:
        bug_report
    """

    prompt = load_prompt()

    language = state["language"]
    code = state["code"]

    final_prompt = f"""
{prompt}

Programming Language:
{language}

Source Code:

```{language.lower()}
{code}
"""

    response = llm.invoke(
        [HumanMessage(content=final_prompt)]
    )

    return {
        "bug_report": response.content
    }