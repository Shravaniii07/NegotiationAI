from langgraph.graph import StateGraph, END
from agents.analyzer_agent import analyze
from agents.personality_agent import detect_personality
from agents.strategy_agent import decide_strategy
from agents.generator_agent import generate_reply
from agents.research_agent import research_vendors
from typing import TypedDict

class AgentState(TypedDict):
    input: str
    mode: str  # 'dojo' or 'procurement'
    persona: str 
    analysis: str
    personality: str
    strategy: str
    reply: str
    scorecard: dict
    vendor_list: list  # New field for procurement
    draft_emails: list # New field for procurement

def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("analyze", analyze)
    workflow.add_node("detect_personality", detect_personality)
    workflow.add_node("decide_strategy", decide_strategy)
    workflow.add_node("research", research_vendors)
    workflow.add_node("generate_reply", generate_reply)

    workflow.set_entry_point("analyze")
    workflow.add_edge("analyze", "detect_personality")
    workflow.add_edge("detect_personality", "decide_strategy")
    workflow.add_edge("decide_strategy", "research")
    workflow.add_edge("research", "generate_reply")
    workflow.add_edge("generate_reply", END)

    return workflow.compile()
