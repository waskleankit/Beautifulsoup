import time

from bs4 import BeautifulSoup
import requests

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    # INEDX IS COUNTER AND ENUMERATOR ALLOWS TO ITERATE THROUGH INDEX
    for index, job in enumerate(jobs):

        published_date = job.find('span', class_="sim-posted").span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','')
            skills = job.find('span' , class_="srp-skills").text.replace(' ','')
            more_info = job.header.h2.a["href"]
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f'Company Name : {company_name.strip()} \n')
                    f.write(f'Required Skills : {skills.strip()} \n ')
                    f.write(f'More Info:{more_info}')
                print(f'File Saved:{index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait =10
        print(f'waiting {time_wait} minutes... ')
        time.sleep(time_wait * 60)

# from bs4 import BeautifulSoup
# with open('home.html','r') as html_file:
#     content = html_file.read()
#     soup = BeautifulSoup(content,'lxml')
#     course_cards = soup.find_all('div', class_='align-items-stretch')
#     for course in course_cards:
#         course_name = course.h4.text.split()[0]
#         course_price = course.p.text
#         print(f'{course_name} is first word of  h4 of p {course_price}')
        # print(course_name)
        # print(course_price)

    # print(soup.prettify())
    # print(content)
    # tags = soup.find('h1')
    # tags = soup.find_all('h1')
    # print(tags)
    # courses_html_tags = soup.find_all('h2')
    # print(courses_html_tags)
    # for course in courses_html_tags:
    #     print(course.text)

# job = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
# company_name = job.find('h3', class_ = "joblist-comp-name").text
# published_date = job.find('span',class_ = "sim-posted")
# company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','')
# skills = job.find('span' , class_="srp-skills").text.replace(' ','')
# published_date = job.find('span',class_ = "sim-posted")
# published_date = job.find('span',class_ = "sim-posted").span.text
# print(published_date)
# print(skills)
# print(company_name)
# print(f'''
# Company Name : {company_name}
# Required Skills : {skills}
# ''')
# print(f'Company Name : {company_name}')
# print(f'Required Skills : {skills}')
# more_info = job.header.h2.a
# print(f'More Info:{more_info}')

# from bs4 import BeautifulSoup
# import requests
#
# print('Put some skill that you are not familiar with')
# unfamiliar_skill = input('>')
# print(f'Filtering out {unfamiliar_skill}')
#
# html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# # print(html_text)
# soup = BeautifulSoup(html_text,'lxml')
# jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
# for job in jobs:
#     published_date = job.find('span', class_="sim-posted").span.text
#     if 'few' in published_date:
#         company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','')
#         skills = job.find('span' , class_="srp-skills").text.replace(' ','')
#         more_info = job.header.h2.a["href"]
#         if unfamiliar_skill not in skills:
#             print(f'Company Name : {company_name.strip()}')
#             print(f'Required Skills : {skills.strip()}')
#             print(f'More Info:{more_info}')
#             print('')



# import time
#
# from bs4 import BeautifulSoup
# import requests
#
# print('Put some skill that you are not familiar with')
# unfamiliar_skill = input('>')
# print(f'Filtering out {unfamiliar_skill}')
#
# def find_jobs():
#     html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#     # print(html_text)
#     soup = BeautifulSoup(html_text,'lxml')
#     jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
#     for job in jobs:
#         published_date = job.find('span', class_="sim-posted").span.text
#         if 'few' in published_date:
#             company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','')
#             skills = job.find('span' , class_="srp-skills").text.replace(' ','')
#             more_info = job.header.h2.a["href"]
#             if unfamiliar_skill not in skills:
#                 print(f'Company Name : {company_name.strip()}')
#                 print(f'Required Skills : {skills.strip()}')
#                 print(f'More Info:{more_info}')
#                 print('')
#
# if __name__ == '__main__':
#     while True:
#         find_jobs()
#         time_wait =10
#         print(f'waiting {time_wait} minutes... ')
#         time.sleep(time_wait * 60)