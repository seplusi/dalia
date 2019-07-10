class JustMediaScreen():

    def __init__(self, driver):
        self.driver = driver.instance

        for element in self.driver.find_elements_by_css_selector('h1 > p > b'):
                if 'Which of the following media do' in element.text:
                    break
        else:
            assert False, 'Social Media page wasn\'t loaded'

        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')

    def cannot_go_next_unless_answered(self):
        self.next_button.click()
        assert self.driver.find_element_by_css_selector(
                    'div[class="info_box ng-binding ng-scope"]').text == 'Please select all that apply.'

    def click_one_box(self, option):
        self.list_options[option].click()
#        self.check_stale_and_click(self.list_options[option])
#        self.click_next()

    def click_several_boxs(self, options_list):
        self.list_options = self.driver.find_elements_by_css_selector('div > div[class^="question_option"]')
        for option in options_list:
            self.click_one_box(option - 1)

        list_clicked = self.driver.find_elements_by_css_selector('div > input[class^="ng-untouched"]')
        print(len(list_clicked))
        assert len(list_clicked) == len(options_list), '%d != %d' % (len(list_clicked), len(options_list))
#        self.driver.find_element_by_css_selector('input[id="%s"]:not([class*="ng-pristine"])' % option)
#        self.click_next()

    def click_next(self):
        self.next_button.click()
