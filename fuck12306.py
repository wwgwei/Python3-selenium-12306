import os
import sys
import selenium
from bs4 import BeautifulSoup
import win32api
import win32con
import selenium.webdriver.common.keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import PIL
import image
import posixpath
import pyexpat

# 定义一个出发地
fromstation='fs=%E7%9B%8A%E9%98%B3'

# 定义目的地
tostation='ts=%E9%95%BF%E6%B2%99'

# 定义日期
data='data=2019-01-18'

# 拼接URL
url='https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&' + fromstation + ',AEQ&' + tostation +',CSQ&' + data +'&flag=N,N,Y'

# url='https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E7%9B%8A%E9%98%B3,AEQ&ts=%E9%95%BF%E6%B2%99,CSQ&date=2019-01-02&flag=N,N,Y'

drive=webdriver.Firefox()

drive.get(url)

# 设置等待事件，确保网页加载完毕
time.sleep(3)

# 勾选对应的车次，不需要选择的注释掉即可
drive.find_element_by_xpath(xpath="/html/body/div[7]/div[5]/div[2]/div[2]/div[2]/ul/li[1]/label").click()#勾选高铁/城铁（G/C）
drive.find_element_by_xpath(xpath="/html/body/div[7]/div[5]/div[2]/div[2]/div[2]/ul/li[2]/label").click()#勾选动车（D）
# drive.find_element_by_xpath(xpath="/html/body/div[7]/div[5]/div[2]/div[2]/div[2]/ul/li[3]/label").click()#勾选直达（Z）
# drive.find_element_by_xpath(xpath="/html/body/div[7]/div[5]/div[2]/div[2]/div[2]/ul/li[4]/label").click()#勾选特快（T）
# drive.find_element_by_xpath(xpath="/html/body/div[7]/div[5]/div[2]/div[2]/div[2]/ul/li[5]/label").click()#勾选快速（K）

# 点击预定按钮
drive.find_element_by_xpath(xpath="/html/body/div[7]/div[7]/table/tbody[1]/tr[11]/td[13]/a").click()
# element=WebDriverWait(drive,10,0.1).until(EC.visibility_of(drive.find_element_by_xpath(xpath="/html/body/div[7]/div[7]/table/tbody[1]/tr[3]/td[13]/a")))
# element.click()

# 点击账号登录
time.sleep(2)
drive.find_element_by_xpath(xpath="/html/body/div[31]/div[2]/ul/li[2]/a").click()

# 输入账号密码
# 输入账号
drive.find_element_by_xpath(xpath="//*[@id='J-userName']").click()
drive.find_element_by_xpath(xpath="//*[@id='J-userName']").send_keys(u'1234567')
# 输入密码
drive.find_element_by_xpath(xpath="//*[@id='J-password']").click()
drive.find_element_by_xpath(xpath="//*[@id='J-password']").send_keys(u'012345')

# 等待20S后点击登录，请手动点击验证码
time.sleep(20)
drive.find_element_by_xpath(xpath="//*[@id='J-login']").click()

time.sleep(3)

# 添加乘车人
# 0为选择第一个乘车人，1为选择第二个乘车人，以此类推
# 如果需要添加多个乘车人直接去掉对应代码的注释即可
drive.find_element_by_xpath(xpath="//*[@id='normalPassenger_0']").click()
# drive.find_element_by_xpath(xpath="//*[@id='normalPassenger_1']").click()
drive.find_element_by_xpath(xpath="//*[@id='normalPassenger_2']").click()
# drive.find_element_by_xpath(xpath="//*[@id='normalPassenger_3']").click()

#提交订单
drive.find_element_by_xpath(xpath="//*[@id='submitOrder_id']").click()
