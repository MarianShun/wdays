#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Page object for a List Page'''
 
from selenium.webdriver.common.by import By
 
from pages.general_page import Page
 
 
class ItemPage(Page):
 
    @property
    def item_name(self):
        _item_name_locator = (By.CLASS_NAME, 'name') 
        return self.olb_find_element(_item_name_locator)
  
    @property
    def is_article_not_found(self):
        result = False
        _no_article_message_locator = By.CLASS_NAME, "mbox-text"
        mes = self.selenium.find_elements(*_no_article_message_locator)
        if mes:
            if u'Вікіпедія не має статті з саме цією назвою' in mes[0].text or \
                            self.olb_title == u'Вікіпедія':  # Wiki main page
                result = True
        return result
        
    @property
    def some_steps_with_item(self):
        pass
        
    def click_save(self):
        _save_locator = (By.ID, 'name')
        self.olb_find_element(_save_locator).click()
