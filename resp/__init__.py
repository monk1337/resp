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

__all__ = [
    "__version__",
    "Resp",
    "Semantic_Scholar",
    "Arxiv",
    "ACM",
    "Serp",
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
