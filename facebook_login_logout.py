#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

mail_id = ''
pass_id = ''


driver = webdriver.Chrome()


def nav_to_facebook():
    global driver
    driver.get('http://www.facebook.com')


def log_in():
    global mail_id
    global driver
    mail = driver.find_element_by_id('email')
    mail.send_keys(mail_id)
    password = driver.find_element_by_id('pass')
    password.send_keys(pass_id)
    password.send_keys(Keys.ENTER)


def log_out():
    global driver
    logout_nav = driver.find_element_by_id('userNavigationLabel')
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(8)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    logout_nav.click()
    time.sleep(2)
    driver.find_element_by_partial_link_text('Log Out').click()


if __name__ == '__main__':
    nav_to_facebook()
    log_in()
    log_out()
    driver.quit()