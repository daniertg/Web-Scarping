from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Selenium webdriver
service = Service('C:/windows/system32/chromedriver.exe') # Sesuaikan dengan path ke driver Chrome di komputer Anda
driver = webdriver.Chrome(service=service)
driver.get("http://localhost/UAS%20WEB/index.php")

# Find and fill in login form
wait = WebDriverWait(driver, 10)

username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))

username.send_keys("dani")
password.send_keys("aku")

# Submit login form
login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn")))
login_button.click()

# # Get HTML content of the target page after logging in
# target_url = "http://localhost/UAS%20WEB/menu.php"
# driver.get(target_url)
# html_content = driver.page_source

# # Use Beautiful Soup to extract information from HTML
# soup = BeautifulSoup(html_content, "html.parser")
# data = soup.find("h3", {"class": "h2"})
# message = "Halo, ini informasi yang saya dapatkan: " + data.text

# # Print or send the message to another service
# print(message)

# # Close the Selenium webdriver
driver.quit()
