#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 11:00:34 2019

@author: kylebradley
"""

from selenium import webdriver

from bs4 import BeautifulSoup



#launch url
url = "https://www.marketwatch.com/search?q=KPMG&m=Keyword&rpp=15&mp=806&bd=false&rs=false&o=16"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)




soup_level1=BeautifulSoup(driver.page_source, 'lxml')

datalist = [] #empty list
x = 0 #counter

#sometimes this breaks
for x in range(50):
    for link in driver.find_elements_by_xpath('//a[@href]'):
        if 'www.marketwatch.com/story' in link.get_attribute('href'):
                datalist.append(link.get_attribute('href'))
    try:
        driver.find_element_by_partial_link_text('Next').click()
    except:
        break

with open('urls.txt', 'w') as f:
    for item in datalist:
        f.write("%s\n" % item)
