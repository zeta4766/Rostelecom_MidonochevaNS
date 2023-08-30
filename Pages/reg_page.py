import random

from selenium.webdriver import Keys

from Pages.base_page import *
from Pages.locators import *

import time, os


class RegPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/"
        driver.get(url)
        reg_button = driver.find_element(*BaseLocator.REGISTRATION)
        reg_button.click()
        # создаем нужные элементы
        self.driver = driver
        self.firstname = driver.find_element(*RegLocators.REG_FIRSTNAME)
        self.lastname = driver.find_element(*RegLocators.REG_LASTNAME)
        self.address = driver.find_element(*RegLocators.REG_ADDRESS)
        self.password = driver.find_element(*RegLocators.REG_PASSWORD)
        self.password_confirm = driver.find_element(*RegLocators.REG_PASSWORD_CONF)
        self.labels = driver.find_elements(*RegLocators.REG_LABELS)
        self.button = driver.find_element(*RegLocators.REG_BUTTON)
        self.dropdown = driver.find_element(*RegLocators.REG_DROPDOWN)
        self.eyes = driver.find_elements(*RegLocators.EYES)



    def enter_firstname(self, value):
        self.firstname.send_keys(value)

    def enter_lastname(self, value):
        self.lastname.send_keys(value)

    def enter_address(self, value):
        self.address.send_keys(value)

    def clear_address(self):
        self.address.send_keys(Keys.CONTROL + "a", Keys.DELETE)

    def enter_password(self, value):
        self.password.send_keys(value)

    def clear_password(self):
        self.password.send_keys(Keys.CONTROL + "a", Keys.DELETE)

    def enter_password_confirm(self, value):
        self.password_confirm.send_keys(value)

    def clear_password_confirm(self):
        self.password_confirm.send_keys(Keys.CONTROL + "a", Keys.DELETE)

    def button_click(self):
        self.button.click()

    def dropdown_click(self):
        self.dropdown.click()

    def eye_password_click(self):
        self.eyes[0].click()

    def eye_password_confirm_click(self):
        self.eyes[1].click()

    def option_click(self):
        options = self.driver.find_elements(*RegLocators.REG_OPTIONS)
        n = random.randrange(len(options))
        text = options[n].text
        options[n].click()
        return text

    def return_region_name(self):
        labels = self.driver.find_elements(*RegLocators.LABELS)
        return labels[2].get_attribute("innerText")

    def back_address_click(self):
        self.back_address = self.driver.find_element(*ConfirmLocators.BACK_ADDRESS)
        self.back_address.click()

    def return_all_information(self):
        labels = self.driver.find_elements(*RegLocators.LABELS)
        return [i.get_attribute("innerText") for i in labels]

    def enter_confirm_code(self, value):
        self.driver.find_element(*ConfirmLocators.CONFIRM_CODE).send_keys(value)
