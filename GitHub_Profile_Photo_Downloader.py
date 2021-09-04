import requests 
from bs4 import BeautifulSoup as bs
from beautifultable import BeautifulTable
import os

table = BeautifulTable()
github_user = input("\nEnter GitHub Username: ")
url = "https://github.com/" + github_user
req = requests.get(url)
scrab = bs(req.content, "html.parser")
data = scrab.find("img" , {"alt" : "Avatar"})['src']
print("\n")
table.rows.append([data])                
copy_link = "echo " + data.strip() + "| clip"
os.system(copy_link)
table.columns.header = ["Download Link"]
table.rows.append(["Download Link Copy in Clipboard Successfully"])
table.set_style(BeautifulTable.STYLE_BOX_ROUNDED) 
print(table)
input()

# Made By Yasin Rezvani

