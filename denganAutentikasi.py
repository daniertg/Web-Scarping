from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
link = "https://id.wikipedia.org/wiki/Halaman_Utama"
html = urlopen(link).read()
soup = BeautifulSoup(html, 'html.parser')
driver = webdriver.Chrome()
driver.get("https://www.example.com/login")

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("your_username")
password.send_keys("your_password")

login_button = driver.find_element_by_id("login-button")
login_button.click()

data = soup.find('a', {'title': 'Metempsikosis'})

message = "Halo, ini informasi yang saya dapatkan: " + data.text

print(message)