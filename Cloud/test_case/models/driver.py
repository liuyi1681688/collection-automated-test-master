from selenium.webdriver import Remote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 启动浏览器驱动
def browser(name):
    # driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    options = Options()
    # 设置为无界面启动
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # driver = webdriver.Chrome(executable_path="/usr/sbin/chromedriver",
    #                           chrome_options=options)
    try:
        if name == "firefox" or name == "Firefox" or name == "ff":
            # pycharm 安装selenium, 默认安装了3.14的版本。本机Firefox的版本为最新（68），且安装了geckodriver v0.24.0（Firefox的驱动包，使用selenium需要的）。
            print("start browser name :Firefox")
            driver = webdriver.Firefox()
            return driver
        elif name == "chrome" or name == "Chrome":
            print("start browser name :Chrome")
            # driver = webdriver.Chrome(executable_path="/usr/sbin/chromedriver", chrome_options=options)
            driver = webdriver.Chrome()
            return driver
        elif name == "ie" or name == "Ie":
            print("start browser name :Ie")
            driver = webdriver.Ie()
            return driver
        elif name == "phantomjs" or name == "Phantomjs":
            print("start browser name :phantomjs")
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("Not found this browser,You can use 'firefox', 'chrome', 'ie' or 'phantomjs'")
    except Exception as msg:
        print("启动浏览器出现异常：%s" % str(msg))
    '''
    #可以启动到远程主机中，运行自动化测试
    host = '127.0.0.1:4444' #运行主机：端口号（本机默认：127.0.0.1:4444）
    dc = {'browserName': 'chrome'}  #指定浏览器
    driver = Remote(command_execute='http://' + host + '/wd/hub',
                    desired_capabilities=dc)
    '''


# '''
#用于测试该脚本是否有效
# if __name__ == '__main__':
#     dr = browser('Firefox')
# '''
