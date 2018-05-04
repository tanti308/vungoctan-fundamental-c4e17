from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

soup = BeautifulSoup(urlopen(url).read().decode("utf8"), "html.parser")

table_header = soup.find("div", id="divTableHeader")
table = soup.find("table", id="tableContent")

data_list=[]
tr_list = table.find_all("tr")

for tr in tr_list:
    td_list = tr.find_all("td", "b_r_c")
    for td in td_list:
        stt = td.string
        q4_2016 = td.string
        q1_2017 = td.string
        q2_2017 = td.string
        q3_2017 = td.string
        data = {
            "Hạng mục" : stt,
            "Quý 4/2016": q4_2016,
            "Quý 1/2017": q1_2017,
            "Quý 2/2017": q2_2017,
            "Quý 3/2017": q3_2017,
        }
        data_list.append(data)

pyexcel.save_as(records=data_list, dest_file_name="vinamilk.xlsx")
