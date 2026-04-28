import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import selenium
import re
import pyperclip
import urllib.error

chrome_options = webdriver.ChromeOptions()
# 使用headless浏览器模式，这样就可以在不打开浏览器的情况下模拟操作
# chrome_options.add_argument('--headless')
# 使用无头模式下缺少浏览器信息，或默认填充的浏览器信息带有爬虫痕迹，所以给其加上请求头
prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
chrome_options.add_experimental_option("prefs", prefs)  # 禁止加载图片和CSS
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-javascript") #禁用JavaScript
# chrome_options.add_argument('blink-settings=imagesEnabled=false')
# chrome_options.page_load_strategy = 'eager'
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('window-size=1920x1080')# 页面动态加载的时候，无头模式默认size为0x0
chrome_options.add_argument('--start-maximized')
# chrome_options.add_argument('Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36')

driver1 = webdriver.Chrome(options=chrome_options)
def main(url):
    print('该产品的url为：' + str(url))
    # url = "https://www.amazon.fr/dp/B000ZSW6EK"
    try:
        driver1.get(url)
    except:
        time.sleep(2.0)
        driver1.refresh()
        driver1.get(url)
    m = 0
    title_text = ''
    while m < 2:
        try:
            title_text = driver1.find_element(by=By.ID, value='titleSection').text
            break
        except:
            time.sleep(20)
            driver1.refresh()
            m = m + 1

    def have_Q_A():
        time.sleep(15.0)
        target_element = driver1.find_element(by=By.XPATH, value='//*[@id="cm_cr_dp_d_rating_histogram"]/div[1]/h2')
        driver1.execute_script("arguments[0].scrollIntoView();", target_element)
        time.sleep(5.0)
        search_Q_A = driver1.find_element(by=By.XPATH, value='//*[@id="ask-btf-container"]/div/div/div[1]/span/span/span/span/span/span/div/form/span/span/div/div/div/input')
        time.sleep(1.0)
        search_Q_A.send_keys('Q')
        time.sleep(2.5)
        customer = driver1.find_element(by=By.XPATH, value='//*[@id="ask-btf-container"]/div/div/div[1]/span/span/span/span/span/span/div/form/div[2]/div[2]/span[5]/span/span')
        customer.click()
        time.sleep(10.0)
        question = driver1.find_element(by=By.XPATH, value='//*[@id="ask-btf-container"]/div/div/div[1]/span/span/span/span/span/span/div/form/div[2]/div[3]/div/div[6]')
        texts_ask = question.find_elements(by=By.CLASS_NAME, value='a-declarative')
        text_ask = ""
        for texts0 in texts_ask:
            texts = texts0.text
            # print(texts)
            text_ask = str(texts) + "#" + text_ask

        print(text_ask)
        return text_ask


    if title_text != '':
        random_num = round(random.uniform(8, 10), 2)
        time.sleep(random_num)
        title = driver1.find_element(by=By.ID, value='titleSection')
        title.click()
        text = have_Q_A()
        return text
    else:
        print('该ASIN在亚马逊上已不存在')
        return ''

def get_url():
    ASIN0 = open('ASIN.txt', 'r+', encoding='utf-8')
    ASINS = ASIN0.readlines()
    urls = ['https://www.amazon.com/dp/'+str(i).replace('\n', '') for i in ASINS]
    return urls

if __name__ == '__main__':
    urls = get_url()
    m = 1
    # 必须要搞一个10次左右就重新发起一个对话，不然就卡住动不了了，刷新也没有用
    for url in urls:
        ASIN = url.split('/')[-1]
        print(ASIN)
        print('*******************************************这是第' + str(
            m) + '个产品************************************************')
        text = main(url)
        # print(text)
        random_num = round(random.uniform(2, 3), 2)
        time.sleep(random_num)
        if text != '':
            asin_product = open('ASIN_Products.txt', 'a+', encoding='utf-8')
            try:
                print(ASIN + "#" + text)
                asin_product.write(ASIN + '#' + text + '\n')
                random_num = round(random.uniform(5, 12), 2)
                time.sleep(random_num)
                asin_product.close()
            except TypeError:
                pass
        else:
            pass
            # 在此处写一个函数关于收集亚马逊上不存在的ASIN
        m = m + 1
    driver1.quit()
    # time.sleep(30000)
