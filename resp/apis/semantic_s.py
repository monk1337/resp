import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import time

class Semantic_Scholar(object):
    
    def __init__(self):
        pass
    
    
    def payload(self,  keyword, page = 1, 
                       min_year = 2018, 
                       max_year = 2022):

        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            'Cache-Control': 'no-cache,no-store,must-revalidate,max-age=-1',
            'Content-Type': 'application/json',
            'sec-ch-ua-mobile': '?1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36',
            'X-S2-UI-Version': '20166f1745c44b856b4f85865c96d8406e69e24f',
            'sec-ch-ua-platform': '"Android"',
            'Accept': '*/*',
            'Origin': 'https://www.semanticscholar.org',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.semanticscholar.org/search?year%5B0%5D=2018&year%5B1%5D=2022&q=multi%20label%20text%20classification&sort=relevance',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

        data = json.dumps({ "queryString": f'{keyword.lower()}',"page":page,"pageSize":10,
                           "sort":"relevance","authors":[],"coAuthors":[],"venues":[],
                           "yearFilter":{"min":min_year,"max":max_year},"requireViewablePdf":False,
                           "publicationTypes":[],"externalContentTypes":[],"fieldsOfStudy":[],
                           "useFallbackRankerService":False,"useFallbackSearchCluster":True,
                           "hydrateWithDdb":True,"includeTldrs":True,"performTitleMatch":True,
                           "includeBadges":True,
                           "tldrModelVersion":"v2.0.0","getQuerySuggestions":False})

        response = requests.post('https://www.semanticscholar.org/api/1/search', headers=headers, data=data)
        return response




    def soup_html(self, output):
        """Semantic Scholar Result """

        final_result = []
        output       = output.json()['results']

        for paper in output:

            result = {'title': [], 'link': []}
            result['title'] = paper['title']['text']

            if 'primaryPaperLink' in paper:
                result['link'] = paper['primaryPaperLink']['url']
            elif paper['alternatePaperLinks']:
                result['link'] = paper['alternatePaperLinks'][0]['url']
            else:
                result['link'] = 'no_link_found'

            final_result.append(result)
        df = pd.DataFrame(final_result)
        return df



    def ss(self, keyword, max_pages = 5, 
                 min_year = 2015, 
                 max_year = 2022, 
                 full_page_result = False, api_wait = 5):
        "ss function call"

        all_pages = []
        for page in tqdm(range(1, max_pages+1)):
            ss_soup = self.payload(keyword, page = page, 
                       min_year = min_year,
                       max_year = max_year)

            ss_result = self.soup_html(ss_soup)
            all_pages.append(ss_result)
            time.sleep(api_wait)
        
        df = pd.concat(all_pages)
        return df.reset_index(drop=True)