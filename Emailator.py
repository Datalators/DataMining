original_url = input('Enter The Url You Want To Emailate: ')

import re
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup

unscraped = deque([original_url])  

scraped = set()  

emails = set()  

while len(unscraped):
    url = unscraped.popleft()  
    scraped.add(url)

    parts = urlsplit(url)
        
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    if '/' in parts.path:
      path = url[:url.rfind('/')+1]
    else:
      path = url

#    print("Datalating %s" % url)
    try:
        response = requests.get(url, timeout=20)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        #return 'no'
        continue

    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", response.text, re.I))
    emails.update(new_emails) 

    soup = BeautifulSoup(response.text, 'lxml')