from src.main.common.page_common_object import Common


class FavouriteFilm(Common):
    def __init__(self, driver):
        self.driver = driver.instance
        self.heading_selector = 'h1 > p'
        self.heading_str = 'Which is your favourite from these award-winning films?'
        self.validate_heading(self.heading_str, self.heading_selector)
        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')
        self.list_options = self.driver.find_elements_by_css_selector('div > div[class^="question_option"]')

    def click_option(self, option_str):
        for element in self.list_options:
            if element.find_element_by_css_selector('div[class^="question_option"] > label').text == option_str:
                element.click()
                break

        for element in self.driver.find_elements_by_css_selector('div > div[class^="question_option"]'):
            if element.find_element_by_css_selector('div[class^="question_option"] > label').text == option_str:
                element.find_element_by_css_selector('div > input[class^="ng-untouched"]')
                break
        else:
            assert False