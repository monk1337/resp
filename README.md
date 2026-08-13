<h2 align="center">RESP: Research Papers Search</h2>
<h4 align="center">Fetch academic research papers from multiple sources including Google Scholar, Arxiv, Semantic Scholar, ACL, ACM, and more</h4>

<p align="center">
  <a href="https://pypi.org/project/respsearch/"><img src="https://img.shields.io/pypi/v/respsearch.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/respsearch/"><img src="https://img.shields.io/pypi/pyversions/respsearch.svg" alt="Python versions"></a>
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License"></a>
  <a href="https://github.com/monk1337/resp/commits/main"><img src="https://img.shields.io/github/last-commit/monk1337/resp" alt="GitHub commit"></a>
  <a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"></a>
  <a href="https://colab.research.google.com/drive/188cWcZrBRVGAF3Dp_5uswmLgbBNKSioB?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
</p>

<p align="center">
  <a href="https://github.com/monk1337/resp_mcp">
    <img src="https://img.shields.io/badge/%F0%9F%9A%80%20NEW-RESP%20MCP%20Server-8A2BE2?style=for-the-badge&labelColor=black" alt="RESP MCP Server">
  </a>
  <a href="https://github.com/monk1337/resp_mcp">
    <img src="https://img.shields.io/badge/Try%20with-Claude%20Code%20%26%20Agents-FF6F00?style=for-the-badge&labelColor=black" alt="Try with Claude Code and Agents">
  </a>
</p>

> [!IMPORTANT]
> ## 🚀 RESP is now available as an MCP server &nbsp;—&nbsp; [**`resp_mcp`**](https://github.com/monk1337/resp_mcp)
>
> **Use RESP's paper search directly inside [Claude Code](https://github.com/monk1337/resp_mcp), Claude Desktop, Cursor, and any other AI agent** via the [Model Context Protocol](https://modelcontextprotocol.io). Search arXiv, Semantic Scholar, OpenReview, DBLP, the ACL Anthology, and 27 major AI/ML/NLP/CV conferences — as agent tools.
>
> ```bash
> claude mcp add resp -- resp-mcp
> ```
>
> ### &nbsp; 👉 &nbsp; **Check it out: [github.com/monk1337/resp_mcp](https://github.com/monk1337/resp_mcp)** &nbsp; ⭐

## Installation

```bash
pip install respsearch
```

For Connected Papers support (requires Selenium):
```bash
pip install respsearch[selenium]
```

## Quick Start

### Simple API (Recommended)

```python
from resp import arxiv, semantic_scholar, acm, google_scholar

# Arxiv - No API key needed
papers = arxiv.search_papers("deep learning", max_results=10)

# Semantic Scholar - No API key needed
papers = semantic_scholar.search_papers("natural language processing", max_results=5)

# ACM Digital Library - No API key needed
papers = acm.search_papers("machine learning", max_results=5)

# Google Scholar - Requires free SerpAPI key from https://serpapi.com/
google_scholar.set_api_key("your_serpapi_key")
papers = google_scholar.search_papers("machine learning", num_results=10)
```

### Advanced API (Direct Class Access)

```python
from resp.apis.arxiv_api import Arxiv
from resp.apis.semantic_s import Semantic_Scholar
from resp.apis.serp_api import Serp

# Arxiv
ap = Arxiv()
papers = ap.arxiv('deep learning', max_pages=5)

# Semantic Scholar
sc = Semantic_Scholar()
papers = sc.ss('neural networks', max_pages=3)

# Google Scholar via Serp
serp = Serp(api_key="your_serpapi_key")
papers = serp.google_scholar_search('transformers', max_pages=2)
```

## Features

- 🔍 **Search papers** by keywords across multiple academic sources
- 📚 **Fetch citations** of any paper from Google Scholar
- 🔗 **Find related papers** from Google Scholar
- 🕸️ **Connected Papers** - discover papers using [similarity graphs](https://www.connectedpapers.com/about) (not just citations)

## Supported Sources

| Source | API Key Required | Status |
|--------|------------------|--------|
| [Arxiv](https://arxiv.org/) | ✅ Free | ✅ Working |
| [Semantic Scholar](https://www.semanticscholar.org/) | ✅ Free | ✅ Working |
| [Google Scholar](https://scholar.google.com/) | 🔑 Required ([SerpAPI](https://serpapi.com/)) | ✅ Working |
| [ACM Digital Library](https://dl.acm.org/) | ✅ Free | ⚠️ Limited* |
| [ACL Anthology](https://aclanthology.org/) | ✅ Free | ✅ Via Resp |
| [PMLR](https://proceedings.mlr.press/) | ✅ Free | ✅ Via Resp |
| [NeurIPS](https://nips.cc/) | ✅ Free | ✅ Via Resp |
| [IJCAI](https://www.ijcai.org/) | ✅ Free | ✅ Via Resp |
| [OpenReview](https://openreview.net/) | ✅ Free | ✅ Via Resp |
| [CVF Open Access](https://openaccess.thecvf.com/menu) | ✅ Free | ✅ Via Resp |
| [Connected Papers](https://www.connectedpapers.com/) | ✅ Free | ✅ Requires Selenium |

<sub>*ACM website structure changes frequently, may return limited results</sub>

## Advanced Features

### Google Scholar: Get Citations & Related Papers

```python
from resp import google_scholar

# Set API key once
google_scholar.set_api_key("your_serpapi_key")

# Search papers
papers = google_scholar.search_papers("attention mechanism", num_results=5)

# Get citations for a paper
citations = google_scholar.get_citations("Attention is all you need")

# Get related papers
related = google_scholar.get_related_papers("BERT language model")
```

### Connected Papers (Requires Selenium)

```python
from resp import connected_papers

# Install first: pip install respsearch[selenium]
papers = connected_papers().get_connected_papers("paper_title")
```

### Using Resp Class for Multiple Sources

```python
from resp import Resp

# Search across ACL, PMLR, NeurIPS, etc.
resp = Resp()
papers = resp.search_papers("keyword", source="acl")
```

## Citation

If you find this repository useful, please cite:

```bibtex
@misc{Resp2021,
  title = {RESP: Research Papers Search},
  author = {Pal, Ankit},
  year = {2021},
  howpublished = {\url{https://github.com/monk1337/resp}},
  note = {Fetch academic research papers from multiple sources}
}
```

## Support

If you'd like to support this project:

<p align="center">
  <a href="https://www.buymeacoffee.com/stoicbatman"><img src="https://github.com/appcraftstudio/buymeacoffee/raw/master/Images/snapshot-bmc-button.png" width="200"></a>
</p>

[![Star History Chart](https://star-history.dera.page/svg?repos=monk1337/resp&type=Date)](https://star-history.dera.page/#monk1337/resp&Date)
