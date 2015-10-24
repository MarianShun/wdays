#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pages.list import ItemList
from pages.item import ItemPage
from data.urls import urls
 
class Test404:
    @pytest.mark.nondestructive
    @pytest.mark.parametrize('url', urls)
    def test_pages_to_satisfy(self, selenium, url):
        selenium.get(url)
        item_page = ItemPage(selenium)
        item_name = item_page.item_name
        item_page.some_steps_with_item()
        item_page.click_save()
        
        item_list = ItemList(selenium)
        assert item_list.is_success_message
        assert not item_list.is_item_in_list(item_name)
        
