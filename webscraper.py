import sys
import json
import importlib.util
from bs4 import BeautifulSoup 
import requests

def main():
    scrape_file = sys.argv[1]
    json_file = "scrapedData.json"

    spec = importlib.util.spec_from_file_location("my_module", scrape_file)
    scraper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scraper)
    
    url = scraper.get_url()
    response = requests.get(url)
    content = BeautifulSoup(response.content, "html.parser")

    attributes = scraper.initial_scrape(content)

    attribute_array = []

    for attribute in attributes:
        attribute_object = scraper.scraper(attribute)
        attribute_array.append(attribute_object)

    # print(attribute_array)
    with open(json_file, 'w') as outfile:
        json.dump(attribute_array, outfile)


main()