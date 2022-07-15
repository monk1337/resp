import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from resp.apis.serp_api import Serp



class Ferp(object):
    
    def __init__(self, api_key):
        self.engine = Serp(api_key)

    
    def acl(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:https://aclanthology.org {keyword}', 
                                            max_pages)
        return result
    
    def pmlr(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:https://proceedings.mlr.press {keyword}', 
                                            max_pages)
        return result
    
    def arxiv(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:https://arxiv.org {keyword}', 
                                            max_pages)
        return result
    
    
    def semantic_scholar(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:https://www.semanticscholar.org {keyword}', 
                                            max_pages)
        return result
    
    
    def nips(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:https://papers.nips.cc {keyword}', 
                                            max_pages)
        return result
    
    
    def ijcai(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:https://www.ijcai.org {keyword}', 
                                            max_pages)
        return result
    
    
    def openreview(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:https://openreview.net {keyword}', 
                                            max_pages)
        return result
    
    def cvf(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:https://openaccess.thecvf.com {keyword}', 
                                            max_pages)
        return result
    
    def google_scholar(self, keyword, max_pages = None):
        result  = self.engine.google_search(
            f'site:https://scholar.google.com {keyword}', 
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