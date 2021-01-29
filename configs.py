"""
request selenium配置
"""
from requestium import Session
from os.path import realpath
'''
chrome 和 edge 浏览器的selenium driver 下载地址
chrome: https://npm.taobao.org/mirrors/chromedriver
edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
'''
# 网址
pwd = realpath('.')
base_path = pwd.replace("\\", "/")
# print(base_path)
# 本地driver文件的绝对路径
driver_path = base_path + '/pku_law_selenium/drivers/88.4324_chromedriver.exe'
# 数据保存在本地的文件夹路径
data_path = base_path + '/dataset'

# driver实例化配置
s = Session(webdriver_path=driver_path,  # driver文件路径
            browser='chrome',  # 选择浏览器(暂时只支持chrome和phantomjs)
            webdriver_options={'arguments': ['--no-sandbox'],  # , 'headless','--disable-gpu'
                               'profile.default_content_settings.popups': 0,
                               'download.default_directory': data_path},  # 可以选择配置无头浏览器,禁止弹出下载窗口,默认下载路径
            default_timeout=9)  # 设置等待超时时间，单位s

"""
语料配置
"""