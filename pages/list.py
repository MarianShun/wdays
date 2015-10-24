#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Page object for a List Page'''
 
from selenium.webdriver.common.by import By
 
from general_page import Page
 
 
class ListPage(Page):
 
    @property
    def is_404(self):
        return '404 Not Found' in self.olb_title
 
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
    def is_item_in_list(self, item_name):
        try:
            self.selenium.find_elements_by_partial_link_text(item_name)
            return True
        except: return False
