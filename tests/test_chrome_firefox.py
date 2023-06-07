import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"], scope="session")
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()

def test_chrome_firefox(driver):
    driver.get("https://www.google.com")
    assert driver.title == "Google"
