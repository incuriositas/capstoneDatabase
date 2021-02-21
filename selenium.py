# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("http://dreamy.jejunu.ac.kr/frame/index.do")

driver.find_element_by_name('userid').send_keys('아이디입력'))
driver.find_element_by_name('password').send_keys('비밀번호입력')
driver.find_element_by_id('act_lgn').click()

iframes=driver.find_elements_by_tag_name('iframe')
driver.switch_to_frame("leftFrame")
# 교양교육과정관리
driver.find_element_by_xpath(
    '//*[@id="mainleft"]/div[2]/table/tbody/tr/td[2]').click()
# 전공교육과정조회
driver.find_element_by_xpath('//*[@id="sta_su_3100e"]').click()
# 교양교육과정조회
# driver.find_element_by_xpath('//*[@id="sta_su_3090e"]').click()

driver.switch_to_default_content()
iframes=driver.find_elements_by_tag_name('iframe')
driver.switch_to_frame("centerFrame")
driver.find_element_by_id('curri_year').clear()
driver.find_element_by_id('curri_year').send_keys('2020')

# 대학 : 제주대학교
driver.find_element_by_xpath('//*[@id="univ_cd"]/option[17]').click()

# 학과 : 연계전공
driver.find_element_by_xpath('//*[@id="cls_cd"]/option[4]').click()

# "관광융합소프트웨어",
# driver.find_element_by_xpath('//*[@id="maj_cd"]/option[12]]').click()
# "스마트그리드",
# driver.find_element_by_xpath('//*[@id="maj_cd"]/option[17]').click()
# "신재생에너지",
# driver.find_element_by_xpath('//*[@id="maj_cd"]/option[18]]').click()
# "전기자동차",
# driver.find_element_by_xpath('//*[@id="maj_cd"]/option[19]').click()
# "스마트관광",
# driver.find_element_by_xpath('//*[@id="maj_cd"]/option[24]').click()
# "빅데이터융합",
# driver.find_element_by_xpath('//*[@id="maj_cd"]/option[25]').click()
# "블록체인보안"
driver.find_element_by_xpath('//*[@id="maj_cd"]/option[26]').click()

driver.find_element_by_id('searchSubject').click()

subject=[]

def getData():
    table=driver.find_element_by_xpath(
        '//*[@id="gridMst_container"]/table/tbody/tr[2]/td/div/div/table')
    data=table.find_elements_by_tag_name("tr")
    for i in range(len(data)-1):
        subject.append(data[i+1].text)
