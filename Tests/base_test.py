import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseTest(unittest.TestCase):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity"

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def login(self, email, password):
        wait = WebDriverWait(self.driver, 10)

        # open modal
        sign_in_selector = ".header_navigation-menu-right-list > .header_sign-in-link"
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, sign_in_selector))).click()

        # enter credentials
        wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)

        # submit
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # wait modal close
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//app-auth-modal")))