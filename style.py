"""
Style Review Agent

Reviews code for:
- Variable naming
- Function naming
- Readability
- Formatting
- Comments
- Code duplication
- Maintainability
"""

from pathlib import Path

from langchain_core.messages import HumanMessage

from llm import llm


def load_prompt() -> str:
    """
    Load the style review prompt.
    """
    prompt_path = Path("prompts") / "style.txt"

    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()


def style_agent(state):
    """
    LangGraph node for style analysis.

    Reads:
        code
        language

    Writes:
        style_report
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
        "style_report": response.content
    }