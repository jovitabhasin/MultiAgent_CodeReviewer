from typing import TypedDict


class ReviewState(TypedDict):
    """
    Shared state passed between all LangGraph agents.
    """

    # User Input
    code: str

    # Filled by Supervisor
    language: str

    # Filled by Review Agents
    bug_report: str
    complexity_report: str
    style_report: str
    security_report: str

    # Filled by Aggregator
    final_report: str