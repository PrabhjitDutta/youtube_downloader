from bs4 import BeautifulSoup
import requests
from pytube import YouTube

search = "https://www.youtube.com/results"
search_term = input("Enter the name of the Video: ")
params = {"search_query" : search_term}

r = requests.get(search, params=params)
soup = BeautifulSoup(r.text, 'html5lib')

result = soup.find('a', {'aria-hidden': 'true'})
result = result['href']

YouTube("https://www.youtube.com" + result).streams.first().download()
