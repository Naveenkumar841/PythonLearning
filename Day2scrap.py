import requests
import numpy as np
import lxml
import pandas as pd


import requests
from bs4 import BeautifulSoup

# Define headers
headers = [
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/116.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Linux; Android 9; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.0.0 Mobile Safari/537.36'
]

# Choose a random header
random_header = {'User-Agent':headers[np.random.randint(len(headers))]}

# URL to scrape
URL = "https://stackoverflow.com/questions/17766725/how-to-re-install-lxml"

try:
    # Send GET request with random User-Agent
    response = requests.get(URL, headers=random_header)
    if response.status_code == 200:
        print("Request successful!")
    else:
        print(f"Request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

soup = BeautifulSoup(response.content, 'html.parser')
element = soup.select('h1')
print(element[0].text)
data = {"text": element[0].text }
pd.to_excel