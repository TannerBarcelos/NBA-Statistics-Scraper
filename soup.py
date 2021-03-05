from bs4 import BeautifulSoup
import requests

class Soup:
    
    # default baseURL is the root page we are pulling data from [can accept
    # any url if passed in when instantiating a new instance of this class]
    def __init__(self, baseURL = 'https://www.basketball-reference.com/teams/'):
        self.url = baseURL

    # returns the baseURL of the instance of this object
    def getURL(self):
        return self.url

    # performs the request to the url of the object instance
    def getData(self):
        data = requests.get(self.url).text
        return BeautifulSoup(data, 'lxml')