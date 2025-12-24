"""RESP: Research Papers Search

Fetch Academic Research Papers from different sources including
Google Scholar, ACL, ACM, PMLR, Arxiv, Semantic Scholar, and more.
"""

__version__ = "0.1.0"

from resp.resp import Resp
from resp.apis.semantic_s import Semantic_Scholar
from resp.apis.arxiv_api import Arxiv
from resp.apis.acm_api import ACM
from resp.apis.serp_api import Serp


# Create wrapper classes for convenient module-level API
class ArxivWrapper:
    """Wrapper for Arxiv API with simplified interface."""
    
    def __init__(self):
        self._client = Arxiv()
    
    def search_papers(self, query, max_results=10, api_wait=5):
        """Search papers on Arxiv.
        
        Args:
            query: Search query string
            max_results: Maximum number of results/pages to fetch
            api_wait: Wait time between API calls in seconds
            
        Returns:
            DataFrame with paper titles and links
        """
        return self._client.arxiv(query, max_pages=max_results, api_wait=api_wait)


class SemanticScholarWrapper:
    """Wrapper for Semantic Scholar API with simplified interface."""
    
    def __init__(self):
        self._client = Semantic_Scholar()
    
    def search_papers(self, query, max_results=5, min_year=2015, max_year=2024, api_wait=5):
        """Search papers on Semantic Scholar.
        
        Args:
            query: Search query string
            max_results: Maximum number of result pages to fetch
            min_year: Minimum publication year
            max_year: Maximum publication year
            api_wait: Wait time between API calls in seconds
            
        Returns:
            DataFrame with paper titles and links
        """
        return self._client.ss(
            query,
            max_pages=max_results,
            min_year=min_year,
            max_year=max_year,
            api_wait=api_wait
        )


class ACMWrapper:
    """Wrapper for ACM Digital Library API with simplified interface."""
    
    def __init__(self):
        self._client = ACM()
    
    def search_papers(self, query, max_results=5, min_year=2015, max_year=2024, api_wait=5):
        """Search papers on ACM Digital Library.
        
        Args:
            query: Search query string
            max_results: Maximum number of result pages to fetch
            min_year: Minimum publication year
            max_year: Maximum publication year
            api_wait: Wait time between API calls in seconds
            
        Returns:
            DataFrame with paper titles and links
        """
        return self._client.acm(
            query,
            max_pages=max_results,
            min_year=min_year,
            max_year=max_year,
            api_wait=api_wait
        )


class GoogleScholarWrapper:
    """Wrapper for Google Scholar API via Serp with simplified interface."""
    
    def __init__(self):
        self._client = None
        self._api_key = None
    
    def _ensure_client(self):
        """Ensure client is initialized with API key."""
        if self._client is None:
            if self._api_key is None:
                raise ValueError(
                    "Google Scholar search requires a SerpAPI key. "
                    "Set it using: google_scholar.set_api_key('your_key_here') "
                    "or get one at https://serpapi.com/"
                )
            self._client = Serp(self._api_key)
    
    def set_api_key(self, api_key):
        """Set the SerpAPI key for Google Scholar searches.
        
        Args:
            api_key: Your SerpAPI key from https://serpapi.com/
        """
        self._api_key = api_key
        self._client = Serp(api_key)
    
    def search_papers(self, query, num_results=5):
        """Search papers on Google Scholar.
        
        Args:
            query: Search query string
            num_results: Maximum number of result pages to fetch
            
        Returns:
            DataFrame with paper titles, links, and snippets
        """
        self._ensure_client()
        return self._client.google_scholar_search(query, max_pages=num_results)
    
    def get_citations(self, query):
        """Get citations for a paper.
        
        Args:
            query: Search query for the paper
            
        Returns:
            Dictionary of citation data
        """
        self._ensure_client()
        return self._client.get_citations(query)
    
    def get_related_papers(self, query):
        """Get related papers from Google Scholar.
        
        Args:
            query: Search query for the paper
            
        Returns:
            Dictionary of related papers
        """
        self._ensure_client()
        return self._client.get_related_pages(query)


# Create module-level instances
arxiv = ArxivWrapper()
semantic_scholar = SemanticScholarWrapper()
acm = ACMWrapper()
google_scholar = GoogleScholarWrapper()


__all__ = [
    "__version__",
    "Resp",
    "Semantic_Scholar",
    "Arxiv",
    "ACM",
    "Serp",
    "arxiv",
    "semantic_scholar",
    "acm",
    "google_scholar",
]


def connected_papers():
    """Lazy import and instantiate connected_papers (requires selenium extra)."""
    try:
        from resp.apis.cnnp import connected_papers as _connected_papers

        return _connected_papers()
    except ImportError as e:
        raise ImportError(
            "connected_papers requires selenium. "
            "Install with: pip install respsearch[selenium]"
        ) from e
