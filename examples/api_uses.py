"""
RESP Package - Comprehensive API Usage Examples

This file demonstrates all the ways to use the RESP package for searching academic papers.

EXAMPLES COVERED:
  1. Arxiv (Simple API) - No API key needed
  2. Semantic Scholar (Simple API) - No API key needed  
  3. ACM Digital Library (Simple API) - No API key needed
  4. Google Scholar (Simple API) - Requires SerpAPI key
  5. Arxiv (Advanced API) - Direct class import
  6. Semantic Scholar (Advanced API) - Direct class import
  7. ACM (Advanced API) - Direct class import
  8. Serp/Google Scholar (Advanced API) - Full control
  9. Resp Class - Multiple sources via Google
  10. Comparing results across multiple sources

NOTES:
  • Most sources work without any API key
  • Google Scholar features require free SerpAPI key from https://serpapi.com/
  • Set API key via environment: export SERPAPI_KEY="your_key"
  • Some services (Semantic Scholar) may rate-limit frequent requests
  • The script handles errors gracefully and continues execution

RUN: python3 api_uses.py
"""

import os
from pprint import pprint

print("=" * 80)
print(" " * 25 + "RESP API Usage Examples")
print("=" * 80)

# =============================================================================
# EXAMPLE 1: Simple API - Arxiv (No API Key Required)
# =============================================================================
print("\n\n### EXAMPLE 1: Arxiv Search (Simple API) ###")
print("-" * 80)

from resp import arxiv

# Basic search
papers = arxiv.search_papers("deep learning", max_results=2)
print(f"Found {len(papers)} papers from Arxiv")
print("\nFirst paper:")
print(f"  Title: {papers.iloc[0]['title']}")
print(f"  Link:  {papers.iloc[0]['link']}")

# With custom parameters
papers = arxiv.search_papers(
    query="transformer models",
    max_results=1,
    api_wait=3  # Wait 3 seconds between requests
)
print(f"\nCustom search found {len(papers)} papers")


# =============================================================================
# EXAMPLE 2: Simple API - Semantic Scholar (No API Key Required)
# =============================================================================
print("\n\n### EXAMPLE 2: Semantic Scholar Search (Simple API) ###")
print("-" * 80)

from resp import semantic_scholar
import time

try:
    # Brief pause to avoid rate limits
    time.sleep(2)
    
    # Basic search
    papers = semantic_scholar.search_papers("natural language processing", max_results=1)
    print(f"Found {len(papers)} papers from Semantic Scholar")
    print("\nFirst paper:")
    print(f"  Title: {papers.iloc[0]['title']}")
    print(f"  Link:  {papers.iloc[0]['link']}")
    
    # With year filter
    time.sleep(2)
    papers = semantic_scholar.search_papers(
        query="BERT language model",
        max_results=1,
        min_year=2018,
        max_year=2024,
        api_wait=3
    )
    print(f"\nFiltered search (2018-2024) found {len(papers)} papers")
except Exception as e:
    print(f"⚠ Semantic Scholar search failed: {str(e)[:60]}...")
    print("  Note: Semantic Scholar may rate-limit frequent requests")
    print("  This is normal - try again in a moment")


# =============================================================================
# EXAMPLE 3: Simple API - ACM Digital Library (No API Key Required)
# =============================================================================
print("\n\n### EXAMPLE 3: ACM Digital Library Search (Simple API) ###")
print("-" * 80)

from resp import acm

papers = acm.search_papers("machine learning", max_results=1)
if len(papers) > 0:
    print(f"Found {len(papers)} papers from ACM")
    print("\nFirst paper:")
    print(f"  Title: {papers.iloc[0]['title']}")
    print(f"  Link:  {papers.iloc[0]['link']}")
else:
    print("⚠ ACM returned no results (website structure may have changed)")


# =============================================================================
# EXAMPLE 4: Simple API - Google Scholar (Requires API Key)
# =============================================================================
print("\n\n### EXAMPLE 4: Google Scholar Search (Simple API) ###")
print("-" * 80)

from resp import google_scholar

# Check if API key is set via environment variable
serpapi_key = os.environ.get("SERPAPI_KEY")

if serpapi_key:
    # Set API key
    google_scholar.set_api_key(serpapi_key)
    
    # Basic search
    papers = google_scholar.search_papers("artificial intelligence", num_results=1)
    print(f"Found {len(papers)} papers from Google Scholar")
    print("\nFirst paper:")
    print(f"  Title: {papers.iloc[0]['title']}")
    print(f"  Link:  {papers.iloc[0]['link']}")
    
    # Get citations (may take longer)
    print("\nFetching citations for 'Attention is all you need'...")
    citations = google_scholar.get_citations("Attention is all you need")
    print(f"Retrieved citations data: {type(citations)}")
    
    # Get related papers
    print("\nFetching related papers for 'BERT'...")
    related = google_scholar.get_related_papers("BERT")
    print(f"Retrieved related papers data: {type(related)}")
else:
    print("ℹ Google Scholar requires a SerpAPI key")
    print("  Set it via: google_scholar.set_api_key('your_key')")
    print("  Or environment variable: export SERPAPI_KEY='your_key'")
    print("  Get a free key at: https://serpapi.com/")


# =============================================================================
# EXAMPLE 5: Advanced API - Direct Class Import (Arxiv)
# =============================================================================
print("\n\n### EXAMPLE 5: Arxiv (Advanced API - Direct Class Import) ###")
print("-" * 80)

from resp.apis.arxiv_api import Arxiv

# Initialize the class
ap = Arxiv()

# Search with custom parameters
papers = ap.arxiv(
    keyword="neural networks",
    max_pages=1,
    api_wait=3
)
print(f"Found {len(papers)} papers using Arxiv class")
print(f"Columns: {list(papers.columns)}")


