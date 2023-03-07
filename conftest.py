# import pytest
#
#
# @pytest.fixture(autouse=True)
# def test_setup():
#     print("Launch browser")
#     print("Login")
#     print("Browse products")
#     yield
#     print("Logoff")
#     print("Close browser")
#
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
#
#
# @pytest.fixture(autouse=True)
# def browser():
#     driver = webdriver.Chrome(executable_path=r"C:\webdrivers\1\chromedriver.exe")
#     wait = WebDriverWait(driver, 10)
#     driver.maximize_window()
#     yield
#     driver.quit()