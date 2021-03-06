from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

# Define arrays - what to extract
part_numbers = []
titles = []
descriptions = []
prices = []
shipping_weights = []  # const
image_links = []
product_links = []
canonical_links = []

# const
brand = []
condition = []
availability = []
identifier_exists = []
product_category = []


# part list - read from CSV file
parts_to_scrap = pd.read_csv('C:/code/web-scrapper/triflex_uk_de.csv')
parts_to_scrap.columns = ["part"]
rawlist = list(parts_to_scrap.part)

# start chrome driver
driver = webdriver.Chrome(
    executable_path=r'C:\code\web-scrapper\chromedriver.exe')

for part_no in rawlist:
    # grab current part and add it to URL
    url = "https://www.igus.co.uk/product/?artNr=" + str(part_no)
    driver.get(url)
     # wait
    sleep(3)
    soup = BeautifulSoup(driver.page_source, "lxml")

   

    # get data from each element

    try:
        part_number = str(part_no)

        price = soup.find('span', {'id': 'orderboxSumPrice'}).get_text()

        title = soup.find("h2", {"class": "productHeadline"}).get_text()
        title = title + ' | ' + str(part_no)
    
        # description = soup.find(
        #     'ul', {'class': 'list-styled unordered'}).get_text()
        description_div = soup.find('div', {'class': "igus005Produktinformationen"})
        description = description_div.find('ul').get_text(', ', strip = True)

        if description:
            descriptions.append(description)         
        else:
            descriptions.append(description_div.get_text()) 


        shipping_weight = 0 # const

        image_div = soup.find(
            'div', {"class": "slider__slide slick-slide slick-current slick-active"})
        image_link = 'https://www.igus.co.uk' + image_div.find('img').attrs['src']

        product_link = url

        canon_link = url

        # append data to arrays


        part_numbers.append(part_number)
        titles.append(title)
        
        prices.append(price)
        shipping_weights.append(shipping_weight)
        image_links.append(image_link)
        product_links.append(product_link)
        canonical_links.append(canon_link)
        brand.append('igus')
        condition.append('new')
        availability.append('in stock')
        identifier_exists.append('no')
        product_category.append('Business & Industrial > Manufacturing')
        print("OK!" + part_number)
    except AttributeError:

        part_numbers.append('ERROR')
        titles.append('ERROR')
        descriptions.append('ERROR')
        prices.append('ERROR')
        shipping_weights.append('ERROR')
        image_links.append('ERROR')
        product_links.append('ERROR')
        canonical_links.append('ERROR')
        brand.append('igus')
        condition.append('new')
        availability.append('in stock')
        identifier_exists.append('no')
        product_category.append('Business & Industrial > Manufacturing')
        print("error! :(" + part_number)
# close chrome driver
driver.close()



# generate results and save as products.csv 
data_file = pd.DataFrame({'id': part_numbers, 'title': titles, 'description': descriptions, 'price': prices,
                         'shipping weight': shipping_weights, 'image_link': image_links, 'link': product_links, 'canonical_link': canonical_links, 'brand': brand, 'condition': condition, 'availability': availability, 'identifier_exists': identifier_exists, 'google_product_category': product_category })
data_file.to_csv('C:/code/web-scrapper/triflex_uk_de_DONE.csv', index=False, encoding='utf-8')


