import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import time


class Arxiv(object):
    def __init__(self):
        pass

    def arxiv_payload(self, keyword, size=50, start=0):

        headers = {
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://arxiv.org/search/?query=Multi-label+text+classification&searchtype=all&abstracts=show&order=&size=50&start=200",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        }

        params = (
            ("searchtype", "all"),
            ("query", keyword.lower()),
            ("abstracts", "show"),
            ("size", str(size)),
            ("order", ""),
            ("start", str(start)),
        )
        response = requests.get(
            "https://arxiv.org/search/", headers=headers, params=params
        )
        soup = BeautifulSoup(response.text, "html.parser")

        return soup

    def arxiv_html_fetch(self, soup):

        final_result = []
        final_out = soup.find_all("li", {"class": "arxiv-result"})

        for paper in final_out:

            temp_result = {}
            title = paper.find("p", {"class": "title is-5 mathjax"}).text.strip()
            paper_link = paper.find("p", {"class": "list-title is-inline-block"}).find(
                "a", href=True
            )["href"]

            temp_result["title"] = title
            temp_result["link"] = paper_link

            final_result.append(temp_result)
            # final_result.append(temp_result)

        df = pd.DataFrame(final_result)
        return df

    def arxiv(self, keyword, max_pages=5, api_wait=5):

        "arxiv function call"

        all_pages = []
        for page in tqdm(range(max_pages)):
            arxiv_pay_load = self.arxiv_payload(keyword, start=page)
            arxiv_soup = self.arxiv_html_fetch(arxiv_pay_load)
            all_pages.append(arxiv_soup)
            time.sleep(api_wait)

        df = pd.concat(all_pages)
        return df.reset_index(drop=True)
