import unittest
from src.main.common.driver import Driver
from src.main.pageobjects.welcome_page import WelcomeScreen
from src.main.pageobjects.hours_read_per_day import HoursReadPerDay
from src.main.pageobjects.social_media import SocialMediaScreen
from src.main.pageobjects.just_media import JustMediaScreen
from src.main.pageobjects.prominent_person import ProminentPerson


class eurosportMotorsport(unittest.TestCase):
    """A sample test class to show how page object works"""

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver()

    def setUp(self):
        self.driver.navigate("https://surveyinterface-v2.opinionsample.com/#/surveys/ab320070-bbad-0134-bb62-0a6b3886cf3d/init?publisher_user_id=07bfe320-86d2-0131-c9aa-0a424708edaa&panel_user_id=PANEL_USER_TEST_c75236c0-bbad-0134-bbe2-0a6b3886cf3d&panel_user_id_kind=PANEL_USER_KIND_TEST&pparam_offer_click_id=OFFER_CLICK_TEST_c75236c0-bbad-0134-bbe2-0a6b3886cf3d&is_test=true")
        self.welcome_screen = WelcomeScreen(self.driver)

#    @unittest.skip('')
    def test_fullsurvey_happy_path(self):
        self.welcome_screen.accept_test_box()
        self.welcome_screen.click_next()

        self.hours_read_day = HoursReadPerDay(self.driver)
        self.hours_read_day.cannot_go_next_unless_answered()
        self.hours_read_day.click_one_box('answer_2_O0010')

        self.social_media = SocialMediaScreen(self.driver)
        self.social_media.cannot_go_next_unless_answered()
        self.social_media.click_several_boxs([1, 2, 3])
        self.social_media.click_next()

        self.just_media = JustMediaScreen(self.driver)
        self.just_media.cannot_go_next_unless_answered()
        self.just_media.click_several_boxs([2, 3])
        self.just_media.click_next()

        self.person = ProminentPerson(self.driver)
        self.person.cannot_go_next_unless_answered()
        self.person.insert_name_and_clock_next('Hover')
        print('Hello World')
 #       self.homepage.click_motorsports()
 #       MotorsportScreen(self.driver)
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.instance.quit()

if __name__ == "__main__":
    unittest.main()
