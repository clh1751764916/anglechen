#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver import Chrome
import time
import re


driver= webdriver.Chrome()
#访问网站
driver.get('http://xg.fjsdxy.com/SPCP/Sys/UserLogin.aspx')
print(driver.title)
time.sleep(0.5)
#定位用户名  "//input[@id='UserName']"
UserName_el=driver.find_element_by_xpath("//*[@id='UserName']")
#清空表内元素
UserName_el.clear()
#send_keys()在元素上进行输入
UserName_el.send_keys('输入用户名')
time.sleep(0.5)
#定位密码，输入密码//*[@id="Password"]
Password_el=driver.find_element_by_xpath("//*[@id='Password']")
#清空表内元素
Password_el.clear()
Password_el.send_keys('输入密码')
time.sleep(0.5)

#获取全局代码html_text=driver.page_source
#打印print(html_text)

YZM=driver.find_element_by_xpath("//*[@id='code-box']").text 
#定位验证码框，输入验证码"//*[@id='codeInput']"
yzm_el=driver.find_element_by_xpath("//*[@id='codeInput']")
#清空表内元素
yzm_el.clear()
yzm_el.send_keys(YZM)
time.sleep(0.5)


#driver.find_element_by_id() id是唯一的，可以直接定位,queryBtn是登入按钮的id
driver.find_element_by_id('queryBtn').click()


#定位电力工程学院，//*[@id="XYQX"]/a[2]/strong/font
DLGCXY_el=driver.find_element_by_xpath('//*[@id="XYQX"]/a[2]/strong/font').click()
time.sleep(5)


# 进入frame
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="MainSpace"]/frame[2]'))
name=driver.find_elements_by_xpath('//*[@id="GridView1"]/tbody')

leng=["小明","小红","小丽",......,"小白"]

lists=[]
for i in name:
    a=i.text
    lists.append(a)
    lists=str(lists).split(' ') 
    #lists=str(lists).replace(' ',',')

list3=[]
list4=[]
#找相同
for i in leng:
    for j in lists:
        if i ==j:
            list3.append(i)
            
#找不同
for b in(leng):
    if b not in list3:
        list4.append(b)


print(list4)


driver.quit()