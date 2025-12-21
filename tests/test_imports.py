"""Minimal tests to verify package imports and structure."""


def test_version():
    import resp

    assert resp.__version__ == "0.1.0"


def test_main_imports():
    from resp import Resp, Semantic_Scholar, Arxiv, ACM, Serp

    assert Resp is not None
    assert Semantic_Scholar is not None
    assert Arxiv is not None
    assert ACM is not None
    assert Serp is not None


def test_all_exports():
    import resp

    expected = ["__version__", "Resp", "Semantic_Scholar", "Arxiv", "ACM", "Serp"]
    for name in expected:
        assert name in resp.__all__


def test_connected_papers_without_selenium():
    """Verify connected_papers raises helpful ImportError when selenium is missing."""
    import pytest

    try:
        import selenium
        pytest.skip("selenium is installed")
    except ImportError:
        pass

    import resp

    with pytest.raises(ImportError, match="selenium"):
        resp.connected_papers()
