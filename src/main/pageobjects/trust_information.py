from src.main.common.page_common_object import Common


class TrustInformation(Common):

    def __init__(self, driver):
        self.driver = driver.instance
        self.heading_selector = 'h1 > p > b'
        self.heading_str = 'Do you agree or disagree: In general, I trust the information I get from the media.'
        self.validate_heading(self.heading_str, self.heading_selector)

        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
        self.list_options = self.driver.find_elements_by_css_selector('div > div[class^="question_option"]')

    def click_one_box(self, option):
        self.list_options[option - 1].click()
        self.driver.find_element_by_css_selector('input[id="answer_6_O00%d0"]:not([class*="ng-pristine"])' % option)
        self.next_button.click()
