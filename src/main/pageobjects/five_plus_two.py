from src.main.common.page_common_object import Common


class FivePlusTwo(Common):
    def __init__(self, driver):
        self.driver = driver.instance
        self.heading_selector = 'h1 > p'
        self.heading_str = 'What is five plus two?'
        self.validate_heading(self.heading_str, self.heading_selector)
        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')

    def insert_name_and_clock_next(self, name):
        element = self.driver.find_element_by_css_selector('div[class="question_option"] > input')
        element.send_keys(name)
        self.next_button.click()