# =============================================================================
# EXAMPLE 6: Advanced API - Direct Class Import (Semantic Scholar)
# =============================================================================
print("\n\n### EXAMPLE 6: Semantic Scholar (Advanced API - Direct Class Import) ###")
print("-" * 80)

from resp.apis.semantic_s import Semantic_Scholar

try:
    # Initialize the class
    sc = Semantic_Scholar()
    
    # Brief pause
    time.sleep(2)
    
    # Search with full control
    papers = sc.ss(
        keyword="reinforcement learning",
        max_pages=1,
        min_year=2020,
        max_year=2024,
        api_wait=3
    )
    print(f"Found {len(papers)} papers using Semantic_Scholar class")
    print(f"Columns: {list(papers.columns)}")
except Exception as e:
    print(f"⚠ Semantic Scholar search failed (may be rate-limited)")
    print(f"  Error: {str(e)[:60]}...")


# =============================================================================
# EXAMPLE 7: Advanced API - Direct Class Import (ACM)
# =============================================================================
print("\n\n### EXAMPLE 7: ACM Digital Library (Advanced API - Direct Class Import) ###")
print("-" * 80)

from resp.apis.acm_api import ACM

# Initialize the class
ac = ACM()

# Search with year range
papers = ac.acm(
    keyword="computer vision",
    max_pages=1,
    min_year=2020,
    max_year=2024,
    api_wait=3
)
print(f"Found {len(papers)} papers using ACM class")
if len(papers) > 0:
    print(f"Columns: {list(papers.columns)}")


# =============================================================================
# EXAMPLE 8: Advanced API - Serp (Google Scholar with full control)
# =============================================================================
print("\n\n### EXAMPLE 8: Google Scholar via Serp (Advanced API) ###")
print("-" * 80)

if serpapi_key:
    from resp.apis.serp_api import Serp
    
    # Initialize with API key
    serp = Serp(api_key=serpapi_key)
    
    # Google Scholar search
    papers = serp.google_scholar_search(
        q="generative AI",
        max_pages=1
    )
    print(f"Found {len(papers)} papers using Serp class")
    print(f"Columns: {list(papers.columns)}")
    
    # Regular Google search (not just scholar)
    results = serp.google_search(
        query="machine learning trends",
        max_pages=1
    )
    print(f"\nRegular Google search found {len(results)} results")
else:
    print("ℹ Skipping - requires SERPAPI_KEY environment variable")


# =============================================================================
# EXAMPLE 9: Using Resp Class for Multiple Sources (Requires API Key)
# =============================================================================
print("\n\n### EXAMPLE 9: Resp Class for Multiple Academic Sources ###")
print("-" * 80)

from resp import Resp

if serpapi_key:
    # Resp class uses Google to search across multiple sources
    resp = Resp(api_key=serpapi_key)
    
    # Search ACL Anthology
    papers = resp.acl("deep learning", max_pages=1)
    print(f"ACL Anthology search found {len(papers)} results")
    
    # Search PMLR
    papers = resp.pmlr("neural networks", max_pages=1)
    print(f"PMLR search found {len(papers)} results")
    
    # Other available methods:
    # resp.nips(), resp.ijcai(), resp.openreview(), resp.cvf()
    print("\nResp class provides access to: ACL, PMLR, NeurIPS, IJCAI, OpenReview, CVF")
else:
    print("ℹ Resp class requires SerpAPI key (uses Google search)")
    print("  The Resp class provides access to multiple academic sources:")
    print("  - ACL Anthology, PMLR, NeurIPS, IJCAI, OpenReview, CVF")
    print("  Set SERPAPI_KEY environment variable to use this feature")


# =============================================================================
# EXAMPLE 10: Comparing Results from Multiple Sources
# =============================================================================
print("\n\n### EXAMPLE 10: Comparing Results from Multiple Sources ###")
print("-" * 80)

query = "transformer architecture"

print(f"Searching for '{query}' across multiple sources...\n")

# Arxiv
try:
    arxiv_papers = arxiv.search_papers(query, max_results=1)
    print(f"Arxiv:            {len(arxiv_papers)} papers")
except Exception as e:
    print(f"Arxiv:            Error - {str(e)[:50]}")
    arxiv_papers = []

# Semantic Scholar (with error handling for rate limits)
try:
    import time
    time.sleep(2)  # Brief pause to avoid rate limits
    ss_papers = semantic_scholar.search_papers(query, max_results=1)
    print(f"Semantic Scholar: {len(ss_papers)} papers")
except Exception as e:
    print(f"Semantic Scholar: Error - {str(e)[:50]}")
    ss_papers = []

# ACM
try:
    acm_papers = acm.search_papers(query, max_results=1)
    print(f"ACM:              {len(acm_papers)} papers")
except Exception as e:
    print(f"ACM:              Error - {str(e)[:50]}")
    acm_papers = []

total = len(arxiv_papers) + len(ss_papers) + len(acm_papers)
print(f"\nTotal papers found: {total}")


# =============================================================================
# Summary
# =============================================================================
print("\n\n" + "=" * 80)
print(" " * 30 + "EXAMPLES COMPLETE")
print("=" * 80)
print("\n✅ All examples executed successfully!")
print("\nKey Takeaways:")
print("  • Simple API: Use 'from resp import arxiv, semantic_scholar, ...'")
print("  • Advanced API: Import classes directly for more control")
print("  • Most sources are FREE (no API key needed)")
print("  • Google Scholar requires SerpAPI key from https://serpapi.com/")
print("\nFor more information, visit: https://github.com/monk1337/resp")
print("=" * 80)
