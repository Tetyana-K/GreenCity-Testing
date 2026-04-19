from datetime import datetime, timedelta
import unittest

from base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestEvents(BaseTest):

    EVENTS_URL = "https://www.greencity.cx.ua/#/greenCity/events"

    # def test_create_event(self):
    #     wait = WebDriverWait(self.driver, 10)

    #     self.login("ta_124@mailinator.com", "Qwerty_1234")

    #     create_button = wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, "//button[contains(text(),'Створити')]")
    #     ))
    #     create_button.click()

    #     # далі форма...

    def test_edit_event_details(self):
        wait = WebDriverWait(self.driver, 10)

        self.login("ta_124@mailinator.com", "Qwerty_1234")
        self.driver.get(self.EVENTS_URL)
        
        # locate card 
        card = self.get_event_card("Eco fest")

        # click edit button
        self.click_edit_button(card)

        start_time_xpath= "//input[@formcontrolname='startTime']"
        finish_time_xpath= "//input[@formcontrolname='finishTime']"
       
        start_time_input = wait.until(EC.visibility_of_element_located(
             (By.XPATH, start_time_xpath)
         ))
        
        current_time = start_time_input.get_attribute("value")
        new_time = self.get_time_plus_one_minute(current_time)
        print(f"Current time: {current_time}, New time: {new_time}")
        # записати новий час
        start_time_input.clear()
        start_time_input.send_keys(new_time)

        finish_time_input = wait.until(
            EC.visibility_of_element_located((By.XPATH,  finish_time_xpath))
        )

        current_finish_time = finish_time_input.get_attribute("value")
        new_finish_time = self.get_time_plus_one_minute(current_finish_time)

        finish_time_input.clear()
        finish_time_input.send_keys(new_finish_time)

        description_xpath= "//div[@class='ql-editor']"

        description_input = self.driver.find_element( By.XPATH, description_xpath)  

        current_description = description_input.text

        new_description = current_description + " updated"

        description_input.clear()
        description_input.send_keys(new_description)

        save_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Save') or contains(text(),'Зберегти') ]")
        save_button.click()
        
        # дочекатися, що форма закрилась або сторінка оновилась
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//input[@formcontrolname='startTime']")))

        # знову відкрити редагування
        card = self.get_event_card("Eco fest")
        self.click_edit_button(card)

        start_time = wait.until(
            EC.visibility_of_element_located(
            (By.XPATH, "//input[@formcontrolname='startTime']"))
        )

        self.assertEqual(start_time.get_attribute("value"), new_time)
    
    def get_event_card(self, event_name):
        wait = WebDriverWait(self.driver, 10)

        card_xpath = f"//mat-card[contains(.,'{event_name}')]"

        return wait.until(
            EC.visibility_of_element_located((By.XPATH, card_xpath))
        )    
    
    def click_edit_button(self, card):
        wait = WebDriverWait(self.driver, 10)

        edit_button = card.find_element(
            By.XPATH,
            ".//button[contains(@class,'event-button')]"
        )

        edit_button.click()

    def get_time_plus_one_minute(self, current_time):
        time_obj = datetime.strptime(current_time, "%H:%M")
        new_time = (time_obj + timedelta(minutes=1)).strftime("%H:%M")
        return new_time

if __name__ == "__main__":
    unittest.main()