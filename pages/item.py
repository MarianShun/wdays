#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Page object for a List Page'''
 
from selenium.webdriver.common.by import By
 
from general_page import Page
 
 
class ListPage(Page):
 
    @property
    def item_name(self):
        _item_name_locator = (By.CLASS_NAME, 'name') 
        return self.olb_find_element(_item_name_locator)
  
    @property
    def is_success_message(self):
        result = False
        mes = self.selenium.find_elements_by_class_name('note-msg')
        if mes:
            if u'Der er ikke nogen produkter, som matcher de kriterier, du har angivet.' in mes[0].text\
                    or u'Vi fandt desværre ingen varer, som passer til dine søgekriterier.' in mes[0].text:
                result = True
        return result
        
    @property
    def some_steps_with_item():
        pass
        
    def click_save(self):
        _save_locator = (By.ID, 'name')
        self.olb_find_element(_save_locator).click()
