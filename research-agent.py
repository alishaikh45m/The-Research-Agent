import os
from typing import TypedDict
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import StateGraph, END

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)
search_tool = TavilySearchResults(
    max_results=5,
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)

class AgentState(TypedDict):
    topic: str
    articles: list
    analysis: str
    summary: str

def search_node(state: AgentState):
    print(f"🔍 Searching for: {state['topic']}")
    results = search_tool.invoke(state['topic'])
    return {"articles": results}

def analyst_node(state: AgentState):
    print("📊 Analyzing articles...")
    context = "\n".join([f"Source: {a['url']}\nContent: {a['content']}" for a in state['articles']])
    # prompt = f"Tech Analyst: Extract stats and viewpoints for '{state['topic']}' from:\n{context}"
    # response = llm.invoke(prompt)
    return {"analysis": context}

def writer_node(state: AgentState):
    print("Writing summary...")
    prompt = f"Technical Writer: Create a Markdown summary for '{state['topic']}' using this analysis:\n{state['analysis']}"
    response = llm.invoke(prompt)
    return {"summary": response.content}

# Construct the Graph
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("searcher", search_node)
workflow.add_node("analyst", analyst_node)
workflow.add_node("writer", writer_node)

# Set the flow (Linear sequence)
workflow.set_entry_point("searcher")
workflow.add_edge("searcher", "analyst")
workflow.add_edge("analyst", "writer")
workflow.add_edge("writer", END)

# Compile
app = workflow.compile()

# Run it
if __name__ == "__main__":
    user_input = input("Enter a tech trend: ") or "Impact of AI on Cybersecurity"
    
    # Run the graph
    final_state = app.invoke({"topic": user_input})
    
    print("\n" + "="*50)
    print("FINAL REPORT")
    print("="*50 + "\n")
    print(final_state["summary"])