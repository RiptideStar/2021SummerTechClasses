import requests
import sys
from bs4 import BeautifulSoup #html parser
import xlwt
import sqlite3


print("--- Command Line:", sys.argv)

api_url = "https://www.bestvalueschools.com/rankings/students-with-autism/"
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

    elements = soup.findChild("ol").findChildren("li")
    # print(elements)
    
    datalist = []
    # row content: university name, location, ranking, description, url of college, api_url
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
        row.append(url)
        row.append(api_url)
        datalist.append(row)

    return datalist

datalist = retrieveData(api_url)
# print(datalist)

def save_to_excel(datalist):
    # create book
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)

    # create sheet
    sheet = book.add_sheet('universitiesForAutismStudents', cell_overwrite_ok=True)

    # column setup
    columns = {'Univ Name', 'Location', 'Ranking', 'Description', 'URL', 'Source', 'Misc'}

    #write our columns into the top row of the excel sheet
    for i in range(0, len(columns)):
        sheet.write(0, i, columns[i])

    # write our data in for every row past the top column row
    for i in range(0, len(datalist)):
        data = datalist[i]
        for j in range(0, len(data)):
            sheet.write(i+1, j, data[j])
            # print(i, data[j])

# save_to_excel(datalist)


def create_table(name):
    conn = sqlite3.connect(name)
    c = conn.cursor()

    sql = '''
        create table autism_unis
        (
            id integer primary key autoincrement,
            univ_name varchar,
            location varchar,
            ranking integer,
            description text,
            url text,
            source_url text,
            misc text
        )
    '''

    c.execute(sql)
    conn.commit()
    conn.close()

# create_table("autism_universities.db")

def select_data_db(name):
    conn = sqlite3.connect(name)
    c = conn.cursor()

    sql = '''
        SELECT *
        FROM autism_unis
    '''

    c.execute(sql)

    result = c.fetchall()
    print(result)

    conn.close()
    return result

database_results = select_data_db("autism_universities.db")

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