import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_find_broken_links(driver):
    driver.get("https://djom202.github.io")

    anchor_tags = driver.find_elements(By.TAG_NAME, 'a')

    for tag in anchor_tags:
        href = tag.get_attribute('href')

        if href:
            driver.get(href)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            if "404" in driver.page_source:
                print(f"Broken link found: {href}")