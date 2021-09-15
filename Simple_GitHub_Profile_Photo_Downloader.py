import requests 
from bs4 import BeautifulSoup as bs
from beautifultable import BeautifulTable
import os

try:
 table = BeautifulTable()
 github_user = input("\nEnter GitHub Username: ")
 url = "https://github.com/" + github_user
 req = requests.get(url)
 scrab = bs(req.content, "html.parser")
 data = scrab.find("img" , {"alt" : "Avatar"})['src']
 print("")
 table.rows.append([data])                
 copy_link = "echo " + data.strip() + "| clip"
 os.system(copy_link)
 table.columns.header = ["Download Link"]
 table.rows.append(["Download Link Copy in Clipboard Successfully"])
 table.set_style(BeautifulTable.STYLE_BOX_ROUNDED) 
 print(table)
 input()
 
except:
 print("")
 print("--Username Not Found , Invalid Mode--")
 input()

# Made By Yasin Rezvani

