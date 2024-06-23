import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from IPython.display import Image, display

from langgraph.graph import StateGraph, END

import utils
from data_classes.book_summarizer_state import BookSummarizerState
from llm_agents.relevant_chapter_selector import AgentRelevantChaptersSelector
from llm_agents.section_summarizer import AgentSectionSummarizer
from llm_agents.summaries_aggregator import AgentSummariesAggregator
from non_llm_agents.epub_loader import AgentEpubLoader
from non_llm_agents.chapters_loader import AgentChaptersLoader
from non_llm_agents.results_reporter import AgentResultsReporter
from non_llm_agents.chapter_router import AgentChapterRouter

def get_multi_agent_summarizer_graph():
    # Set API Keys 
    os.environ["OPENAI_API_KEY"] = utils.get_openai_api_key()
    os.environ["TAVILY_API_KEY"] = utils.get_tavily_api_key()

    graph = StateGraph(BookSummarizerState)

    graph.add_node("Epub Loader", AgentEpubLoader())
    graph.add_node("Relevant Chapters Selector", AgentRelevantChaptersSelector())
    graph.add_node("Chapters Loader", AgentChaptersLoader())
    graph.add_node("Section Summarizer", AgentSectionSummarizer())
    graph.add_node("Summaries Aggregator", AgentSummariesAggregator())
    graph.add_node("Results Reporter", AgentResultsReporter())

    graph.set_entry_point("Epub Loader")
    graph.add_edge("Epub Loader", "Relevant Chapters Selector")
    graph.add_edge("Relevant Chapters Selector", "Chapters Loader")
    graph.add_conditional_edges("Chapters Loader", AgentChapterRouter(), ["Section Summarizer"])
    graph.add_edge("Section Summarizer", "Summaries Aggregator")
    graph.add_edge("Summaries Aggregator", "Results Reporter")
    graph.add_edge("Results Reporter", END)

    return graph

if __name__ == "__main__":
    graph = get_multi_agent_summarizer_graph()
    app = graph.compile()
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))
