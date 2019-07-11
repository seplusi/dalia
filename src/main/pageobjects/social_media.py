import time
from selenium.common.exceptions import StaleElementReferenceException
from src.main.common.page_common_object import Common


class SocialMediaScreen(Common):

    def __init__(self, driver):
        self.driver = driver.instance
        self.validate_heading('Which of these social media platforms do you use at least once a week?', 'h1 > p > b')

    def cannot_go_next_unless_answered(self):
        for _ in range(10):
            try:
                self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
                self.next_button.click()
                assert self.driver.find_element_by_css_selector(
                    'div[class="info_box ng-binding ng-scope"]').text == 'Please select at least 2.'
                break
            except StaleElementReferenceException:
                time.sleep(0.1)
                print('Stale next button')
        else:
            print('Too many stale next button element')
            assert False

    def click_one_box(self, option):
        self.list_options[option].click()

    def click_several_boxs(self, options_list):
        for _ in range(10):
            try:
                self.list_options = self.driver.find_elements_by_css_selector('div > div[class^="question_option"]')
                for option in options_list:
                    self.click_one_box(option - 1)
                break
            except StaleElementReferenceException:
                time.sleep(0.1)
                self.list_options = self.driver.find_elements_by_css_selector('div > div[class^="question_option"]')
                print('stale at option %d' % option)
        else:
            print('Too many stale objects in sococial media page')
            assert False

        list_clicked = self.driver.find_elements_by_css_selector('div > input[class^="ng-untouched"]')
        assert len(list_clicked) == len(options_list), '%d != %d' % (len(list_clicked), len(options_list))

    def click_next(self):
        for _ in range(10):
            try:
                self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
                self.next_button.click()
            except StaleElementReferenceException:
                time.sleep(0.1)
        else:
            print('To many stale click next element')
