import time
from selenium.common.exceptions import StaleElementReferenceException
from src.main.common.page_common_object import Common


class ProminentPerson(Common):

    def __init__(self, driver):
        self.driver = driver.instance
        self.validate_heading('If given the chance to learn all the secrets of one PROMINENT PERSON, '
                              'whose secrets would you like to know?', 'h1 > p > b')

    def cannot_go_next_unless_answered(self):
        for _ in range(10):
            try:
                self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
                self.next_button.click()
                break
            except StaleElementReferenceException:
                time.sleep(0.1)
                print('Prominent Stale')
        else:
            print('Too many stale objects failed attempts for next button click')
            assert False

        time.sleep(2)
        self.validate_heading('If given the chance to learn all the secrets of one PROMINENT PERSON, '
                              'whose secrets would you like to know?', 'h1 > p > b')

    def insert_name_and_click_next(self, name):
        element = self.driver.find_element_by_css_selector('div[class="question_option"] > input')
        element.send_keys(name)
        self.next_button.click()