#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import ErrorInResponseException
from selenium.webdriver.common.action_chains import ActionChains


class Page(object):
    '''Base class for all Pages'''

    def __init__(self, testsetup):
        '''Constructor'''
        self.base_url = testsetup.current_url
        self.selenium = testsetup

    @property
    def olb_title(self):
        WebDriverWait(self, 10).until(lambda s: s.selenium.title)
        return self.selenium.title

    def olb_maximize_window(self):
        self.selenium.maximize_window()

    def olb_is_displayed(self, locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except (NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException):
            return False

    def olb_find_element(self, locator):
        try:
            result = self.selenium.find_element(*locator)
            return result
        except (NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException, ErrorInResponseException):
            return None

    def olb_text(self, locator):
       return self.selenium.find_element(*locator).text

    def olb_send_keys(self, locator, value):
        if value == '' or value == [] or value is None or value == {} or value == ():
            return
        else: return self.selenium.find_element(*locator).send_keys(value)

    def olb_click(self, locator):
        return self.selenium.find_element(*locator).click()

    def olb_clear(self, locator):
        return self.selenium.find_element(*locator).clear()

    def olb_mouse_hover(self, locator):
        hover = ActionChains(self.selenium).move_to_element(locator)
        WebDriverWait(self.selenium, 1)
        hover.perform()
        WebDriverWait(self.selenium, 1)

    def olb_wait_for_present(self, locator):
        WebDriverWait(self.selenium, self.timeout).until(EC.presence_of_element_located(locator),
                                                         'The element has not loaded.')
