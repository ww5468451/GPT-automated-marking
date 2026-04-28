from selenium import webdriver
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options as EdgeOption
import time
from selenium.webdriver.common.by import By


# 设定edge浏览器参数
edge_options = EdgeOption()
edge_options.add_experimental_option('detach', True)#禁止浏览器在脚本结束后自动关闭
edge_options.add_experimental_option("excludeSwitches", ['enable-automation'])#禁止出现自动检测提示标志
edge_options.add_experimental_option('useAutomationExtension', False)#关闭Edge浏览器中的自动化扩展
edge_options.add_argument("--disable-blink-features=AutomationControlled")#禁用Blink引擎中的自动化检测功能
edge_options.add_argument("disable-infobars")#移除地址栏中的提示信息栏
edge_options.add_argument(r'--user-data-dir=C:\Users\kyt\AppData\Local\Microsoft\Edge\User Data1')
# edge_options.add_argument('--profile-directory=Default')
# edge_options.add_argument('--disable-gpu')
edge_options.add_argument('window-size=1920x1080')# 页面动态加载的时候，无头模式默认size为0x0
edge_options.add_argument('--start-maximized')
driver = Edge(options=edge_options)
#跳转到outlook邮箱登录页面
driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=15&ct=1691638652&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26RpsCsrfState%3d320b1ff0-5513-2047-f9bf-9cf9085ee7e9&id=292841&aadredir=1&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c')

login_account = driver.find_element(by=By.XPATH, value='//*[@id="i0116"]')
login_account.send_keys('weilelechanpin@outlook.com')
submit_login_account = driver.find_element(by=By.XPATH, value='//*[@id="idSIButton9"]')
submit_login_account.click()
time.sleep(5.0)

password = driver.find_element(by=By.XPATH, value='//*[@id="i0118"]')
password.send_keys('Wll1128~')
submit_password = driver.find_element(by=By.XPATH, value='//*[@id="idSIButton9"]')
submit_password.click()
time.sleep(20.0)
driver.switch_to.default_content()
# while True:
#     try:
#         login_code_file = driver.find_element(by=By.CSS_SELECTOR, value='//*[@id="MainModule"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/i[2]')
#         login_code_file.click()
#     except:
#         driver.refresh()
#         time.sleep(10.0)