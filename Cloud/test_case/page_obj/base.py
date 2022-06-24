from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import time
import datetime
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


# 基本层
class Base(object):

    def __init__(self, driver, base_url=''):
        self.driver = driver
        self.base_url = 'https://opensea.io/collection/perdidos-no-tempo'
        self.timeout = 90

    def _open(self, url):
        url_ = self.base_url + url
        # print(url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        # assert self.driver.current_url == url_, 'Did ont land on %s' % url_

    def open(self):
        self._open(self.url)

    # *参数个数不是固定的（By.ID, 'kw'）
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 寻找多个参数集合
    def find_elements(self, loc):
        return self.driver.find_elements(loc)

    # 下拉框选择
    def select_element(self, *loc):
        return Select(self.find_element(*loc))

    # 过去的时间
    def past_time(self):
        return str(datetime.datetime.now() - datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')

    # 未来的时间
    def later_time(self):
        return str(datetime.datetime.now() + datetime.timedelta(hours=0.0083333)).strftime('%Y-%m-%d %H:%M:%S')

    # 当天的日期
    def date_today(self):
        return str(datetime.date.today())

    # 当前时间
    def now_time(self):
        return str(time.strftime("%Y%m%d%H%I%S", time.localtime(time.time())))

    # 七天后的日期
    def date_endday(self):
        return str(datetime.date.today() + datetime.timedelta(days=7))

    # 三天后的日期
    def date_threeday(self):
        return str(datetime.date.today() + datetime.timedelta(days=3))

    def iframe(self, iframeid):
        return self.driver.switch_to.frame(iframeid)

    def iframe_out(self):
        return self.driver.switch_to.default_content()

    # 获取cookies值
    def get_cookies(self):
        return self.driver.get_cookies()

    # 判断元素是否存在返回True or False
    def is_element_exist(self, by, name):
        if by == 'NAME':
            s = self.driver.find_elements(By.NAME, name)
        elif by == 'XPATH':
            s = self.driver.find_elements(By.XPATH, name)
        elif by == 'LINK_TEXT':
            s = self.driver.find_elements(By.LINK_TEXT, name)
        elif by == 'CLASS_NAME':
            s = self.driver.find_elements(By.CLASS_NAME, name)
        else:
            pass
        if len(s) == 0:
            # print("元素未找到:%s" % name)
            return False
        else:
            # print("元素已找到:%s" % name)
            return True

    # 鼠标悬停操作
    def mouse_hover(self, by, elem):
        if by == 'XPATH':
            above = self.driver.find_element(By.XPATH, elem)
        elif by == 'NAME':
            above = self.driver.find_element(By.NAME, elem)
        else:
            pass
        ActionChains(self.driver).move_to_element(above).perform()

    # 元素显性等待点击 传driver和xpath
    def WaitElem(driver, xpath):
        WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()

    # 元素显性等待点击 传driver和css
    def WaitElement(driver, CSS_SELECTOR):
        WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR))).click()

    # 元素显性等待双击 传driver和xpath
    def WaitDblclickElem(driver, xpath):
        # ActionChains(driver).double_click(click).perform()
        WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located((By.XPATH, xpath))).double_click

    # 元素显性等待后输入 传driver、xpath和text
    def waitInputElem(driver, xpath, text):
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(text)

    # 元素显性等待显示 传driver、xpath
    def waitElemShow(driver, xpath):
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    # 元素显性等待显示返回文本 传driver、xpath
    def waitElemReturnText(driver, xpath):
        txt = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, xpath))).text
        return str(txt)

    # 窗口切换 传窗口编号 从0开始
    def switch_to_window(self, nums):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[nums])

    def switch_to_next_window(self):  # 关闭当前窗口并切换到下一个窗口
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.driver.current_window_handle:
                self.driver.close()
                self.driver.switch_to.window(handle)
