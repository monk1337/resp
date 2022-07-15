from serpapi import GoogleScholarSearch, GoogleSearch
import pandas as pd
import requests
import uuid
import json
import re
import hashlib
from pathlib import Path
from tqdm import tqdm
from urllib.parse import parse_qsl, urlsplit


class Serp(object):
    def __init__(self, api_key):
        """api key of serp api"""
        self.api_key = api_key

    def sengine(self, q):
        """initialize scholar search engine"""
        sengine = GoogleScholarSearch({"q": q, "api_key": self.api_key})
        return sengine

    def gengine(self, q, location="India"):
        """initialize google search engine"""
        gengine = GoogleSearch({"q": q, "location": location, "api_key": self.api_key})
        return gengine

    def write_json(self, data, save_path):
        """Write json data"""

        unique_node_id = str(uuid.uuid4())
        with open(f"{save_path}/{unique_node_id}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return 0

    def to_md5(self, text):
        """text to md5 conversion"""

        m = hashlib.md5()
        m.update(text.encode("utf-8"))
        return m.hexdigest()

    def filter_url(self, results):
        """filter the urls of special text"""

        try:
            fl_result = results["organic_results"]
        except Exception as e:

            print("API limit exhaust")

        related_articles = []
        for result in fl_result:
            # https://regex101.com/r/XuEhoh/1
            related_article = re.search(
                r"q=(.*)\/&scioq", result["inline_links"]["related_pages_link"]
            ).group(1)
            related_articles.append(related_article)
        return related_articles

    def get_related_pages(self, query):
        """get all related pages of a research
        paper from google scholar"""

        folder_name = self.to_md5(query)
        folder_path = f"Google_data/related_pages/{folder_name}/"
        Path(folder_path).mkdir(parents=True, exist_ok=True)

        seng = self.sengine(query)
        data = seng.get_dict()

        if "error" in data:
            return "API limit exhaust"
        else:
            url = self.filter_url(data)

            all_results = {}
            for single_url in tqdm(url):
                seng = self.sengine(single_url)
                result = self.pagination(seng, None, folder_path)
                all_results[self.to_md5(single_url)] = result
            return all_results

    def google_search(self, query, max_pages):

        folder_name = self.to_md5(query)
        folder_path = f"Google_data/Google_search/{folder_name}/"
        Path(folder_path).mkdir(parents=True, exist_ok=True)

        seng = self.gengine(query)
        result = self.pagination(seng, max_pages, folder_path)
        return result
    
    
    def google_scholar_search(self, q, max_pages):
    
        folder_name = self.to_md5(query)
        folder_path = f"Google_data/Google_Scholar/{folder_name}/"
        Path(folder_path).mkdir(parents=True, exist_ok=True)

        seng        = qs.sengine(q)
        result      = qs.pagination(seng, max_pages, folder_path)
        return result

    def filter_re(self, res):
        return [k["title"] for k in res["organic_results"]]

    def get_citations(self, query):

        folder_name = self.to_md5(query)
        folder_path = f"Google_data/Citation_data/{folder_name}/"
        Path(folder_path).mkdir(parents=True, exist_ok=True)

        seng = self.sengine(query)
        data = seng.get_dict()
        all_results = {}

        url = [
            links["inline_links"]["cited_by"]["serpapi_scholar_link"]
            for links in data["organic_results"]
        ]
        for paper_ in tqdm(url):
            res = self._req_pagination(paper_, max_pages=None, save_result=folder_path)
            all_results[self.to_md5(paper_)] = res
        return all_results

    def filter_data_(self, result, save_path):
        unique_node_id = str(uuid.uuid4())
        df_result = {"title": [], "link": [], "snippet": []}

        try:
            fl_result = result["organic_results"]
        except Exception as e:
            print("API limit exhaust")

        for single_result in fl_result:
            if "title" in single_result:
                df_result["title"].append(single_result["title"])
            else:
                df_result["title"].append("no_title")

            if "link" in single_result:
                df_result["link"].append(single_result["link"])
            else:
                df_result["link"].append("no_link")

            if "snippet" in single_result:
                df_result["snippet"].append(single_result["snippet"])
            else:
                df_result["snippet"].append("no_snipped")
        small_df = pd.DataFrame(df_result)
        small_df.to_csv(f"{save_path}{unique_node_id}.csv", index=False)
        return small_df

    def _req_pagination(self, url, max_pages=None, save_result="."):

        results = {}
        next_page = True
        page_no = 1
        next_link = url + f"&api_key={self.api_key}"
        all_df = []

        if max_pages:
            while next_page and page_no <= max_pages:

                print(f"Page : {page_no}")
                result = requests.get(next_link).json()

                if "error" in result:
                    break
                else:
                    fil_res = self.filter_data_(result, save_result)
                    all_df.append(fil_res)
                    self.write_json(result, save_result)
                    if "serpapi_pagination" in result:
                        pagination = result["serpapi_pagination"]
                        if "next" in pagination:
                            next_page = True
                            next_link = (
                                pagination["next_link"] + f"&api_key={self.api_key}"
                            )
                        else:
                            next_page = False
                        results[page_no] = result
                        page_no += 1
                    else:
                        break

        else:
            while next_page:
                print(f"Page : {page_no}")
                result = requests.get(next_link).json()

                if "error" in result:
                    break
                else:
                    fil_res = self.filter_data_(result, save_result)

                    all_df.append(fil_res)
                    self.write_json(result, save_result)

                    if "serpapi_pagination" in result:
                        pagination = result["serpapi_pagination"]

                        if "next" in pagination:
                            next_page = True
                            next_link = (
                                pagination["next_link"] + f"&api_key={self.api_key}"
                            )
                        else:
                            next_page = False

                        results[page_no] = result
                        page_no += 1
                    else:
                        break

        all_df = pd.concat(all_df)
        alpha_df = pd.DataFrame(all_df).reset_index(drop=True)
        alpha_df.to_csv(f"{save_result}allcsvs_req_df.csv", index=False)
        return alpha_df

    def pagination(self, cengine, max_pages, save_result="."):

        has_next_page = True
        page_no = 1
        all_result = {}
        all_df = []

        if max_pages:
            while has_next_page and page_no <= max_pages:
                print(f"Page : {page_no}")
                data = cengine.get_dict()

                if "error" in data:
                    break
                else:

                    fil_res = self.filter_data_(data, save_result)

                    all_df.append(fil_res)
                    self.write_json(data, save_result)
                    all_result[page_no] = data
                    page_no += 1

                    if "pagination" in data:
                        has_next_page = data["pagination"]["next"]
                        cengine.params_dict.update(
                            dict(
                                parse_qsl(
                                    urlsplit(
                                        data.get("serpapi_pagination").get("next")
                                    ).query
                                )
                            )
                        )
                    else:
                        break

        else:
            while has_next_page:
                print(f"Page : {page_no}")
                data = cengine.get_dict()

                if "error" in data:
                    break
                else:
                    fil_res = self.filter_data_(data, save_result)

                    all_df.append(fil_res)
                    self.write_json(data, save_result)
                    all_result[page_no] = data

                    page_no += 1

                    if "pagination" in data:
                        has_next_page = data["pagination"]["next"]
                        cengine.params_dict.update(
                            dict(
                                parse_qsl(
                                    urlsplit(
                                        data.get("serpapi_pagination").get("next")
                                    ).query
                                )
                            )
                        )
                    else:
                        break

        all_df = pd.concat(all_df)
        alpha_df = pd.DataFrame(all_df).reset_index(drop=True)
        alpha_df.to_csv(f"{save_result}allcsvs_df.csv", index=False)
        return alpha_df
