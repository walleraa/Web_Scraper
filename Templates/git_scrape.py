def get_urls():
    arr = [
        "https://github.com/walleraa/Beast_Of_The_Sea",
        "https://github.com/walleraa/Professional-Portfolio"
    ]
    return arr

def initial_scrape(content):
    return content.find('main').find_all('div', attrs={"class":"Box-row"})

def scraper(attribute):
    # return attribute
    return {
        "File Name": attribute.find("div", attrs={"class":"col-md-2"}).find("span").find("a").text.strip(),
        "Last Commit Name": attribute.find("div", attrs={"class":"col-5"}).find("span").find("a").text.strip(),
        "Last Commit Time": attribute.find("div", attrs={"class":"text-right"}).text.strip()
    }