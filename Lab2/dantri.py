from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://dantri.com.vn"
# 1.1 Open connection
conn = urlopen(url)
# 1.2 Read data
raw_data = conn.read()
# 1.3 Decode
text = raw_data.decode('utf8')
# print(text)
# Save file
# dan_tri_file = open("dantri.html", "wb")  #luu text =w luu raw =wb
# dan_tri_file.write(raw_data)
#
# dan_tri_file.close()

# 2 Find ROI
soup = BeautifulSoup(text, "html.parser")
# print(soup.prettify())

ul = soup.find("ul", "ul1 ulnew")
# print(ul.prettify())
li_list = ul.find_all("li")
item_list=[]
for li in li_list:
    a = li.h4.a
    title = a.string    #cach lay string or content
    link = url + a["href"]
    item = {
        "Title": title,
        "Link": link
    }
    item_list.append(item)
# print(item_list)
import pyexcel
pyexcel.save_as(records=item_list, dest_file_name="dantri.xlsx")
    # print(title)
    # print(link)
    # print("----------------------------")
