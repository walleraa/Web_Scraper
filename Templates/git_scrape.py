def get_url():
    return "https://github.com/walleraa/Beast_Of_The_Sea"

def initial_scrape(content):
    return content.find('main')

def scraper(attribute):
    return attribute
    # return {
    #     "File Name": attribute.find("div", attrs={"class":"col-md-2"}).find("span").find("a").text.strip(),
    #     "Last Commit": attribute.find("div", attrs={"class":"col-5"}).find("span").find("a").text.strip(),
    #     "Commit Time": attribute.find("div", attrs={"class":"text-right"})
    # }