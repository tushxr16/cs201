from bs4 import BeautifulSoup
import requests
import os
import re

r = requests.get("www.google.com")
print(r)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup)