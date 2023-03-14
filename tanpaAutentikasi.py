from bs4 import BeautifulSoup
from twilio.rest import Client
import requests
import json
from urllib.request import urlopen

url = 'https://web.padangsidimpuankota.go.id/sejarah'

# wiki_link = "https://en.wikipedia.org/wiki/Wikipedia"
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# soup = BeautifulSoup(html, 'html.parser')
# soup = BeautifulSoup(response.content, 'html.parser')
data = soup.find('h1', {'class': 'page-title'})

message = "Halo, ini informasi yang saya dapatkan: " + data.text

account_sid = 'ACed6000105782f21d5a3222de4d0d5287'
auth_token = ''
client = Client(account_sid, auth_token)

from_whatsapp_number = 'whatsapp:+14155238886'  # Nomor WhatsApp Twilio
to_whatsapp_number = 'whatsapp:+6281264473007'  # Nomor WhatsApp Anda

# Susun pesan WhatsApp yang ingin dikirim
message = client.messages.create(
    body=message,
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

print(message.sid)
