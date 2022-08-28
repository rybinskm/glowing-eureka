from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep
import selenium_exercies.credentials as cred

driver = webdriver.Firefox()
driver.get(f'{cred.website}')

sleep(3)

# cookie section
cookie_button = driver.find_element(By.CLASS_NAME, 'ic-info-bar-buttons')
print(f'cookie button found')
cookie_button.click()
print(f'cookie button clicked')

driver.execute_script('window.scrollTo(0, 968)')
sleep(1)

options_drop_button = driver.find_element(By.CSS_SELECTOR, '.riflebird')
print(f'options drop button found')
options_drop_button.click()
print(f'options drop button clicked')

options_drop_button = driver.find_element(By.CSS_SELECTOR, '#pesel')
print(f'searching via pesel found')
options_drop_button.click()
print(f'searching via pesel clicked')

sleep(1)

id_number_field = driver.find_element(By.CSS_SELECTOR, '#pesel > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)')
id_number_field.send_keys(f'{cred.id_number}')
id_number_field = driver.find_element(By.CSS_SELECTOR, '#imię > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)')
id_number_field.send_keys(f'{cred.name}')
id_number_field = driver.find_element(By.CSS_SELECTOR, '#nazwisko > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)')
id_number_field.send_keys(f'{cred.surname}')

check_button = driver.find_element(By.CSS_SELECTOR, '.submit-box > ic-ghost-button:nth-child(1) > button:nth-child(1) > div:nth-child(1) > svg:nth-child(1)')
print(f'check button found')
check_button.click()
print(f'check button clicked')

# read main info
current_info = driver.find_element(By.CSS_SELECTOR, '.status-text > span:nth-child(1)').text
print(f'Current state: {current_info}')

# read status
current_status = driver.find_element(By.CSS_SELECTOR, 'span.text-done').text
if current_status != '':
    print(f'Current state: {current_status}')

sleep(5)
driver.close()
