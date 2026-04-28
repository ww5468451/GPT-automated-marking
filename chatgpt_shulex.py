from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import selenium
import pyperclip

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
chrome_options.add_argument(r'--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data2')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('window-size=1920x1080')# 页面动态加载的时候，无头模式默认size为0x0
chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=chrome_options)

chrome_options2 = webdriver.ChromeOptions()
# 使用headless浏览器模式，这样就可以在不打开浏览器的情况下模拟操作
# chrome_options.add_argument('--headless')
# 使用无头模式下缺少浏览器信息，或默认填充的浏览器信息带有爬虫痕迹，所以给其加上请求头
prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
chrome_options2.add_experimental_option("prefs", prefs)  # 禁止加载图片和CSS
chrome_options2.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options2.add_experimental_option('detach', True)
chrome_options2.add_experimental_option('useAutomationExtension', False)
chrome_options2.add_argument("--disable-javascript") #禁用JavaScript
# chrome_options.add_argument('blink-settings=imagesEnabled=false')
# chrome_options.page_load_strategy = 'eager'
chrome_options2.add_argument("--disable-blink-features=AutomationControlled")
chrome_options2.add_argument(r'--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data3')
chrome_options2.add_argument('--profile-directory=Default')
chrome_options2.add_argument('--disable-gpu')
chrome_options2.add_argument('window-size=1920x1080')# 页面动态加载的时候，无头模式默认size为0x0
chrome_options2.add_argument('--start-maximized')



driver.get('https://apps.voc.ai/account/?#/cnLoginOfficial?activeKey=password&lang=zh-CN')
driver1 = webdriver.Chrome(options=chrome_options2)

time.sleep(10.0)
try:
    account = driver.find_element(by=By.XPATH, value='//*[@id="contact"]')
    account.send_keys('xulei@angniugroup.com')
    password = driver.find_element(by=By.XPATH, value='//*[@id="code"]')
    password.send_keys('ANGNIU001')
    login = driver.find_element(by=By.XPATH, value='//*[@id="entry"]/div/div/div[1]/div[2]/div[1]/div/div[1]/main/form/div[4]/div/div/div/div/button')
    login.click()
except:
    pass
time.sleep(10.0)
driver.get('https://www.voc.ai/cn/chatgpt-free')
time.sleep(10.0)

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
    while m < 5:
        try:
            title_text = driver1.find_element(by=By.ID, value='titleSection').text
            break
        except:
            time.sleep(20)
            driver1.refresh()
            m = m + 1

    def have_product():
        try:
            see_more = driver1.find_element(by=By.LINK_TEXT, value='See more')
            see_more.click()
        except:
            pass
        try:
            see = driver1.find_element(by=By.XPATH, value='//*[@id="feature-bullets"]/div/a/i')
            see.click()
        except:
            pass
        time.sleep(3.0)
        try:
            products = driver1.find_element(by=By.ID, value='productOverview_feature_div').text
        except:
            products = ''
        # print(products)
        try:
            five_dec = driver1.find_element(by=By.ID, value='featurebullets_feature_div').text
        except:
            five_dec = ''

        try:
            page = driver1.find_element(by=By.ID, value="aplusBatch_feature_div")
            tbody = page.find_element(by=By.TAG_NAME, value="tbody")
            driver1.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", tbody)
            page_text = page.get_attribute("innerText")
        except:
            page_text = ''

        # try:
        #     product_description = driver.find_element(by=By.ID, value='aplus_feature_div').text
        # except:
        #     product_description = ''

        try:
            product_detailed = driver1.find_element(by=By.ID, value='detailBullets_feature_div').text
        except selenium.common.exceptions.NoSuchElementException:
            product_detailed = ''

        try:
            product_description = driver1.find_element(by=By.ID, value='productDescription').text
        except selenium.common.exceptions.NoSuchElementException:
            product_description = ''

        try:
            product_detailed2 = driver1.find_element(by=By.ID, value='productDetailsNonPets_feature_div').text
        except selenium.common.exceptions.NoSuchElementException:
            product_detailed2 = ''

        # 如果有变体
        # products_description = title_text + '\n' + products + '\n' + five_dec + '\n' + page_text + '\n' + product_detailed + '\n' + 'Product Description:' +product_description + '\n' + product_detailed2 \
        #                        + '\n' + '请你回答我上述所有的信息中花盆架包含的主要材质(如层压板Laminated，复合木板等)有哪些，用不多于30个中文字符回答我，注意是花盆架，不是其他产品'
        # pyperclip.copy(products_description)
        # driver = webdriver.Chrome(options=chrome_options)
        # driver.get('https://chat12.aichatos.xyz/')
        # ## 登录ChatGpt
        # time.sleep(5.0)
        products_description = '该产品的桌面的长和宽是多少，桌面的桌板是否为拼接的，电机的数量是多少，请你必须按以下的形式:长x宽##是##1，使用中文回答我'+title_text + '\n' + five_dec + '\n' + 'Product Description:' + product_description + '\n'+ product_detailed2
        print(products_description)
        print('*****************************************************************************************************')
        return products_description
    if title_text != '':
        text = have_product()
        return text
    else:
        print('该ASIN在亚马逊上已不存在')
        return ''

def get_url():
    ASIN0 = open('ASIN.txt', 'r+', encoding='utf-8')
    ASINS = ASIN0.readlines()
    urls = ['https://www.amazon.de/dp/'+str(i).replace('\n', '') for i in ASINS]
    return urls
j = 1
m = 1
urls = get_url()
for url in urls:
    ASIN = url.split('/')[-1]
    print(ASIN)
    print('*******************************************这是第' + str(m) + '个产品************************************************')
    text = main(url)
    random_num = round(random.uniform(8, 10), 2)
    time.sleep(random_num)
    if text != '':
        asin_product = open('ASIN_Products.txt', 'a+', encoding='utf-8')
        ask_question = driver.find_element(by=By.XPATH,
                                           value='//*[@id="rc-tabs-0-panel-chat"]/div/div[2]/div[2]/span/textarea')
        pyperclip.copy(text)
        ask_question.send_keys(Keys.CONTROL, 'v')
        ask_question.send_keys(Keys.RETURN)
        time.sleep(15.0)
        answer = driver.find_element(by=By.XPATH,
                                     value=f'//*[@id="rc-tabs-0-panel-chat"]/div/div[1]/div[3]/div[{2 * j}]/div/span').text
        print(answer)
        asin_product.write(ASIN + '##' + answer + '\n')
        asin_product.close()
        j = j + 1
    m = m + 1

