import requests 
from bs4 import BeautifulSoup as bs

github_user = input("Enter GitHub user: ")
url = "https://github.com/" + github_user
req = requests.get(url)
scrab = bs(req.content, "html.parser")
data = scrab.find("img" , {"alt" : "Avatar"})['src']
print(data)

# Made By Yasin Rezvani

