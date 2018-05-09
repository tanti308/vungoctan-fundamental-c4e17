from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs"

soup = BeautifulSoup(urlopen(url).read().decode("utf8"), "html.parser")
section = soup.find("section","section chart-grid")
ul = section.find("ul")

li_list = ul.find_all("li")

for li in li_list:
    name_a = li.h3.a
    name = name_a.string
    artist_a = li.h4.a
    artist = artist_a.string
    options = {
        'default_search': 'ytsearch',
        'max_downloads': len(li_list),
        'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([name, "- ", artist, "official video"])
