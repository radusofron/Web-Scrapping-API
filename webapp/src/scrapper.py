import requests as req
from selenium import webdriver
from bs4 import BeautifulSoup
import json
from sentiment_analyzer import analyze


def get_data(url: str) -> BeautifulSoup:
    """Function to load webpage and scrape its content
    """
    # Set the type of browser => headless browser (to not open a browser window)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # Navigate to the webpage using Chrome after an explicit delay to make sure that the content of the page was fully loaded
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(15)
    driver.get(url)
    # Get page source
    page_source = driver.page_source
    # Close browser
    driver.quit()
    
    # Create object to scrape the webapge
    soup = BeautifulSoup(page_source, 'html.parser')

    return soup


def get_desired_content(url: str) -> json:
    """Function to extract only the necessary content
    """
    # Create list to store the desired content
    content = list()

    # Get object to scrape the main webpage
    soup = get_data(url)

    # Go to level 6 divs
    level_6_divs = soup.find("div").find("main").find("div").find("div").find_all("div", recursive=False)[1].find_all("div", recursive=False)    
    
    # Scrape divs content
    for div in level_6_divs:
        
        # Create a new object for every part of the desired content
        object = dict()

        # Convert BS4 element to string
        div=str(div)
        
        # Create object to scrape the div
        soup = BeautifulSoup(div, 'html.parser')

        # First div -> to select the current div
        object["title"] = soup.find("div").find("div", recursive=False).find_all("div", recursive=False)[1].find("a").text
        object["short description"] = soup.find("div").find("div", recursive=False).find_all("div", recursive=False)[1].find_all("div", recursive=False)[1].text
        object["image"] = soup.find("div").find("a").find("img").get("src")
        object["link"] = url + soup.find("div").find("a").get("href")

        # Get object to scrape the post page
        soup = get_data(object["link"])

        # Go to long description
        object["long description"] = soup.find("div").find("div").find("div").find("div").find_all("div", recursive=False)[1].find("div").find_all("div", recursive=False)[2].find_all("div", recursive=False)[1].text
        
        # Analyze and determine overall sentiment
        object["sentiment"] = analyze(object["long description"])
        
        content.append(object)

    # Convert into JSON format
    json_content = json.dumps(content, indent=4)
    return json_content