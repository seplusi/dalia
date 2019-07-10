import time
from selenium.common.exceptions import StaleElementReferenceException


class SocialMediaScreen():

    def __init__(self, driver):
        self.driver = driver.instance

        for _ in range(10):
            try:
                for element in self.driver.find_elements_by_css_selector('h1 > p > b'):
                    if 'Which of these social media' in element.text:
                        break
                else:
                    continue
                break

            except StaleElementReferenceException:
                time.sleep(0.1)

        else:
            assert False, 'Social Media page wasn\'t loaded'

    def cannot_go_next_unless_answered(self):
        for _ in range(10):
            try:
                self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
                print('Got NEXT button')
                self.next_button.click()
                print('Clicked NEXT button')
                assert self.driver.find_element_by_css_selector(
                    'div[class="info_box ng-binding ng-scope"]').text == 'Please select at least 2.'
                print('Performed NEXT assertion')
                break
            except StaleElementReferenceException:
                time.sleep(0.1)
                print('Stale next button')

    def click_one_box(self, option):
        self.list_options[option].click()
#        self.check_stale_and_click(self.list_options[option])
#        self.click_next()

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

        list_clicked = self.driver.find_elements_by_css_selector('div > input[class^="ng-untouched"]')
        assert len(list_clicked) == len(options_list), '%d != %d' % (len(list_clicked), len(options_list))
#        self.driver.find_element_by_css_selector('input[id="%s"]:not([class*="ng-pristine"])' % option)
#        self.click_next()

    def click_next(self):
        for _ in range(10):
            try:
                self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
                print('Got NEXT button')
                self.next_button.click()
            except StaleElementReferenceException:
                time.sleep(0.1)