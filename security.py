"""
Security Review Agent

Reviews code for:
- Hardcoded credentials
- SQL Injection
- Command Injection
- Unsafe eval()/exec()
- Buffer overflow
- Path Traversal
- Unsafe file handling
- Insecure deserialization
- Secrets/API keys
"""

from pathlib import Path

from langchain_core.messages import HumanMessage

from llm import llm


def load_prompt() -> str:
    """
    Load the security review prompt.
    """
    prompt_path = Path("prompts") / "security.txt"

    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()


def security_agent(state):
    """
    LangGraph node for security analysis.

    Reads:
        code
        language

    Writes:
        security_report
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
        "security_report": response.content
    }