import time
from src.main.common.page_common_object import Common


class PreferenceAboutMovie(Common):
    def __init__(self, driver, film_name):
        self.driver = driver.instance
        self.film_name = film_name
        self.heading_selector = 'h1 > p'
        self.validate_heading('What do you like most about %s?' % film_name, self.heading_selector)
        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
        self.list_options = self.driver.find_elements_by_css_selector('div > div[class^="question_option"]')

    def cannot_go_next_unless_answered(self, ):
        self.next_button.click()
        time.sleep(2)
        self.validate_heading('What do you like most about %s?' % self.film_name, self.heading_selector)

    def click_next(self):
        self.next_button.click()

    def click_option(self, option_str):
        for element in self.list_options:
            if element.find_element_by_css_selector('div[class^="question_option"] > label').text == option_str:
                element.click()
                break

        for element in self.driver.find_elements_by_css_selector('div > div[class^="question_option"]'):
            if element.find_element_by_css_selector('div[class^="question_option"] > label').text == option_str:
                element.find_element_by_css_selector('div > input[class^="ng-untouched"]')
                break
        else:
            assert False