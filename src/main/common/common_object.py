from selenium.common.exceptions import StaleElementReferenceException


class Common:

    def check_stale_and_click(self, element):
        if self.link_has_gone_stale(element):
            print('%s % is STALE' %(element.tag_name, element.text))
        element.click()

    def link_has_gone_stale(self, element):
        try:
            # poll the link with an arbitrary call
            self.driver.implicitly_wait(1)
            element.find_elements_by_id('doesnt-matter')
            return False
        except StaleElementReferenceException:
            return True
        finally:
            self.driver.implicitly_wait(30)

    def check_link_stale_and_find(self, element):
        try:
            # poll the link with an arbitrary call
            self.driver.implicitly_wait(1)
            element.find_elements_by_id('doesnt-matter')
            return False
        except StaleElementReferenceException:
            return True
        finally:
            self.driver.implicitly_wait(30)