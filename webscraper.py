import sys
import json
import importlib.util
from bs4 import BeautifulSoup 
import requests

def main():
    template_file = sys.argv[1]
    template = []
    # with open (template_file, 'r') as infile:
    #     for line in infile:
    #         template.append(json.loads(line))
    f = open(template_file)
    template = json.load(f)

    json_file = "scrapedData.json"
    url = template["url"]
    scrape_file = template["scrape-file"]

    spec = importlib.util.spec_from_file_location("my_module", scrape_file)
    scraper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scraper)

    response = requests.get(url)
    content = BeautifulSoup(response.content, "html.parser")

    # attributes = content.findAll('div', attrs={"class":"project"})
    attributes = content.findAll(template["content-container"], attrs=template["content-attrs"])

    attribute_array = []

    for attribute in attributes:
        # print(attribute.text.encode('utf-8'))
        # attribute_object = {"Name": attribute.find('h2').text,
        #                     "Desc": attribute.find('p', attrs = {"class":"desc"}).text.strip().replace("\n", "").replace("  ",""),
        #                     "Git": attribute.find('p', attrs = {"class":"git"}).find("a", href=True, recursive=False)['href']}
        attribute_object = scraper.scraper(attribute)
        attribute_array.append(attribute_object)
        # print(attribute_object)

    # print(attribute_array)
    with open(json_file, 'w') as outfile:
        json.dump(attribute_array, outfile)


main()