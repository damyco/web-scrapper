import bs4 as bs
from bs4 import BeautifulSoup
import requests
import urllib
from urllib import request, response




# URL ( todo: loop through all products)
url = "https://www.igus.co.uk/product/?artNr=NWV-21-27-60-P10"


req = requests.get(url, verify=False)
soup = BeautifulSoup(req.text, "html.parser")

# what to extract
part_number = []
title = []
description = []
price = []
shipping_weight =[]
image_link = []
product_link = []

# const
brand = []
condition = []
availability = []
identifier_exists = []
shipping_label = []

############

response = request.Request(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'})
part_number.append(response.get_full_url().removeprefix('https://www.igus.co.uk/product/?artNr='))

get_product_title = soup.find("h2", {"class": "productHeadline"})
title.append(get_product_title.text)






source = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(source, 'lxml')
get_price = soup.find("span", {"id": "orderboxSumPrice"})
price.append(get_price)
print("PRICE:", get_price)

# generate CSV
data_file = pd.DataFrame({'id':part_number, 'title':title, 'price':price} )
data_file.to_csv('products.csv', index=False, encoding='utf-8')



