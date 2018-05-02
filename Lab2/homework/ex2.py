from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)

raw_data = conn.read()
text = raw_data.decode("utf8")


soup = BeautifulSoup(text, "html.parser")
section = soup.find("section","section chart-grid")
ul = section.find("ul")

li_list = ul.find_all("li")
item_list=[]
for li in li_list:
    name_a = li.h3.a
    artist_a = li.h4.a
    name = name_a.string
    artist = artist_a.string
    item = {
        "Names": name,
        "Artists": artist,
    }
    item_list.append(item)

pyexcel.save_as(records=item_list, dest_file_name="itunetop100.xlsx")
