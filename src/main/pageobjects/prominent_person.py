import time
from selenium.common.exceptions import StaleElementReferenceException


class ProminentPerson:

    def __init__(self, driver):
        self.driver = driver.instance
        self.verify_page_heading()

    def verify_page_heading(self):
        for _ in range(10):
            try:
                heading = self.driver.find_element_by_css_selector('h1 > p > b')
                if 'one PROMINENT' in heading.text:
                    break
            except StaleElementReferenceException:
                time.sleep(0.1)
                print('Prominent Stale')
        else:
            assert False

    def cannot_go_next_unless_answered(self):
        for _ in range(10):
            try:
                self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
                print('Got NEXT button')
                self.next_button.click()
                print('Clicked NEXT button')
                time.sleep(2)
                self.verify_page_heading()
                break
            except StaleElementReferenceException:
                time.sleep(0.1)
                print('Prominent Stale')

    def insert_name_and_clock_next(self, name):
        element = self.driver.find_element_by_css_selector('div[class="question_option"] > input')
        element.send_keys(name)
        self.next_button.click()