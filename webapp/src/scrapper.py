import requests as req
from bs4 import BeautifulSoup


def getData(url):
    """Function scrapes website content
    """
    response = req.get(url)
    print(response)
    try:
        response = req.get(url)
        response.raise_for_status()  # Check for HTTP errors

        webpage = BeautifulSoup(response.content, 'html.parser')
        title = webpage.title

        # # Extract title and short description (change selectors as needed)
        # title = soup.find('title').get_text()
        # description = soup.find('meta', attrs={'name': 'description'})['content']

        # return {"title": title, "description": description}

        return title

    except Exception as e:
        return {"error": str(e)}