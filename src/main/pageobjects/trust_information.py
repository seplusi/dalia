import time
from selenium.common.exceptions import StaleElementReferenceException


class TrustInformation:

    def __init__(self, driver):
        self.driver = driver.instance
        self.validate_heading('Do you agree or disagree: In general, I trust the information I get from the media.')

        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
        self.list_options = self.driver.find_elements_by_css_selector('div > div[class^="question_option"]')

    def click_one_box(self, option):
        self.list_options[option - 1].click()
        self.driver.find_element_by_css_selector('input[id="answer_6_O00%d0"]:not([class*="ng-pristine"])' % option)
        self.next_button.click()


    def cannot_go_next_unless_answered(self):
        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
        self.next_button.click()
        time.sleep(2)
        self.validate_heading('Do you agree or disagree: In general, I trust the information I get from the media.')

    def validate_heading(self, heading_str):
        for _ in range(10):
            try:
                headings = self.driver.find_elements_by_css_selector('h1 > p > b')
                for heading in headings:
                    if heading.text == heading_str:
                        break
                else:
                    continue
                break
            except StaleElementReferenceException:
                time.sleep(0.1)
                print('where_i_live Stale')
        else:
            assert False

#        for _ in range(10):
#            for element in self.driver.find_elements_by_css_selector('h1 > p > b'):
#                if 'I trust the information' in element.text:
#                    break
#                time.sleep(0.1)
#            else:
#                continue
#            break
#
#        else:
#            assert False, 'I trust the information page wasn\'t loaded'
