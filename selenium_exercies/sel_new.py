from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

driver.title  # => "Google"

# driver.implicitly_wait()

# search_box = driver.find_element(By.NAME, "q")
# search_button = driver.find_element(By.NAME, "btnK")

# search_box.send_keys("Selenium")
# search_button.click()

# driver.find_element(By.NAME, "q").get_attribute("value")  # => "Selenium"

# driver.quit()

# driver = webdriver.Chrome(service=service)
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.google.com")
#
# driver.title # => "Google"
#
# driver.implicitly_wait(0.5)
#
# search_box = driver.find_element(By.NAME, "q")
# search_button = driver.find_element(By.NAME, "btnK")
#
# search_box.send_keys("Selenium")
# search_button.click()
#
# driver.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"
#
# driver.quit()
