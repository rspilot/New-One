from bs4 import BeautifulSoup

import requests

import os

htmltext = requests.get("https://www.flipkart.com/search?q=apple+watch"
                        "&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&"
                        "otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&"
                        "as-type=HISTORY&suggestionId=apple+watch%7CSmart+Watches&"
                        "requestId=298f20df-c2f4-4a6c-931f-d6fb015115f6")

soup = BeautifulSoup(htmltext.text, "lxml")

res = soup.findAll("div", class_= "_3pLy-c row")

html ="<center>"
html +="<h1>"+" Apple Smart Watches "+"</h1>"

html += f'<table border={3}>'
html += "<tr>"

html += "<th>" + "Product Name" +"</th>"
html += "<th>" + "Price" + "</th>"
html += "<th>" + "Rating" + "</th>"
html += "</tr>"

for r in res:

    prod = r.find("div", class_="_4rR01T").text
    price = r.find("div", class_="_30jeq3 _1_WHN1").text
    rating = r.find("div",class_="_3LWZlK").text


    html += "<td>" + prod + "</td>"
    html += "<td>" + price + "</td>"
    html += "<td>" + rating + "</td>"

    html += "</tr>"
html += "</table>"
html +="</center>"

with open("output.html", "w", encoding='utf-8') as file:
    file.write(html)

os.startfile('output.html')