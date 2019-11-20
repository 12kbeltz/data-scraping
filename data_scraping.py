# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:46:55 2019

@author: 12kbe
"""

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# opens Chrome driver to initiate site scripts, pull data and close chrome
driver = webdriver.Chrome()
driver.get('https://ultrasignup.com/results_event.aspx?did=62105')
results = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

soup = BeautifulSoup(results,'lxml')

tables = soup.find_all('table', {'class': 'ui-jqgrid-btable'})

# pulls data from table into list
for i in tables:
    td = i.find_all('td')
strings = []
for i in td:
    strings.append(i.string)

while None in strings:
    strings.remove(None)

# turns list into DataFrame
data_final = pd.DataFrame(np.array(strings).reshape(len(strings)//14,14),
                          columns = ['Place','First','Last','City','ST','Age',
                                'G','GP','Time','Rank',11,'Age_Cat',13,14])

#check what 13 and 14 are - might combine people
data_final = data_final.drop(columns=[11])

data_final.to_excel('HAT_RUN_DATA.xlsx')