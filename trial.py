from bs4 import BeautifulSoup as bs
import requests


url = "https://waskleshoppinglyx.herokuapp.com/product-detail/22"
page = requests.get(url)
# print(page)
soup = bs(page.content, 'html.parser')
# print(soup.prettify)
list = soup.find('p').text.replace('\n', ' ').replace('\r', '')
print(list)
