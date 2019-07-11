from src.main.common.page_common_object import Common


class JustMediaScreen(Common):

    def __init__(self, driver):
        self.driver = driver.instance
        self.validate_heading('Which of the following media do you use at least once a week?', 'h1 > p > b')
        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')

    def cannot_go_next_unless_answered(self):
        self.next_button.click()
        assert self.driver.find_element_by_css_selector(
                    'div[class="info_box ng-binding ng-scope"]').text == 'Please select all that apply.'

    def click_one_box(self, option):
        self.list_options[option].click()

    def click_several_boxs(self, options_list):
        self.list_options = self.driver.find_elements_by_css_selector('div > div[class^="question_option"]')
        for option in options_list:
            self.click_one_box(option - 1)

        list_clicked = self.driver.find_elements_by_css_selector('div > input[class^="ng-untouched"]')
        assert len(list_clicked) == len(options_list), '%d != %d' % (len(list_clicked), len(options_list))
