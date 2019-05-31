#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import selenium
from selenium import webdriver

user_id = 'mngr198611'
pass_word = 'nEpugUs'
pass_word = 'boom'

driver = webdriver.Chrome()


def nav_to_site():
    global driver
    driver.get('http://www.demo.guru99.com/V4/')


def login():
    global driver
    username = driver.find_element_by_name('uid')
    password = driver.find_element_by_name('password')
    login_btn = driver.find_element_by_name('btnLogin')
    username.send_keys(user_id)
    password.send_keys(pass_word)
    login_btn.click()
    try:
        current_page = driver.current_url
        if current_page.endswith('manager/Managerhomepage.php'):
            return True
        else:
            return False
    except selenium.common.exceptions.UnexpectedAlertPresentException:
        return False


if __name__ == '__main__':
    nav_to_site()
    print(login())
    driver.quit()