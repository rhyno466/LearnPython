# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:00:20 2022

@author: rhyno
"""

from selenium import webdriver
import time

usr = "rhyno466@gmail.com"
pss = "Rhynoek0612"

dr = webdriver.Chrome()

dr.get("https://www.ifit.com")
print(dr.title)

li = dr.find_element_by_xpath(
    '//*[@id="__next"]/div/div[2]/header/div[1]/div/div/div/a/a'
).click()
time.sleep(5)

e = dr.find_element_by_xpath('//*[@id="1-email"]')
e.send_keys(usr)

p = dr.find_element_by_xpath(
    '//*[@id="ifit-login-container"]/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div[3]/div[2]/div[1]/div/input'
)
p.send_keys(pss)

yup = dr.find_element_by_xpath(
    '//*[@id="ifit-login-container"]/div/div/form/div/div/div/button/span'
).click()


time.sleep(5)

# wo = dr.find_element_by_xpath(
#     '//*[@id="navbar-inner-elem"]/div/div[1]/ul/li[1]/ul/li[3]/a'
# ).click()
# btr = dr.get('ttps://www.ifit.com/me/workouts')
# //*[@id="navbar-inner-elem"]/div/div[1]/ul/li[1]/ul/li[3]/a
btr = dr.find_element_by_xpath('//*[@id="navbar-inner-elem"]/a').click()

time.sleep(5)

ebtr = dr.find_element_by_xpath(
    '//*[@id="navbar-inner-elem"]/div/div[1]/ul/li[1]/ul/li[3]/a'
).click()

time.sleep(5)

wo = dr.find_element_by_xpath(
    '//*[@id="workout-table-bar-headers"]/div/div[2]/div[2]/a'
).click()

time.sleep(5)


ex = dr.find_element_by_xpath(
    '//*[@id="main"]/div[2]/div/div[1]/div[1]/div[4]/div/a'
).click()

time.sleep(5)


strUrl = dr.current_url
print(strUrl)


# out_q = dr.find_element_by_xpath(
#     '///*[@id="main"]/div[2]/div/div[1]/div[1]/div[4]/div/ul/li[1]/a'
# ).click()

dr.find_element_by_xpath(
    "//a[@href=/workout/export/tcx/61ed82fced3fde28748d07c6)]" ""
).cilck()

# <a href="/workout/export/tcx/61ed82fced3fde28748d07c6" target="_exportPane">TCX</a>
# driver.find_element_by_xpath('//a[contains(@href,"href")]')
# //*[@id="main"]/div[2]/div/div[1]/div[1]/div[4]/div/ul/li[1]/a


# //*[@id="main"]/div[2]/div/div[1]/div[1]/div[4]/div/ul/li[1]/a


# //*[@id="main"]/div[2]/div/div[1]/div[1]/div[4]/div/a

# //*[@id="workout-table-bar-headers"]/div/div[2]/div[2]/a

# //*[@id="navbar-inner-elem"]/div/div[1]/ul/li[1]/ul/li[3]/a
# //*[@id="navbar-inner-elem"]/a

# //*[@id="ifit-login-container"]/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div[3]/div[2]/div[1]/div/input


# dr.switch_to.f(f)
pass1 = dr.find_element_by_id("1-email")


em = dr.find_element_by_name('email')
em = dr.find_element_by_class_name('auth0-lock-input')
em = dr.find_element_by_id('1-email')
# li.click()
