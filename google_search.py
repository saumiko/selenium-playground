#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import json
import time

how_many_pages = 3
query_file = 'search.csv'

driver = webdriver.Chrome()


def nav_to_google():
    global driver
    driver.get('http://www.google.com')


def search(query):
    global driver
    input_box = driver.find_element_by_name('q')
    input_box.send_keys(query)
    input_box.send_keys(Keys.ENTER)


def scroll():
    global driver
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)


def next_page():
    global driver
    driver.find_element_by_partial_link_text('পরবর্তী').click()


def get_queries():
    query_list = []
    with open(query_file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                q = row[0]
                query_list.append(q)
                line_count += 1
    return query_list


def get_result_links():
    global driver
    links = driver.find_elements_by_class_name('rc')
    results = []
    for link in links:
        title = link.find_element_by_css_selector('h3')
        url = link.find_element_by_css_selector('a')
        result = {
            'title': title.text,
            'url': url.get_attribute('href')
        }
        results.append(result)
    return results


if __name__ == '__main__':
    search_results = {
        'query_list': []
    }
    for query in get_queries():
        results = []
        nav_to_google()
        search(query)
        for i in range(how_many_pages):
            for result in get_result_links():
                results.append(result)
            scroll()
            time.sleep(1)
            next_page()
        final_result_for_query = {
            'query': query,
            'results': results
        }
        search_results['query_list'].append(final_result_for_query)
    with open('output.json', 'w') as outfile:
        json.dump(search_results, outfile)
    driver.quit()
