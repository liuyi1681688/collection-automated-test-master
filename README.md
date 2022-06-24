# 设计思路
UI自动化测试框架基于python-selenium-unittest-HTMLTestRunner

互联网公司更新迭代比较快，版本发布频率较高，在每次上线之前要做一次整体的回归测试，所以留给测试人员的时间并没有很多，
实施UI自动化测试，构建到jenkins上进行周期的运行，提测后，或者上线前都会进行运行测试，保障每一次更新迭代功能不受影响。

框架主要使用了page_object模式，对每个页面进行封装，需要操作时直接调用封装的方法，这样做的好处是如果页面发生变化，不需要
去调整用例，只需要对封装的页面进行调整。


安装说明如下：
 
### **安装python**

下载地址如下:

https://www.python.org/downloads/release/python-365/

安装时记得勾选Add Python 3.6 to PATH

### **下载selenium第三方包**

cmd命令行输入如下：

Pip install selenium

Pip install requests

或

进入到程序根目录运行:

pip install -r requirements.txt



### **配置文件**

把driver目录下的浏览器驱动文件chromedriver文件和报表插件HTMLTestRunner_PY3.py放置在指定目录

chromedriver复制到chrome目录和path下，如C:\Program Files (x86)\Google\Chrome\Application

chromedriver复制到python目录和path下，如D:\software\python36

HTMLTestRunner_PY3.py复制到python目录lib下，如C:\Python36\Lib



### **测试结果展示**
HTML报告日志 
HTML报告点击截图，弹出截图 
测试报告通过的日志 
自动截图存放指定的目录 
邮件测试报告 








