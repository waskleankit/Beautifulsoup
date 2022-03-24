from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/clothing-and-accessories/bottomwear/pr?sid=clo,vua&p[]=facets.ideal_for%255B%255D%3DMen&p[]=facets.ideal_for%255B%255D%3Dmen&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_223f73df-86bc-4755-a253-5d2e4e2e376c_2_372UD5BXDFYS_MC.8HARX8UX7IX5&otracker=hp_rich_navigation_2_2.navigationCard.RICH_NAVIGATION_Fashion~Men%2527s%2BBottom%2BWear_8HARX8UX7IX5&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L1_view-all&cid=8HARX8UX7IX5"
response = requests.get(url)

htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')

titles = []
prices = []
images = []

for d in soup.find('div',attrs={'class':'_13oc-S'}):
    title =d.find('a',attrs={'class':'IRpwTa'})
    # print(title.string)

    price = d.find('div', attrs={'class': '_30jeq3'})
    # print(price.string.replace('₹','₹ '))
    # print(price.string)
    image =d.find('img',attrs={'class':'_2r_T1I'})
    print(image)
    print(image.get('src'))
    # images.append(img.get('src'))

    titles.append(title.string)
    prices.append(price.string)
    images.append(image.get('src'))

print(titles)



# for d in soup.find('div',attrs={'class':'_312yBx SFzpgZ'}):
#     #image = d.find('div', attrs={'class': '_312yBx SFzpgZ'})
#     img =d.find('img',attrs={'class':'_2r_T1I'})
#     print(d.getText)
#     # images.append(img.get('src'))
#
# print(images)