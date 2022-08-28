import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep
import selenium_exercies.credentials as cred

NoSuchEl = selenium.common.exceptions.NoSuchElementException

driver = webdriver.Firefox()
driver.get(f'{cred.website}')
sleep(5)

''' cookie section '''
cookie_button = driver.find_element(By.CLASS_NAME, 'ic-info-bar-buttons')
print(f'cookie button found')
cookie_button.click()
print(f'cookie button clicked')
driver.execute_script('window.scrollTo(0, 968)')
print(f'move window below')
sleep(1)

''' select correct option via pesel '''
options_drop_button = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-checking-drivers-license-status/div/div[1]/div/div[1]/form/div/app-selectable-input/div/div[1]/si-internal-text-input/div')
print(f'options drop button found')
options_drop_button.click()
print(f'options drop button clicked')
options_drop_button = driver.find_element(By.XPATH, '//*[@id="pesel"]')
print(f'searching via pesel found')
options_drop_button.click()
print(f'searching via pesel clicked')
sleep(1)

''' fulfill necessary sections '''
id_number_field = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-checking-drivers-license-status/div/div[1]/div/div[1]/app-checking-status-form/form/div[1]/app-form-input/div/div[1]/input')
id_number_field.send_keys(f'{cred.id_number}')
id_number_field = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-checking-drivers-license-status/div/div[1]/div/div[1]/app-checking-status-form/form/div[2]/app-form-input/div/div[1]/input')
id_number_field.send_keys(f'{cred.name}')
id_number_field = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-checking-drivers-license-status/div/div[1]/div/div[1]/app-checking-status-form/form/div[3]/app-form-input/div/div[1]/input')
id_number_field.send_keys(f'{cred.surname}')

''' click check button '''
check_button = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-checking-drivers-license-status/div/div[1]/div/div[1]/app-checking-status-form/form/div[4]/ic-ghost-button/button')
print(f'check button found')
check_button.click()
print(f'check button clicked')
sleep(1)

''' read status '''
current_info = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-checking-drivers-license-status/div/div[2]/div/div/app-checking-status-result/section/div/div[2]/div/div[1]/div[2]/span').text
print(f'Current state: {current_info}')

for status_verify_1 in range(2, 6):
    try:
        for status_verify_2 in range(1, 4):
            current_status = driver.find_element(By.XPATH, f'/html/body/app-root/app-layout/app-checking-drivers-license-status/div/div[2]/div/div/app-checking-status-result/section/div/div[2]/div/div[{status_verify_1}]/div[3]/span[{status_verify_2}]').text
            try:
                if current_status != '':
                    print(f'Current state {status_verify_1}.{status_verify_2}: {current_status}')
            except NoSuchEl:
                print(f'Current state {status_verify_1}.{status_verify_2}: missing status')
                continue
    except NoSuchEl:
        continue

sleep(10)
driver.close()
