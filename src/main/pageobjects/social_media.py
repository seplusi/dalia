from src.main.common.common_object import Common


class SocialMediaScreen(Common):

    def __init__(self, driver):
        self.driver = driver.instance

#        for element in self.driver.find_elements_by_css_selector('h1 > p > b'):
#            if 'Which of these social media' in element.text:
#                break
#        else:
#            assert False, 'Social Media page wasn\'t loaded'

        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
        self.list_options = self.driver.find_elements_by_css_selector('div > div[class^="question_option"]')

    def cannot_go_next_unless_answered(self):
#        self.next_button.click()
        self.check_stale_and_click(self.next_button)
        assert self.driver.find_element_by_css_selector('div[class="info_box ng-binding ng-scope"]').text == 'Please select at least 2.'

    def click_one_box(self, option):
#        self.list_options[option].click()
        self.check_stale_and_click(self.list_options[option])
        self.click_next()

    def click_several_boxs(self, options_list):
        for option in options_list:
            self.click_one_box(option - 1)
        for element in self.driver.find_element_by_css_selector('input[id=""]:not([class*="ng-pristine"])'):
            pass
#        self.driver.find_element_by_css_selector('input[id="%s"]:not([class*="ng-pristine"])' % option)
#        self.click_next()

    def click_next(self):
        self.next_button.click()