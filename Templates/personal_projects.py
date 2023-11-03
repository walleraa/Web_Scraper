def scraper(attribute):
    return {"Name": attribute.find("h2").text,
            "Desc": attribute.find("p", attrs = {"class":"desc"}).text.strip().replace("\n", "").replace("  ",""),
            "Git": attribute.find("p", attrs = {"class":"git"}).find("a", href=True, recursive=False)["href"]}