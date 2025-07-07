# requests module --->
# is your go-to tool for making HTTP requests—whether you're fetching data from a website, interacting with an API, 
# or automating web tasks

# Key       Features
# Method	Purpose
# get()	    Retrieve data
# post()	Submit data
# put()	    Update data
# delete()	Remove data
# head()	Get headers only
# patch()	Partial update


import requests 
from bs4 import BeautifulSoup


# GET METHOD

response = requests.get("https://www.google.com")
print(response.text)

# POST METHOD
url1 = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": 'munmun',
    "body": 'good',
    "userId": 1,
}

headers = {
    'Content-type': 'application/json; charset=UTF-8'
}
response2 = requests.post(url1, headers=headers, json=data)
print(response2.text)

# BS4---->
# Python library used for parsing HTML and XML documents, especially in web scraping tasks.
# pip install beautifulsoup4

# What It Does
# Extracts data from messy or nested HTML/XML.
# Navigates and searches the document tree easily.
# Cleans up poorly formatted markup.

# Common Methods
# Method	           Purpose
# soup.find()	       Finds the first matching tag
# soup.find_all()	   Finds all matching tags
# soup.select()	       Uses CSS selectors
# .text	               Extracts text from a tag
# .attrs	           Accesses tag attributes

url = "https://www.codewithharry.com/blogpost/django-cheatsheet"
r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, "html.parser")

print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)





