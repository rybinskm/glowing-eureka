from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

# options = Options()
# options.add_argument("--headless")
# options.add_argument("window-size=600,400")

browser = webdriver.Chrome()
browser.get("https://lowcygier.pl/")
browser.set_window_size(400, 600)
page_title = browser.title
print(f'{page_title}')
searching_input = browser.find_element(By.NAME, value="s")
sleep(1)
searching_button = browser.find_element(By.LINK_TEXT, value="Rozumiem")
searching_button.click()
sleep(1)
searching_input.send_keys("nintendo switch oled")
sleep(1)
# searching_button = browser.find_element(By.LINK_TEXT, value="Rozumiem")
# searching_button.click()

# driver.quit()

# driver = webdriver.Chrome()
#
# driver.get("https://www.google.com")
#
# driver.title  # => "Google"
#
# driver.implicitly_wait(0.5)
#ASD
# search_box = driver.find_element(By.NAME, "q")
# search_button = driver.find_element(By.NAME, "btnK")
#
# search_box.send_keys("Selenium")
# search_button.click()
#
# driver.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"
#
# driver.quit()