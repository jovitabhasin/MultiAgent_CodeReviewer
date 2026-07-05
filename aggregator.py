"""
Aggregator Agent

Combines the outputs from all review agents into a
single comprehensive code review.
"""

from pathlib import Path

from langchain_core.messages import HumanMessage

from llm import llm


def load_prompt() -> str:
    """
    Prompt used by the aggregator.
    """

    return """
You are a Senior Staff Software Engineer.

You have received reports from four expert reviewers:

1. Bug Detection Expert
2. Complexity Expert
3. Style Expert
4. Security Expert

Your job is to merge them into ONE professional report.

Do NOT invent issues.

Produce a well-structured markdown report.

Use this format:

# Code Review Report

## Overall Score
Give a score out of 10.

## Executive Summary
2-4 sentences.

## Bug Analysis

(summarize)

## Complexity Analysis

(summarize)

## Style Analysis

(summarize)

## Security Analysis

(summarize)

## Priority Fixes

List the most important fixes first.

## Final Verdict

Excellent / Good / Fair / Poor
"""
    

def aggregator_agent(state):
    """
    LangGraph node.

    Reads:
        bug_report
        complexity_report
        style_report
        security_report

    Writes:
        final_report
    """

    prompt = load_prompt()

    final_prompt = f"""
{prompt}

--------------------------------------
BUG REPORT
--------------------------------------

{state['bug_report']}

--------------------------------------
COMPLEXITY REPORT
--------------------------------------

{state['complexity_report']}

--------------------------------------
STYLE REPORT
--------------------------------------

{state['style_report']}

--------------------------------------
SECURITY REPORT
--------------------------------------

{state['security_report']}
"""

    response = llm.invoke(
        [HumanMessage(content=final_prompt)]
    )

    return {
        "final_report": response.content
    }