import unittest
from asyncio import wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from time import sleep
#from time import sleep


class TestLogin(unittest.TestCase):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity"
    modal_xpath = "//app-auth-modal"
    def setUp(self):

        oprions = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=oprions)
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

   

    def test_successful_login(self):
        wait = WebDriverWait(self.driver, 10)

        # 1. Open modal window
        sign_in_selector = ".header_navigation-menu-right-list > .header_sign-in-link"
        sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, sign_in_selector)))
        sign_in_button.click()

        # 2. Enter email
        email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
        email_input.send_keys("ta_124@mailinator.com")

        # 3. Enter password
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("Qwerty_1234")

        # 4. Click login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # 5. Check: modal is closed
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.modal_xpath)))
        print("Login modal is closed")

        # 6. Check: sign-out  button is available
        logout_xpath = "//li[@aria-label='sign-out']"
        logout_button = wait.until(EC.visibility_of_element_located((By.XPATH, logout_xpath)))
        self.assertTrue(logout_button.is_displayed(), "User is not logged in")

if __name__ == "__main__":
    unittest.main()
