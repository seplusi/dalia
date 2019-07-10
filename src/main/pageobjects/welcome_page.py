class WelcomeScreen():

    def __init__(self, driver):
        self.driver = driver.instance

        self.understand_box = self.driver.find_element_by_css_selector('label[for^="answer"]')
        self.next_button = self.driver.find_element_by_css_selector('button[class^="btn next_button"]')

    def accept_test_box(self):
        self.understand_box.click()

    def click_next(self):
        self.next_button.click()