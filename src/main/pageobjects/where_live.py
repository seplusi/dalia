from src.main.common.page_common_object import Common


class WhereILive(Common):
    def __init__(self, driver):
        self.driver = driver.instance
        self.heading_selector = 'h1 > p'
        self.heading_str = 'Do you live in a city or in a rural area?'
        self.validate_heading(self.heading_str, self.heading_selector)
        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
        self.list_options = self.driver.find_elements_by_css_selector('div > div[class^="question_option"]')

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