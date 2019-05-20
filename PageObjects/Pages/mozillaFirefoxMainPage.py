import time
from PageObjects.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class mozilla_Firefox_Main_Page():
    def __init__(self, driver):
        self.driver = driver
        self.main_page_mozilla_logo = Locators.mozilla_main_logo
        self.main_page_mozilla_language_link = Locators.all_languages_link

    def get_mozilla_main_page_logo(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, Locators.mozilla_main_logo))
            )
        except TimeoutException:
            print("Mozilla Main Page Logo Has Not Loaded")
        return self.driver.find_element_by_xpath(Locators.mozilla_main_logo)

    def access_mozilla_all_lang_link(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, Locators.all_languages_link))
            )
        except TimeoutException:
            print("Mozilla Main Page Languages Link Has Not Loaded")
        try:
            self.driver.find_element_by_xpath(Locators.all_languages_link).click()
        except StaleElementReferenceException as STException:
            print('StaleElementReferenceException while clicking language link. Trying functionality again')
            self.driver.find_element_by_xpath(Locators.all_languages_link).click()
        except TimeoutException as TOException:
            print('TimeoutException while clicking language link. Trying functionality again')
            self.driver.find_element_by_xpath(Locators.all_languages_link).click()


