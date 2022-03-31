from bs4 import BeautifulSoup as bs
import requests
from csv import writer
url = "https://waskleshoppinglyx.herokuapp.com/bottomwear/"
page = requests.get(url)
# print(page)
soup = bs(page.content, 'html.parser')
# print(soup.prettify)
lists = soup.find_all('div', class_="col-sm-4 text-center mb-4")

with open('housing.csv','a',encoding='utf8', newline='') as f:
    thewriter = writer(f)
    count = 0
    header =['S.No' ,'Title','Link','Image link','Original price','Discounted price','Category','Description']
    thewriter.writerow(header)
    for list in lists:
        count = count + 1
        title = list.find('div', class_="fw-bold").text
        link = list.a["href"]
        img_link = list.a.div.img["src"]
        original_price = list.find('small', class_="fw-light").text.replace('\n         ','')
        discounted_price = list.find_all_next('div', class_="fw-bold")[1].text.replace('\n      ','').replace('\n         ','').replace(original_price,'').replace('        \n','')
        link_next_page = "https://waskleshoppinglyx.herokuapp.com"+link
        page2 = requests.get(link_next_page)
        soup2 = bs(page2.content, 'html.parser')
        category = soup2.find('a', class_="nav-link dropdown-toggle text-white").text
        description = soup2.find('p').text.replace('\n', ' ').replace('\r', '')
        print(description)
        info = [count,title, link, img_link, original_price, discounted_price,category,description]
        thewriter.writerow(info)
        # print(link_next_page)
#
#
#     # title = list.find('div', class_="fw-bold")
#     # title = list.find('div', class_="fw-bold")
# # all_list = list.find('a', attrs={'id': 'video-title'})
# #print(all_list)
# # all = soup.find('a')
# url = "https://www.pararius.com/apartments/amsterdam?ac=1"
# page = requests.get(url)
# # print(page)
# soup = bs(page.content, 'html.parser')
# # print(soup.prettify)
# lists = soup.find_all('li', class_="search-list__item")
# print(lists)
# for list in lists:
#     title = list.find('li', class_="search-list__item search-list__item--listing")
#     location = list.find('div', class_="listing-search-item__location")
#     price = list.find('span', class_="listing-search-item__price")
#     area = list.find('span', class_="illustrated-features__description")
#     # info = [title,location,price,area]
#     # print(info)
#     print(title)
#     print(area)





# from bs4 import BeautifulSoup as bs
# import requests
# from csv import writer
# url = "https://waskleshoppinglyx.herokuapp.com/topwear/"
# page = requests.get(url)
# # print(page)
# soup = bs(page.content, 'html.parser')
# # print(soup.prettify)
# lists = soup.find_all('div', class_="col-sm-4 text-center mb-4")
# for list in lists:
#     fwbold = list.find_all('div', class_="fw-bold")
#     for items in soup.find_all(class_="fw-bold"):
#         data = items.find_next_sibling(class_="fw-bold").text
#         print(data)
    # for fw in fwbold:
        # many_value = [fw.text.replace('\n         ','').replace('\n        ','').replace('\n','')]
        # many_value = [fw.text].next_sibling
        # title = many_value
        # print(title)




# from bs4 import BeautifulSoup as bs
# import requests
# from csv import writer
# url = "https://waskleshoppinglyx.herokuapp.com/topwear/"
# page = requests.get(url)
# # print(page)
# soup = bs(page.content, 'html.parser')
# # print(soup.prettify)
# lists = soup.find_all('div', class_="col-sm-4 text-center mb-4")
# for list in lists:
#     title = list.find('div', class_="fw-bold").text.replace('\n','-')
#     discounted_price = list.find('div', class_="fw-bold").text.next_sibling
#     print(discounted_price)