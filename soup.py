from bs4 import BeautifulSoup
import requests

class Soup:
    
    def __init__(self, baseURL = 'https://www.basketball-reference.com/teams/'):
        self.url = baseURL

    # returns the baseURL of the instance of this object
    def getURL(self):
        return self.url

    # performs the request to the url of the object instance
    def getData(self):
        data = requests.get(self.url).text
        return BeautifulSoup(data, 'lxml')