# importing necessary libraries
from bs4 import BeautifulSoup
import requests
import json

import sys
from src.logger import logging
from src.exceptions import CustomException
# Creating the web source for scraping
logging.info("Imported necessary libraries in webscrapping file")
try:
    source = requests.get('https://indianexpress.com/').text

    soup = BeautifulSoup(source,'lxml')

    # Extracting the title of the webpage
    title_tag = soup.find('title')
    print(title_tag.text)

    # Extracting the content of the webpage
    content_tag = soup.find_all(lambda tag : tag.name in ['p','ol'] and not tag.find_all('strong') and tag.text.strip())
    content = ""
    for tag in content_tag:
        print("cOntent is\n")
        content+=" "+tag.text
    json.loads(content)
    
        
except Exception as e:
    raise CustomException(e,sys)



