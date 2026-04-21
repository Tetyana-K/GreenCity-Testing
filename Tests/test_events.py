from concurrent.futures import wait
from datetime import datetime, timedelta
import unittest

from base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TestEvents(BaseTest):

    EVENTS_URL = "https://www.greencity.cx.ua/#/greenCity/events"

    def _test_create_event(self):
        wait = WebDriverWait(self.driver, 10)

        self.login("ta_124@mailinator.com", "Qwerty_1234")
        self.driver.get(self.EVENTS_URL)

        create_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Create') or contains(text(),'Створити')]")
        ))
        create_button.click()

        event_name = self.generate_event_name()
        title_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@formcontrolname='title']"))
        )
        title_input.send_keys(event_name)

        event_type = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(@class,'mat-mdc-chip-action-label') and (normalize-space()='Environmental' or normalize-space()='Екологічний')]")
        ))
        event_type.click()

        description_xpath= "//div[@class='ql-editor ql-blank']"
        description_input = self.driver.find_element( By.XPATH, description_xpath)  
        description_input.send_keys(f"Test event '{event_name}' description")

        date_input = self.driver.find_element(By.XPATH, "//input[@formcontrolname='day']")
        date_input.send_keys("25.07.2026")
        date_input.send_keys(Keys.TAB)

        start_time = self.driver.find_element(By.XPATH, "//input[@formcontrolname='startTime']")
        start_time.send_keys("23:30")
       
        finish_time = self.driver.find_element(By.XPATH, "//input[@formcontrolname='finishTime']")
        #finish_time.clear()
        finish_time.send_keys("23:59")

        self.driver.find_element(By.TAG_NAME, "body").click()
        online_checkbox = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[normalize-space()='Online']")
        ))
       
        online_checkbox.click()

        link_input = wait.until(EC.visibility_of_element_located(
          (By.XPATH, "//input[@formcontrolname='onlineLink']")
        ))
        link_input.send_keys("https://test_event.com")
        link_input.send_keys(Keys.TAB)
        
        publish_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Publish') or contains(text(),'Опублікувати')]")
        ))
        publish_button.click()
     
        # wait redirect to event page
        wait.until(EC.url_contains("/events"))

        created_event = self.get_event_card(event_name)
        #self.assertTrue(created_event.is_displayed(), "Event was not created") -- continue

    def _test_edit_event_details(self):
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
    
    def _test_add_comment_to_event(self):
        wait = WebDriverWait(self.driver, 10)

        self.login("ta_124@mailinator.com", "Qwerty_1234")
        self.driver.get(self.EVENTS_URL)

        comment_text = "Це тестовий коментар"

        # locatecard
        card = self.get_event_card("Eco fest")

        # click on More button
        details_button = card.find_element(
            By.XPATH,
            ".//button[contains(text(),'Детальніше') or contains(text(),'More')]"
        )
        details_button.click()

        #  wait to see comment input
        comment_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class ='comment-textarea']")
        ))
        comment_input.send_keys(comment_text)

        # click on Comment button
        submit_button = self.driver.find_element(
            By.XPATH,
            "//button[contains(text(),'Коментувати') or contains(text(),'Comment')]"
        )
        submit_button.click()

        # check that comment appears
        new_comment = wait.until(EC.visibility_of_element_located(
            (By.XPATH, f"//*[contains(text(),'{comment_text}')]")
        ))

        self.assertTrue(new_comment.is_displayed(), "Comment was not added")
    
    def test_publish_event_with_invalid_link(self):
        wait = WebDriverWait(self.driver, 10)

        self.login("ta_124@mailinator.com", "Qwerty_1234")
        self.driver.get(self.EVENTS_URL)

        card = self.get_event_card("Eco fest")
        self.click_edit_button(card)
        online_checkbox = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[normalize-space()='Online']")
        ))
        online_checkbox.click()
        link_input = wait.until(EC.visibility_of_element_located(
          (By.XPATH, "//input[@formcontrolname='onlineLink']")
        ))
        link_input.clear()
        link_input.send_keys("http:/invalidmeet.example.com/event")
        link_input.send_keys(Keys.TAB)
        
        error = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//mat-error[contains(text(),'link')]")
        ))
        error_text = error.text.lower()
        self.assertTrue(
            "link" in error_text or "посил" in error_text,
            f"Unexpected error text: {error.text}"
        )

        buttons = self.driver.find_elements(
            By.XPATH,
            "//button[contains(text(),'Publish') or contains(text(),'Опублікувати')]"
        )

        self.assertEqual(len(buttons), 0, "Publish button should not be visible")

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
    
    def generate_event_name(self):
        return f"Test Event {datetime.now().strftime('%H%M%S')}"

if __name__ == "__main__":
    unittest.main()
    