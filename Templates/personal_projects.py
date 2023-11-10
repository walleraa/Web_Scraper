def get_urls():
    arr = [
        "https://walleraa.github.io/Professional-Portfolio/personal.html"
    ]
    return arr

def initial_scrape(content):
    return content.findAll('div', attrs={"class":"project"})

def scraper(attribute):
    return {"Name": attribute.find("h2").text,
            "Desc": attribute.find("p", attrs = {"class":"desc"}).text.strip().replace("\n", "").replace("  ",""),
            "Git": attribute.find("p", attrs = {"class":"git"}).find("a", href=True, recursive=False)["href"]}