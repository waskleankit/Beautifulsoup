from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/clothing-and-accessories/bottomwear/pr?sid=clo,vua&p[]=facets.ideal_for%255B%255D%3DMen&p[]=facets.ideal_for%255B%255D%3Dmen&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_223f73df-86bc-4755-a253-5d2e4e2e376c_2_372UD5BXDFYS_MC.8HARX8UX7IX5&otracker=hp_rich_navigation_2_2.navigationCard.RICH_NAVIGATION_Fashion~Men%2527s%2BBottom%2BWear_8HARX8UX7IX5&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L1_view-all&cid=8HARX8UX7IX5"
response = requests.get(url)
# print(response)
# print(response.status_code)
# print(response.content)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent,'html.parser')
##takes html content in funstion
# soup = BeautifulSoup(htmlcontent)
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())
##page name with tag
# print(soup.title)
##tag name
# print(soup.title.name)
##to see inner content of title
# print(soup.title.text)
##to see inner content of title
# print(soup.title.string)
##to see parent of tag
# print(soup.title.parent.name)
##to see first paragraph
# print(soup.p)
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find('a'))
# print(soup.find(id="container").prettify())
# print(soup.find(id=""))
#
# for link in soup.find_all('a'):
#     link.get('href')

# for link in soup.find_all('img'):
#     print(link.get('src'))

# product = soup.find_all('div',class_='W_R1IA')
# print(product)

product = soup.find('div',attrs={'class':'W_R1IA'})
print(product)