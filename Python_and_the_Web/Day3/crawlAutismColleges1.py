import requests
import sys
from bs4 import BeautifulSoup #html parser

print("--- Command Line:", sys.argv)

api_url = "https://www.bestvalueschools.com/rankings/students-with-autism/"
print("--- api_url:", api_url)

def retrieveData(api_url):
    try:
        response = requests.get(api_url)
    except requests.exceptions.ConnectionError as e:
        print('Error: ', e.args)
        exit(1)

    html = response.content
    # print(html)

    soup = BeautifulSoup(html, 'html.parser')

    elements = soup.findChild("ol").findChildren("li")
    # print(elements)
    
    datalist = []
    sum = 0
    # university name, location, ranking, description, url of college, api_url
    for i in range(0, len(elements)):
        row = []
        univ_name = elements[i].find('span').getText()
        # print(i, univ_name)
        row.append(univ_name)
        location = elements[i].find('p').getText()
        # print(i,location)
        row.append(location)
        ranking = i+1
        # print(i, ranking, univ_name)
        row.append(ranking)
        desc = elements[i].findChild("div", class_="inner-content").find('p').getText()
        # print(i, desc)
        row.append(desc)
        url = elements[i].findChild('a')['href']
        # print(i, url)


retrieveData(api_url)