from time import sleep
import sys
import random
import string
import unittest
from Cloud.test_case.models import function, myunit
from Cloud.test_case.page_obj.collectible_page import CollectiblePage
from Cloud.test_case.page_obj.base import Base
from selenium.webdriver.support import expected_conditions as EC

sys.path.append('./models')
sys.path.append('./page_obj')

class CollectionTest(myunit.MyTest):
    """收藏品测试"""

    ##################################
    #  Test Case
    ##################################

    # @unittest.skip("跳过用例")
    def test001_view_collectibles_success(self):
        """001_查看收藏品成功"""
        # 实例化收藏品页面
        po = CollectiblePage(self.driver)
        po.open()
        #打开OpenSea网址后，捕获并处理异常情况
        try:
            sleep(2)
            # 等待收藏品加载出现后点击收藏品
            po.view_collectibles()
            function.insert_img(self.driver, '%s.png' % po.now_time())
            self.add_img()
            #打开成功后，验证收藏品信息文本是否显示在页面'
            if Base.is_element_exist(self, 'XPATH', po.explore_collections_xpath):
                # 判断收藏品页面显示是否正确
                self.assertEqual(po.view_collectibles_success_return_title(), 'Explore Collections | OpenSea')
            else:
                print('查看失败，请排查问题！')
        except:
            print("环境崩溃或网络异常，请排查问题！")

    # @unittest.skip("跳过用例")
    def test002_refreshing_metadata(self):
        '''002_刷新元数据'''
        # 实例化收藏品页面
        po = CollectiblePage(self.driver)
        time.sleep(2)
        # 点击右上角刷新元数据按钮
        Base.WaitElem(po.driver, po.refresh_metadata_button_xpath)
        # 等待刷新完成, 验证我们对更新的条目进行了排队
        self.assertEqual(procurementBudgetIndex.getRefreshMetadataTipTxt()=="We've queued this item for an update! Check back in a minute...", True)
        time.sleep(2)
        # 添加时间截图
        self.screenshot_and_close_current_window()

