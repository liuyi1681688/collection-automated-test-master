import unittest
from .driver import browser
from Cloud.test_case.page_obj.collectible_page import CollectiblePage


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = browser('chrome')
        cls.driver.implicitly_wait(30)
        cls.driver.set_page_load_timeout(90)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        # print("star")
        pass

    def tearDown(self):
        # print("end")
        pass

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True
