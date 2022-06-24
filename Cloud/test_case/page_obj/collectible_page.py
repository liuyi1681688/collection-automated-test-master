from selenium.webdriver.common.by import By
from .base import Base
import time


class CollectiblePage(Base):
    url = '/'
    explore_collections_xpath = '//*[@id="main"]/div/div[1]/h1'  # 收藏品页面
    explore_collections_loc = (By.XPATH, explore_collections_xpath)

    view_collectibles_xpath = (By.XPATH, '//img[@alt="Herói das pistas"]')  #查看收藏品
    view_collectibles_loc = (By.XPATH, view_collectibles_xpath)

    refresh_metadata_button_xpath = '//div[2]/section/div/div[2]/div/button'  #刷新元数据按钮
    refresh_metadata_button_loc = (By.XPATH, refresh_metadata_button_xpath)

    refresh_metadata_tip_xpath = '//div[2]/div/div'  #刷新元数据提示
    refresh_metadata_tip_loc = (By.XPATH, refresh_metadata_tip_xpath)


    # 把每一个元素封装成一个方法

    # 查看收藏品
    def view_collectibles(self):
        self.find_element(*self.view_collectibles_loc).click()

    # 返回打开收藏品页面后的title
    def view_collectibles_success_return_title(self):
        return self.driver.title

    # 获取刷新元数据提示文本
    def getRefreshMetadataTipTxt(self):
        txt = self.find_element(*self.refresh_metadata_tip_loc).text
        return str(txt)

