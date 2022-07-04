import requests
import os
from bs4 import BeautifulSoup
import pandas as pd

home=os.getcwd()
path=os.path.join(home,"radio.xlsx")
x = requests.get('https://www.radiomirchi.com/more/tamil-top-20')

soup = BeautifulSoup(x.text)
top20 =soup.find_all('h2')
arr=[]
print(type(top20))

for i in range(len(top20)):
    filter=str(top20[i]).replace("<h2>","")
    filter2=str(filter.replace("</h2>",""))
    arr.append(filter2)

top20excel = pd.DataFrame({"TOP 20_Tamil_Songs" :  arr[1:]})

top20excel.to_excel(path, sheet_name = 'testsheet',float_format =" %.2f " ,index=False)

