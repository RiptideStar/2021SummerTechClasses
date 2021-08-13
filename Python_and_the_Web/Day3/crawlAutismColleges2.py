import requests
import sys
from bs4 import BeautifulSoup #html parser
import sqlite3


print("--- Command Line:", sys.argv)

api_url = "https://www.greatvaluecolleges.net/best-colleges-for-students-with-autism/"
print("--- api_url:", api_url)

# takes in url, outputs a universities list of relevant information
def retrieveData(api_url):
    try:
        response = requests.get(api_url)
    except requests.exceptions.ConnectionError as e:
        print('Error: ', e.args)
        exit(1)

    html = response.content
    # print(html)

    soup = BeautifulSoup(html, 'html.parser')

    parentClass = soup.findChild("div", class_="entry-content clearfix")

    children = parentClass.findChildren()

    datalist = []

    # order of rows
    # univ_name, location, ranking, desc, url, src_url
    for i in range(len(children)):
        row = []
        try:
            int(children[i].getText()[0:1])
        except ValueError:
            continue

        # at this point, we have our child we are currently on (children[i])
        # containing an integer as its first character

        try:
            ranking_name = children[i].getText().split(". ")
            ranking = ranking_name[0]
            univ_name = ranking_name[1]
            i+=1
        #break out if we are at end of list
        except IndexError:
            break

        location = children[i].getText()
        i += 1

        row.append(univ_name)
        row.append(location)
        row.append(ranking)

        url = children[i].findChild('a')["href"]
        # print("--url", url)
        i += 2

        desc = ""
        desc += children[i].getText()
        # print("--desc1", desc)

        while True:
            try:
                #make sure we aren't at the next university
                int(children[i].getText()[0:1])
                i -= 1
                break
            except ValueError:
                # for drexel uni description, since it's #1 ranking, there are no more universities past it
                # check to see if the current child we are contemplating to add is the "related rankings"
                # if it is, get out because we don't want to add related rankings to the desc of Drexel
                if (children[i].getText()[0:3] == 'Rel'):
                    break
                # add to description since description goes across multiple children
                desc += children[i].getText()
                i+=1
        # print("--- desc2:", desc)     
        row.append(desc)
        row.append(url)
        row.append(api_url)   

        datalist.insert(0, row)
    return datalist


datalist = retrieveData(api_url)

def insert_into_database(datalist, name):
    conn = sqlite3.connect(name)
    c = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 2:
                continue
            data[index] = '"' + data[index] + '"'

        sql = '''
            insert into autism_unis
            (
                univ_name, location, ranking, description, url, source_url
            )
            values (?, ?, ?, ?, ?, ?)
        '''

        c.execute(sql, (data[0], data[1], data[2], data[3], data[4], data[5]))
        conn.commit()
    c.close()
    conn.close()

insert_into_database(datalist, "autism_universities.db")