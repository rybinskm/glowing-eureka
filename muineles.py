from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# cookie accept
search_button_name = "Zaakceptuj wszystko"

driver = webdriver.Firefox()
driver.get("https://wykop.pl")
time.sleep(5)

search_button = driver.find_element(By.XPATH, f"//button[text()='{search_button_name}'")
search_button.click()

time.sleep(2)
driver.close()

# driver.find_element(by=By.NAME, value="Szukaj").send_keys("Selenium")

