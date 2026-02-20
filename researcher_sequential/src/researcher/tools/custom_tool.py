from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os

class SearchInput(BaseModel):
    """Input for search tool."""
    query: str = Field(..., description="Search query to look up on the internet")

class TavilySearchTool(BaseTool):
    name: str = "tavily_search"
    description: str = "Search the internet using Tavily API for current information, news, research papers, and market data"
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
        """Execute the search query using Tavily API."""
        try:
            from tavily import TavilyClient
            
            api_key = os.getenv("TAVILY_API_KEY")
            if not api_key:
                return "Error: TAVILY_API_KEY not found in environment variables"
            
            client = TavilyClient(api_key=api_key)
            results = client.search(
                query=query, 
                max_results=5,
                search_depth="basic"
            )
            
            formatted = []
            for r in results.get('results', []):
                formatted.append(
                    f"**Title:** {r.get('title')}\n"
                    f"**URL:** {r.get('url')}\n"
                    f"**Content:** {r.get('content')}\n"
                )
            
            return "\n---\n".join(formatted) if formatted else "No results found"
            
        except ImportError:
            return "Error: tavily-python package not installed. Run: uv pip install tavily-python"
        except Exception as e:
            return f"Error searching: {str(e)}"

class AdvancedSearchTool(BaseTool):
    name: str = "advanced_tavily_search"
    description: str = "Advanced search focusing on academic sources like arxiv.org and nature.com for in-depth research"
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
        """Execute advanced search with focus on academic sources."""
        try:
            from tavily import TavilyClient
            
            api_key = os.getenv("TAVILY_API_KEY")
            if not api_key:
                return "Error: TAVILY_API_KEY not found in environment variables"
            
            client = TavilyClient(api_key=api_key)
            results = client.search(
                query=query, 
                max_results=10,
                search_depth="advanced",
                include_domains=["arxiv.org", "nature.com", "scholar.google.com"]
            )
            
            formatted = []
            for r in results.get('results', []):
                formatted.append(
                    f"**Title:** {r.get('title')}\n"
                    f"**URL:** {r.get('url')}\n"
                    f"**Content:** {r.get('content')}\n"
                )
            
            return "\n---\n".join(formatted) if formatted else "No results found"
            
        except ImportError:
            return "Error: tavily-python package not installed. Run: uv pip install tavily-python"
        except Exception as e:
            return f"Error searching: {str(e)}"

# Create tool instances
search_tool = TavilySearchTool()
advanced_search = AdvancedSearchTool()
