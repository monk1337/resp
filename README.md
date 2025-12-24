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

## Installation

```bash
pip install respsearch
```

For Connected Papers support (requires Selenium):
```bash
pip install respsearch[selenium]
```

## Quick Start

```python
from resp import google_scholar, arxiv, semantic_scholar

# Search Google Scholar
papers = google_scholar.search_papers("machine learning", num_results=10)

# Search Arxiv
papers = arxiv.search_papers("deep learning", max_results=10)

# Search Semantic Scholar
papers = semantic_scholar.search_papers("natural language processing")
```

## Features

- 🔍 **Search papers** by keywords across multiple academic sources
- 📚 **Fetch citations** of any paper from Google Scholar
- 🔗 **Find related papers** from Google Scholar
- 🕸️ **Connected Papers** - discover papers using [similarity graphs](https://www.connectedpapers.com/about) (not just citations)

## Supported Sources

| Source | Status |
|--------|--------|
| [Google Scholar](https://scholar.google.com/) | ✅ |
| [Arxiv](https://arxiv.org/) | ✅ |
| [Semantic Scholar](https://www.semanticscholar.org/) | ✅ |
| [ACL Anthology](https://aclanthology.org/) | ✅ |
| [ACM Digital Library](https://dl.acm.org/) | ✅ |
| [PMLR](https://proceedings.mlr.press/) | ✅ |
| [NeurIPS](https://nips.cc/) | ✅ |
| [IJCAI](https://www.ijcai.org/) | ✅ |
| [OpenReview](https://openreview.net/) | ✅ |
| [CVF Open Access](https://openaccess.thecvf.com/menu) | ✅ |

## Examples

### Get citations for a paper

```python
from resp import google_scholar

citations = google_scholar.get_citations("paper_id_here")
```

### Get related papers

```python
from resp import google_scholar

related = google_scholar.get_related_papers("paper_id_here")
```

### Connected Papers

```python
from resp import connected_papers

# Requires: pip install respsearch[selenium]
papers = connected_papers.get_connected_papers("paper_title")
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

[![Star History Chart](https://api.star-history.com/svg?repos=monk1337/resp&type=Date)](https://star-history.com/#monk1337/resp&Date)
