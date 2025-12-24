import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import time


class ACM(object):
    def __init__(self):
        pass

    def payload(self, keyword, st_page=0, pasize=50, start_year=2018, end_year=2022):

        params = (
            ("AllField", keyword),
            ("AfterYear", str(start_year)),
            ("BeforeYear", str(end_year)),
            ("queryID", "45/3852851837"),
            ("sortBy", "relevancy"),
            ("startPage", str(st_page)),
            ("pageSize", str(pasize)),
        )

        response = requests.get(
            "https://dl.acm.org/action/doSearch",
            params=params,
            headers={"accept": "application/json"},
        )
        soup = BeautifulSoup(response.text, "html.parser")

        return soup

    def soup_html(self, soup):

        all_papers = []
        main_class = soup.find(
            "div", {"class": "col-lg-9 col-md-9 col-sm-8 sticko__side-content"}
        )
        
        # Handle case where the HTML structure has changed or page didn't load properly
        if main_class is None:
            print("Warning: Could not find expected ACM page structure. Website may have changed.")
            print("Trying alternative selectors...")
            # Try alternative selector
            main_class = soup.find("div", {"class": "items-results"})
            if main_class is None:
                return pd.DataFrame({"title": [], "link": []})
        
        main_c = main_class.find_all("div", {"class": "issue-item__content"})
        
        # If no results found with this class, try alternative
        if not main_c:
            main_c = main_class.find_all("div", {"class": "search-result"})

        for paper in main_c:
            temp_data = {}

            doi_url = ["https://dl.acm.org", "doi", "pdf"]
            try:
                content_ = paper.find("h5", {"class": "issue-item__title"})
                paper_url = content_.find("a", href=True)["href"].split("/")

                doi_url.extend(paper_url[2:])
                title = content_.text
                temp_data["title"] = title
                temp_data["link"] = "/".join(doi_url)
                all_papers.append(temp_data)
            except Exception as e:
                pass

        df = pd.DataFrame(all_papers)
        return df

    def acm(
        self,
        keyword,
        max_pages=5,
        min_year=2015,
        max_year=2022,
        full_page_result=False,
        api_wait=5,
    ):
        "acm final call"
        all_pages = []

        for page in tqdm(range(max_pages)):
            acm_soup = self.payload(
                keyword, st_page=page, pasize=50, start_year=min_year, end_year=max_year
            )

            acm_result = self.soup_html(acm_soup)
            all_pages.append(acm_result)
            time.sleep(api_wait)

        df = pd.concat(all_pages)
        return df