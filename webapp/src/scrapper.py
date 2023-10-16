import requests as req
from selenium import webdriver
from bs4 import BeautifulSoup
import json


def get_title_and_short_description(div):
    """Function scrapes title and short description for every div
    """
    object = dict()

    # Convert BS4 element to string
    div=str(div)
    
    # Create scrapper
    soup = BeautifulSoup(div, 'html.parser')

    # Scrape title
    # First div -> to select the current div
    object["title"] = soup.find("div").find("div", recursive=False).find_all("div", recursive=False)[1].find("a").text
    object["short description"] = soup.find("div").find("div", recursive=False).find_all("div", recursive=False)[1].find_all("div", recursive=False)[1].text
    return object


def get_data(url: str):
    """Function scrapes website content
    """
    # Set the type of browser => headless browser (to not open a browser window)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # Navigate to the webpage using Chrome
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # Get page source
    page_source = driver.page_source
    # Close browser
    driver.quit()
    
    # Scrape the webapge
    soup = BeautifulSoup(page_source, 'html.parser')

    # Scrape level 6 divs
    level_6_divs = soup.find("div").find("main").find("div").find("div").find_all("div", recursive=False)[1].find_all("div", recursive=False)
    # Scrape divs content
    data = []
    for div in level_6_divs:
        data.append(get_title_and_short_description(div))
    
    # Convert into JSON format
    json_data = json.dumps(data, indent=4)
    return json_data