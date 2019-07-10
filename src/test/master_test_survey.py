import unittest
from src.main.common.driver import Driver
from src.main.pageobjects.welcome_page import WelcomeScreen
from src.main.pageobjects.hours_read_per_day import HoursReadPerDay
from src.main.pageobjects.social_media import SocialMediaScreen
from src.main.pageobjects.just_media import JustMediaScreen
from src.main.pageobjects.prominent_person import ProminentPerson
from src.main.pageobjects.trust_information import TrustInformation
from src.main.pageobjects.five_plus_two import FivePlusTwo
from src.main.pageobjects.where_live import WhereILive
from src.main.pageobjects.favourite_film import FavouriteFilm
from src.main.pageobjects.preferfence_about_movie import PreferenceAboutMovie


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

        self.trust_info = TrustInformation(self.driver)
        self.trust_info.cannot_go_next_unless_answered()
        self.trust_info.click_one_box(1)

        self.five_plus_two = FivePlusTwo(self.driver)
        self.five_plus_two.cannot_go_next_unless_answered()
        self.five_plus_two.insert_name_and_clock_next(7)

        self.where_live = WhereILive(self.driver)
        self.where_live.cannot_go_next_unless_answered()
        self.where_live.click_city_option()
        self.where_live.click_next()

        self.favourite_film = FavouriteFilm(self.driver)
        self.favourite_film.cannot_go_next_unless_answered()
        self.favourite_film.click_option('Gandhi')
        self.favourite_film.click_next()

        self.preference = PreferenceAboutMovie(self.driver, 'Gandhi')
        self.preference.cannot_go_next_unless_answered()
        self.preference.click_option('Editing')
        self.preference.click_next()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.instance.quit()

if __name__ == "__main__":
    unittest.main()
