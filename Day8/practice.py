# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:30:26 2019

@author: KIIT
"""

url = "http://court.mah.nic.in/courtweb/index_eng.php#"
browser = webdriver.Chrome('D:\programs\python\Programs\Day8\selenium\chromedriver.exe')
browser.get(url)


#//*[@id="sess_dist_code"]
#//*[@id="sess_dist_code"]/option[17]


click = browser.find_element_by_xpath('//*[@id="sess_dist_code"]')
click.click()

sleep(4)

code = browser.find_element_by_xpath('#//*[@id="sess_dist_code"]/option[17]')
click.send_keys(code)

sleep(4)

