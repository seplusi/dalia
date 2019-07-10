import time
from selenium.common.exceptions import StaleElementReferenceException


class FivePlusTwo:
    def __init__(self, driver):
        self.driver = driver.instance
        self.validate_heading()
        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')

    def cannot_go_next_unless_answered(self):
        self.next_button.click()
        time.sleep(2)
        self.validate_heading()

    def insert_name_and_clock_next(self, name):
        element = self.driver.find_element_by_css_selector('div[class="question_option"] > input')
        element.send_keys(name)
        self.next_button.click()

    def validate_heading(self):
        for _ in range(10):
            try:
                heading = self.driver.find_element_by_css_selector('h1 > p')
                if heading.text == 'What is five plus two?':
                    break
            except StaleElementReferenceException:
                time.sleep(0.1)
                print('five_plus_tw0 Stale')
        else:
            assert False
