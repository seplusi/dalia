import time
from selenium.common.exceptions import StaleElementReferenceException


class WhereILive:
    def __init__(self, driver):
        self.driver = driver.instance
        self.validate_heading('Do you live in a city or in a rural area?')
        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
        self.list_options = self.driver.find_elements_by_css_selector('div > div[class^="question_option"]')

    def cannot_go_next_unless_answered(self):
        self.next_button.click()
        time.sleep(2)
        self.validate_heading('Do you live in a city or in a rural area?')

    def validate_heading(self, heading_str):
        for _ in range(10):
            try:
                heading = self.driver.find_element_by_css_selector('h1 > p')
                if heading.text == heading_str:
                    break
            except StaleElementReferenceException:
                time.sleep(0.1)
                print('where_i_live Stale')
        else:
            assert False

    def click_next(self):
        self.next_button.click()

    def click_city_option(self):
        for element in self.list_options:
            if element.find_element_by_css_selector('div[class^="question_option"] > label').text == 'City':
                element.click()
                break

        for element in self.driver.find_elements_by_css_selector('div > div[class^="question_option"]'):
            if element.find_element_by_css_selector('div[class^="question_option"] > label').text == 'City':
                element.find_element_by_css_selector('div > input[class^="ng-untouched"]')
                break
        else:
            assert False