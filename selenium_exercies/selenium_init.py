# import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager


def test_driver_manager_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)

    driver.get("https://www.google.com")

    driver.title  # => "Google"

    # driver.implicitly_wait(0.5)

    search_box = driver.find_element(By.NAME, "q")
    search_button = driver.find_element(By.NAME, "btnK")

    search_box.send_keys("Selenium")
    search_button.click()

    driver.find_element(By.NAME, "q").get_attribute("value")  # => "Selenium"

    # driver.quit()


def test_edge_session():
    service = EdgeService(executable_path=EdgeChromiumDriverManager().install())

    driver = webdriver.Edge(service=service)

    driver.quit()


def test_firefox_session():
    service = FirefoxService(executable_path=GeckoDriverManager().install())

    driver = webdriver.Firefox(service=service)

    driver.quit()


# @pytest.mark.skip(reason="only runs on Windows")
# def test_ie_session():
#     service = IEService(executable_path=IEDriverManager().install())
#
#     driver = webdriver.Ie(service=service)
#
#     driver.quit()

test_driver_manager_chrome()