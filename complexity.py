"""
Complexity Analysis Agent

Reviews code for:
- Time Complexity
- Space Complexity
- Algorithm efficiency
- Performance bottlenecks
- Possible optimizations
"""

from pathlib import Path

from langchain_core.messages import HumanMessage

from llm import llm


def load_prompt() -> str:
    """
    Load the complexity analysis prompt.
    """
    prompt_path = Path("prompts") / "complexity.txt"

    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()


def complexity_agent(state):
    """
    LangGraph node for complexity analysis.

    Reads:
        code
        language

    Writes:
        complexity_report
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
        "complexity_report": response.content
    }