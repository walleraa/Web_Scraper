# Web_Scraper
This is a web scraper to scrape the web

# To use:
    Head to terminal
    
    <-Set up virtual environment->
    python3 -m venv env 
    
    <-Enter the virtual environment->
    Mac: source env/bin/active
    Windows: env/Scripts/activate.bat

    <-Install Python libraries->
    pip install bs4
    pip install requests

# To scrape for data:
    python webscraper.py Templates/(json file with templated information, see templates for example)

# To parse data:
    python parsedata.py > (some output file)
