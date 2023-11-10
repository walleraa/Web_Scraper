import sys
import json
import importlib.util
from bs4 import BeautifulSoup 
from selenium import webdriver
# import requests

def scrape_page(scraper, url):
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

    return attribute_array

def main():
    scrape_file = sys.argv[1]
    json_file = "scrapedData.json"

    spec = importlib.util.spec_from_file_location("my_module", scrape_file)
    scraper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scraper)

    output_list = []
    url_list = scraper.get_urls()
    for url in url_list:
        output = {
            "url":url,
            "data":scrape_page(scraper, url)
        }
        output_list.append(output)

    with open(json_file, 'w') as outfile:
        json.dump(output_list, outfile)        

main()