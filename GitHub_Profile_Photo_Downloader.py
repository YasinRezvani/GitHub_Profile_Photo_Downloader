import requests 
from bs4 import BeautifulSoup as bs
from beautifultable import BeautifulTable

table = BeautifulTable()
github_user = input("Enter GitHub Username: ")
url = "https://github.com/" + github_user
req = requests.get(url)
scrab = bs(req.content, "html.parser")
data = scrab.find("img" , {"alt" : "Avatar"})['src']
table.rows.append([data])                
table.columns.header = ["Download Link"]
table.set_style(BeautifulTable.STYLE_BOX_ROUNDED) 
print(table)
input()

# Made By Yasin Rezvani

