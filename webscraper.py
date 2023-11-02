import sys
import json
from bs4 import BeautifulSoup 
import requests

def main():
    url = sys.argv[1]
    json_file = "scrapedData.json"

    response = requests.get(url)
    content = BeautifulSoup(response.content, "html.parser")

    attributes = content.findAll('div', attrs={"class":"project"})
    attribute_array = []

    for attribute in attributes:
        # print(attribute.text.encode('utf-8'))
        attribute_object = {"Name": attribute.find('h2').text,
                            "Desc": attribute.find('p', attrs = {"class":"desc"}).text.strip().replace("\n", "").replace("  ",""),
                            "Git": attribute.find('p', attrs = {"class":"git"}).find("a", href=True, recursive=False)['href']}
        attribute_array.append(attribute_object)
        # print(attribute_object)

    # print(attribute_array)
    with open(json_file, 'w') as outfile:
        json.dump(attribute_array, outfile)


main()