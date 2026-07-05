from langgraph.graph import StateGraph, START, END

from state import ReviewState

from agents.supervisor import supervisor
from agents.bug import bug_agent
from agents.complexity import complexity_agent
from agents.style import style_agent
from agents.security import security_agent
from agents.aggregator import aggregator_agent


builder = StateGraph(ReviewState)

# -------------------------
# Add Nodes
# -------------------------

builder.add_node("Supervisor", supervisor)
builder.add_node("Bug", bug_agent)
builder.add_node("Complexity", complexity_agent)
builder.add_node("Style", style_agent)
builder.add_node("Security", security_agent)

# Synchronization node
builder.add_node("Merge", lambda state: state)

builder.add_node("Aggregator", aggregator_agent)

# -------------------------
# Build Graph
# -------------------------

builder.add_edge(START, "Supervisor")

# Fan-out
builder.add_edge("Supervisor", "Bug")
builder.add_edge("Supervisor", "Complexity")
builder.add_edge("Supervisor", "Style")
builder.add_edge("Supervisor", "Security")

# Fan-in
builder.add_edge("Bug", "Merge")
builder.add_edge("Complexity", "Merge")
builder.add_edge("Style", "Merge")
builder.add_edge("Security", "Merge")

builder.add_edge("Merge", "Aggregator")

builder.add_edge("Aggregator", END)

graph = builder.compile()