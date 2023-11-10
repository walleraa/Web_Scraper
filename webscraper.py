import sys
import json
import importlib.util
from bs4 import BeautifulSoup 
from selenium import webdriver
# import requests

def scrape_page(json_file, scraper, url):
    # response = requests.get(url)
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    response = driver.page_source
    content = BeautifulSoup(response, "html.parser")
    attributes = scraper.initial_scrape(content)

    # ---FOR DEBUGGING--- #
    # print(response)

    attribute_array = []

    for attribute in attributes:
        attribute_object = scraper.scraper(attribute)
        attribute_array.append(attribute_object)

    # print(attribute_array)
    with open(json_file, 'w') as outfile:
        json.dump(attribute_array, outfile)

def main():
    scrape_file = sys.argv[1]
    json_file = "scrapedData.json"

    spec = importlib.util.spec_from_file_location("my_module", scrape_file)
    scraper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scraper)

    url_list = scraper.get_urls()
    for url in url_list:
        scrape_page(json_file, scraper, url)

main()