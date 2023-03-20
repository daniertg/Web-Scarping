from bs4 import BeautifulSoup
from twilio.rest import Client
from urllib.request import urlopen

url = 'https://id.wikipedia.org/wiki/Halaman_Utama'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# soup = BeautifulSoup(html, 'html.parser')
# soup = BeautifulSoup(response.content, 'html.parser')
data = soup.find('a', {'title': 'Metempsikosis'})

message = "Halo, ini informasi yang saya dapatkan: " + data.text

account_sid = 'isi account sid'
auth_token = 'isi auth token twilio'
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
