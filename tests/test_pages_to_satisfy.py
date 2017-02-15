#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from pages.item import ItemPage
from data.urls import urls


class Test404:

    @classmethod
    def setup(cls):
        pass

    @classmethod
    def teardown(cls):
        pass

    @pytest.mark.parametrize('url', urls)
    def test_pages_to_satisfy(self, selenium, url):
        selenium.get(url)
        item_page = ItemPage(selenium)
        item_name = item_page.item_name

        item_page.some_steps_with_item()

        assert not item_page.is_article_not_found

    def test_search_exists(self, selenium, url):
        selenium.get(url)

        item_page = ItemPage(selenium)
        assert item_page.is_search_field_present

