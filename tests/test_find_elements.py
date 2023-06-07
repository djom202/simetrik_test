import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def find_elements_within_element(element: WebElement, locator: tuple):
    return element.find_elements(*locator)

def test_find_elements(driver):
    driver.get("https://www.google.com")

    parent_element = driver.find_element(By.ID, "gb")
    locator = (By.CLASS_NAME, "a[data-pid='2']")
    child_elements = find_elements_within_element(parent_element, locator)
    for child_element in child_elements:
        print(child_element.text)
