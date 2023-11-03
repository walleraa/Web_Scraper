# Web_Scraper
This is a web scraper to scrape the web

# robots.txt
Remember to always check a website's robots.txt file before scraping to ensure you are always following a website's guidelines (https://domain_link/robots.txt). If there is any confusion, copy the robots.txt file into ChatGPT and ask what you can and can't do.

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
    python webscraper.py Templates/(Python file with templated information, see templates for example)

# To parse data:
    python parsedata.py > (some output file)

Sometimes the scraper will throw an error about NoneType not having an attribute "find." This happens when the scraper pulls Skeleton divs. It's probably due to the site's Javascript not updating the HTML in time for the scraper. Either way, just wait a few seconds and try again.
