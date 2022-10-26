from bs4 import BeautifulSoup 
import requests
import pandas as pd
import os
columns = ["name","prices","discount","quantity"]


url = "https://www.flipkart.com/search?q=grocery&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
response_url = requests.get(url)
content_res = response_url.content
soup = BeautifulSoup(content_res, "lxml")
data_class = soup.find_all("div",attrs={"class":"_4ddWXP"})
#print(data_class)

output = []
for data in data_class:
    try:
        product_name = data.find("a",attrs={"class":"s1Q9rs"})["title"]
    except: 
        product_name = None
    
    try:   
        product_prices = data.find("div",attrs={"class":"_30jeq3"}).text
    except:
        product_prices = None
    try:    
        product_discount = data.find("div",attrs={"class":"_3Ay6Sb"}).text
    except:
        product_discount = None
    
    try:       
        product_quantity = data.find("div",attrs={"class":"_3Djpdu"}).text
    except:  
        product_quantity = None
        
    output_rows = [product_name,product_prices,product_discount,product_quantity]
    output.append(output_rows)
    
    #print(data)
            
path = "C:/Users/Ḥ/aditya/flipkart_data_excel/filpdata.xlsx"       
Grocery = pd.DataFrame(output,columns=columns)
Grocery.to_excel(path, index=False)

