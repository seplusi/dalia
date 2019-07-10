class HoursReadPerDay:

    def __init__(self, driver):
        self.driver = driver.instance

        self.dont_read_news_box = self.driver.find_element_by_css_selector('label[for="answer_2_O0010"]')
        self.one_2_three_box = self.driver.find_element_by_css_selector('label[for="answer_2_O0020"]')
        self.four_2_five_box = self.driver.find_element_by_css_selector('label[for="answer_2_O0030"]')
        self.more_than_seven_box = self.driver.find_element_by_css_selector('label[for="answer_2_O0040"]')
        self.next_button = self.driver.find_element_by_css_selector('button[ng-class^="{\'is_disabled"][class^="btn next_button"]')
        self.go_back_button = self.driver.find_element_by_css_selector('a[class="btn back_button"]')
        self.options = {'answer_2_O0010': self.dont_read_news_box, 'answer_2_O0020': self.one_2_three_box, 'answer_2_O0030': self.four_2_five_box, 'answer_2_O0040': self.more_than_seven_box}

    def cannot_go_next_unless_answered(self):
        self.next_button.click()
        assert self.driver.find_element_by_css_selector('div[class="info_box ng-binding ng-scope"]').text == 'INSTRUCTION: Please select one.'

    def click_one_box(self, option):
        self.options[option].click()
        self.driver.find_element_by_css_selector('input[id="%s"]:not([class*="ng-pristine"])' % option)
        self.click_next()

    def click_next(self):
        self.next_button.click()