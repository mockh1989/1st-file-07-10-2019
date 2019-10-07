import requests
from bs4 import BeautifulSoup
from pricedotcom import Product
import time

if __name__ == "__main__":
    query = input("please input your search query: ")
    r = requests.get("https://www.price.com.hk/search.php?g=A&q=" + query)
    soup = BeautifulSoup(r.text,"lxml")
    page_str = soup.find("div",{"class":"pagination-total"}).text
    num_page = int(page_str[1:-1].strip())
    print("total page", num_page)

    product_list = list()
    for i in range(1,num_page+1):
        l = "https://www.price.com.hk/search.php?g=A&q="+ query +"&page=" + str(i) 
    #     print(l)
        # visit webpage
        r = requests.get(l)
        # transform webpage to soup
        soup = BeautifulSoup(r.text,"lxml")
        # find item box
        item_row = soup.find_all("div", {"class":"item-inner"})
        # get product name and price
        for p_item in item_row:
            product_title = p_item.find("div", {"class":"line line-01"}).text.strip()
            product_price = p_item.find("span", {"class":"text-price-number"})
            if product_price is None:
                product_price = "-1"
            else:
                product_price = product_price.text.strip().replace(",","")
            product_list.append(Product(product_title, product_price))
        time.sleep(5)
        
    with open('{}.txt'.format(query),'w', encoding='utf-8') as f:
        for i in product_list:
            f.write(str(i)+'\n')
    with open('{}.csv'.format(query),'w') as f:
        for i in product_list:
            f.write(i.get_csv_format())
        