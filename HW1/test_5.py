from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class TestCase1:
    def test_case_open_login(self):
        chrome_driver = webdriver.Chrome()
        chrome_driver.maximize_window()
        chrome_driver.get("https://www.demoblaze.com/")
        wait = WebDriverWait(chrome_driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='navbarExample']")))
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[id='login2']")))
        login.click()
        try:
            login_window = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='logInModal']/div/div")))
            print("login button is working")
        except NoSuchElementException:
            print("login button doesn't work")


class TestCase2:
    def test_case_add_to_cart(self):
        chrome_driver = webdriver.Chrome()
        chrome_driver.maximize_window()
        chrome_driver.get("https://www.demoblaze.com/")
        wait = WebDriverWait(chrome_driver, 10)
        cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[onclick='showcart()']")))
        cart.click()
        button = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "button[class='btn btn-success']")))
        button.click()
        order = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='orderModal']/div/div")))
        order.click()
