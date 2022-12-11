# _*_ coding : utf-8 _*_
# @Time: 2022/12/10 2:23 PM
# @Author : 张安然
# @File : '031_selenium_基本使用
# @Project : python_space

# 导入selenium
from selenium import webdriver

# 导入浏览器驱动
# https://blog.csdn.net/Student_mn/article/details/123502866 参考授权
# https://chromedriver.storage.googleapis.com/index.html
# https://blog.csdn.net/u010217055/article/details/127192388 驱动安装
browser = webdriver.Chrome()

# 访问网站
url = 'https://www.jd.com/'
# 最新版selenium 会有闪退
# 解决方法 pip3 install selenium==3.141.0 ,参考地址 https://blog.csdn.net/m0_75245302/article/details/128107950
browser.get(url)
content = browser.page_source
print(content)