from src.main.common.page_common_object import Common


class WelcomeScreen(Common):

    def __init__(self, driver):
        self.driver = driver.instance
        self.heading_selector = 'h1 > p'
        self.heading_str = 'There are 10 questions in the survey'
        self.validate_heading(self.heading_str, self.heading_selector)

        self.understand_box = self.driver.find_element_by_css_selector('label[for^="answer"]')
        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')

    def accept_test_box(self):
        self.understand_box.click()
