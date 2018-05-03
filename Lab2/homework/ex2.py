from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
text = raw_data.decode("utf8")
soup = BeautifulSoup(text, "html.parser")

table_header = soup.find("div", id="divTableHeader")
table_content = soup.find("table", id="tableContent")
#Tao list header
tr_header = table_header.find("tr")
td_header = tr_header.find_all("td")
header_list=[]
for td in td_header:
    header = td.string
    header_list.append(header)
#Tao list content
tr_content = table_content.find_all("tr")

content_list=[]
for tr in tr_content:
    td_content = tr.td
    content = td_content.string
    content_list.append(content)
#Tao bang
print(*content_list)
