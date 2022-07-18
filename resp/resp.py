import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from resp.apis.serp_api import Serp
from resp.apis.cnnp import connected_papers



class Resp(object):
    
    def __init__(self, api_key):
        self.engine = Serp(api_key)

    
    def acl(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:aclanthology.org {keyword}', 
                                            max_pages)
        return result
    
    def pmlr(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:proceedings.mlr.press {keyword}', 
                                            max_pages)
        return result
    
    def arxiv(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:arxiv.org {keyword}', 
                                            max_pages)
        return result
    
    
    def semantic_scholar(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:www.semanticscholar.org {keyword}', 
                                            max_pages)
        return result
    
    
    def nips(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:papers.nips.cc {keyword}', 
                                            max_pages)
        return result
    
    
    def ijcai(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:www.ijcai.org {keyword}', 
                                            max_pages)
        return result
    
    
    def openreview(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:openreview.net {keyword}', 
                                            max_pages)
        return result
    
    def cvf(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:openaccess.thecvf.com {keyword}', 
                                            max_pages)
        return result
    
    def google_scholar(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:scholar.google.com {keyword}', 
                                            max_pages)
        return result
    
    def google_scholar_internal(self, keyword, max_pages = None):
        result = self.engine.google_scholar_search(keyword, 
                                                   max_pages)
        return result
    
    def custom_search(self, url, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:{url} {keyword}', max_pages)
        return result


    def all_related_papers(self, query):
        """download all related papers from two sources"""

        result = []
        cp = connected_papers()
        rl_result = cp.download_papers(query, n=1)
        rl_result["source"] = ["connected_papers"] * len(rl_result)
        rl_result["keyword"] = [query] * len(rl_result)
        rl_result = rl_result.loc[:, ~rl_result.columns.str.contains("^Unnamed")]
        rl_result["title"] = rl_result["title"].str.lower()
        result.append(rl_result)
        
        rl_resultgp = self.engine.get_related_pages(query)
        rl_resultgp = rl_resultgp[list(rl_resultgp.keys())[0]]
        rl_resultgp["source"] = ["google_scholar"] * len(rl_resultgp)
        rl_resultgp["keyword"] = [query] * len(rl_resultgp)
        rl_resultgp["title"] = rl_resultgp["title"].str.lower()
        result.append(rl_resultgp)

        df = pd.concat(result)
        df = df.drop_duplicates("title", keep="last")
        df = df.drop_duplicates("link", keep="last")
        df = df[["title", "link", "source", "keyword"]]
        return df.reset_index(drop=True)