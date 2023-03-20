from urllib.request import urlopen
from bs4 import BeautifulSoup

link = "https://id.wikipedia.org/wiki/Halaman_Utama"
html = urlopen(link).read()
soup = BeautifulSoup(html, 'html.parser')

data = soup.find('a', {'title': 'Metempsikosis'})

message = "Halo, ini informasi yang saya dapatkan: " + data.text

print(message)