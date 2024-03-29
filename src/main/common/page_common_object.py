from selenium.common.exceptions import StaleElementReferenceException
import time


class Common:
    def __init__(self, driver):
        self.driver = driver.instance

    def validate_heading(self, heading_str, selector):
        for _ in range(10):
            try:
                headings = self.driver.find_elements_by_css_selector(selector)
                for heading in headings:
                    if heading.text == heading_str:
                        break
                else:
                    continue
                break
            except StaleElementReferenceException:
                time.sleep(0.1)
                print('selector % s is stale' % selector)
        else:
            print('Couldn\'t find heading %s' % heading_str)
            assert False

    def cannot_go_next_unless_answered_without_err_message(self):
        self.next_button.click()
        time.sleep(2)
        self.validate_heading(self.heading_str, self.heading_selector)

    def click_next(self):
        self.next_button.click()
