from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd
import glob
import time
import uuid
from pathlib import Path
from pybtex.database.input import bibtex
import os
from tqdm import tqdm
import hashlib

from datetime import datetime
import shutup

shutup.please()


class connected_papers(object):
    def __init__(self, url="https://www.connectedpapers.com"):
        Path("./Connected_Papers_Data/df_csvs").mkdir(parents=True, exist_ok=True)
        Path("./Connected_Papers_Data/connected_downloads").mkdir(
            parents=True, exist_ok=True
        )

        chrome_options = webdriver.ChromeOptions()
        chrome_prefs = {
            "download.default_directory": r"Connected_Papers_Data/connected_downloads"
        }
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_options.headless = True
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        self.driver = webdriver.Chrome(
            desired_capabilities=capabilities, chrome_options=chrome_options
        )
        self.driver.get(url)

        print("url tab opened..")

    def to_md5(self, text):
        """text to md5 conversion"""

        m = hashlib.md5()
        m.update(text.encode("utf-8"))
        return m.hexdigest()

    def search_(self, query, result_n):

        self.driver.find_elements_by_xpath('//*[@id="new_logo_item"]/a/div')[0].click()
        search_button = self.driver.find_elements_by_xpath(
            '//*[@id="searchbar-input"]'
        )[1].send_keys(query)
        click_ = self.driver.find_elements_by_xpath(
            '//*[@id="desktop-app"]/div[2]/div/div[1]/div/div/div[1]/button'
        )[0].click()
        print("waiting for loading papers result..")
        time.sleep(10)
        articles = self.driver.find_elements_by_xpath(
            f'//*[@id="desktop-app"]/div[2]/div/article[{result_n}]/div'
        )[0].click()
        print("waiting for graph loading..")
        time.sleep(20)
        expand_button = self.driver.find_elements_by_xpath('//*[@id="expand-button"]')[
            0
        ].click()
        self.driver.find_elements_by_xpath(
            '//*[@id="desktop-app"]/div[2]/div[3]/div[1]/div/div[1]/div[2]/span'
        )[0].click()
        print(f"downloaded graph result {result_n}")

    def get_path(self):
        paths = sorted(
            Path("./Connected_Papers_Data/connected_downloads/").iterdir(),
            key=os.path.getmtime,
        )
        latest_paper = str(paths[-1])
        return latest_paper

    def bib2df(self):
        unique_node_id = str(uuid.uuid4())
        parser = bibtex.Parser()
        latest_download = self.get_path()
        print(latest_download)
        bib_data = parser.parse_file(latest_download)
        df = {"key": [], "title": [], "link": []}
        keys = bib_data.entries.keys()
        for k in keys:
            df["key"].append(k)
            df["title"].append(bib_data.entries[k].fields["title"])
            df["link"].append(bib_data.entries[k].fields["url"])
        df = pd.DataFrame(df)
        df.to_csv(f"Connected_Papers_Data/df_csvs/{unique_node_id}.csv", index=False)
        return df

    def download_papers(self, query, n=10):

        for paper_i in tqdm(range(1, n+1)):
            try:
                self.search_(query, paper_i)
                self.bib2df()
            except Exception as e:
                print(e)
                pass

        all_dfs = pd.concat(
            [pd.read_csv(file) for file in glob.glob("Connected_Papers_Data/df_csvs/*")]
        )
        all_dfs = all_dfs.drop_duplicates("key").reset_index(drop=True)
        all_dfs.to_csv("Connected_Papers_Data/df_csvs/final_result.csv")
        print(f"Total connected papers {len(all_dfs)}")
        return all_dfs