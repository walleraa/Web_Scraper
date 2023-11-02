import json

def parse(data):
    # Do whatever

    print(data) # Remove when done

def main():
    json_file = "scrapedData.json"
    json_data = []
    with open(json_file, 'r') as infile:
        json_data = json.load(infile)
    parse(json_data)

main()