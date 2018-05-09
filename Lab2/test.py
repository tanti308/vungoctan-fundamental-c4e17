import csv
import requests
import bs4
import pyexcel
url = 'https://www.techpowerup.com/gpudb/2990/radeon-rx-560d'
response = requests.get(url)
html = response.content

soup = bs4.BeautifulSoup(html, "lxml")

tables = soup.findAll("table")

tableMatrix = []
for table in tables:
    #Here you can do whatever you want with the data! You can findAll table row headers, etc...
    list_of_rows = []
    for row in table.findAll('tr')[1:]:
        list_of_cells =[]
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
    tableMatrix.append(list_of_rows)
pyexcel.save_as(records=tableMatrix, dest_file_name="test")
