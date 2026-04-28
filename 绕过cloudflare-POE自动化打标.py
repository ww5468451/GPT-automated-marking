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
chrome_options.add_argument(r'--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data2')
chrome_options.add_argument(r'--profile-directory=Default')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('window-size=1920x1080')# 页面动态加载的时候，无头模式默认size为0x0
chrome_options.add_argument('--start-maximized')
# chrome_options.add_argument('Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36')

driver1 = webdriver.Chrome(options=chrome_options)

def poe_login():
    driver.get('https://poe.com/login')
    google_login = WebDriverWait(driver, 60, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/button[3]')))
    ActionChains(driver).move_to_element(google_login).perform()
    google_login.click()
    time.sleep(20)
    google_account = WebDriverWait(driver, 60, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
    ActionChains(driver).move_to_element(google_account).perform()
    google_account.click()
    google_account.send_keys('ke799419@gmail.com')
    next_ = WebDriverWait(driver, 60, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button/span')))
    ActionChains(driver).move_to_element(next_).perform()
    driver.execute_script("arguments[0].click();", next_)
    random_num = round(random.uniform(5, 10), 2)
    time.sleep(random_num)
    passwords = WebDriverWait(driver, 60, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    ActionChains(driver).move_to_element(passwords).perform()
    passwords.click()
    passwords.send_keys('2787758Kyt#')
    next_2 = WebDriverWait(driver, 30, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/span')))
    ActionChains(driver).move_to_element(next_2).perform()
    driver.execute_script("arguments[0].click();", next_2)
    while True:
        try:
            Your_bots = WebDriverWait(driver, 30, 1).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'ChatPageBotSwitcher_navigationIcon__XYT52')))
            ActionChains(driver).move_to_element(Your_bots).perform()
            driver.execute_script("arguments[0].click();", Your_bots)
            random_num = round(random.uniform(8, 10), 2)
            time.sleep(random_num)
            claude_instant = WebDriverWait(driver, 60, 1).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Claude-instant')))
            ActionChains(driver).move_to_element(claude_instant).perform()
            driver.execute_script("arguments[0].click();", claude_instant)
            break
        except:
            random_num = round(random.uniform(8, 10), 2)
            time.sleep(random_num)
            driver.refresh()
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
        products_description = '该产品的桌面的长和宽是多少，桌面的桌板是否为拼接的，电机的数量是多少，请你必须按以下的形式:长x宽##是##1，使用中文回答我' + title_text + '\n' + products + '\n' + five_dec + '\n' + page_text + '\n' + product_detailed + '\n' + 'Product Description:' + product_description + '\n' + product_detailed2 \

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


def get_answer(text, n, ASIN):
    random_num = round(random.uniform(2, 5), 2)
    time.sleep(random_num)
    ask_question = WebDriverWait(driver, 30, 1).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div[1]/div/main/div/div/div/footer/div/div/div[1]/textarea')))
    ActionChains(driver).move_to_element(ask_question).perform()
    ask_question.click()
    pyperclip.copy(text)
    ask_question.send_keys(Keys.CONTROL, 'v')
    ask_question.send_keys(Keys.RETURN)
    h = 0
    while h < 3:
        try:
            random_num = round(random.uniform(30, 35), 2)
            time.sleep(random_num)
            answers = driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/div[{n}]/div[2]/div[2]/div[2]/div/div[1]/div/div/p')
            answers_text = answers.text
            if answers_text == '...' or '':
                print('还在加载回答......')
                random_num = round(random.uniform(2, 5), 2)
                time.sleep(random_num)
                driver.refresh()
            else:
                print('————————————————————————————————-已经加载出回答了————————————————————————————————————————')
                print(ASIN + "##" + answers_text)
                asin_product.write(ASIN + '##' + answers_text + '\n')
                break
        except:
            random_num = round(random.uniform(2, 5), 2)
            time.sleep(random_num)
        h = h + 1


def new_chat():
    # 由于claude会记录浏览器的记录及访问次数，删除谷歌浏览器记录，这样能减少缓存文件，不至于让后面卡住无法输入问题
    while True:
        try:
            Your_bots = WebDriverWait(driver, 30, 1).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'ChatPageBotSwitcher_navigationIcon__XYT52')))
            ActionChains(driver).move_to_element(Your_bots).perform()
            driver.execute_script("arguments[0].click();", Your_bots)
            random_num = round(random.uniform(8, 10), 2)
            time.sleep(random_num)
            claude_instant = WebDriverWait(driver, 60, 1).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Claude-instant')))
            ActionChains(driver).move_to_element(claude_instant).perform()
            driver.execute_script("arguments[0].click();", claude_instant)
            break
        except:
            random_num = round(random.uniform(8, 10), 2)
            time.sleep(random_num)
            driver.refresh()


if __name__ == '__main__':
    uc.TARGET_VERSION = 122
    options = uc.ChromeOptions()
    options.add_argument("--incognito")
    prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
    options.add_experimental_option("prefs", prefs)
    driver = uc.Chrome(options=options)
    poe_login()
    urls = get_url()
    m = 1
    n = 3
    i = 1
    chat_r = 0
    # 必须要搞一个10次左右就重新发起一个对话，不然就卡住动不了了，刷新也没有用
    for url in urls:
        ASIN = url.split('/')[-1]
        print(ASIN)
        print('*******************************************这是第' + str(
            m) + '个产品************************************************')
        text = main(url)
        random_num = round(random.uniform(8, 10), 2)
        time.sleep(random_num)
        if chat_r < 10:
            if text != '':
                asin_product = open('ASIN_Products.txt', 'a+', encoding='utf-8')
                get_answer(text, n, ASIN)
                asin_product.close()
                n = n + 1
            else:
                pass
            chat_r = chat_r + 1
        else:
            chat_r = 0
            random_num = round(random.uniform(10, 15), 2)
            time.sleep(random_num)
            new_chat()
            n = 3
            if text != '':
                asin_product = open('ASIN_Products.txt', 'a+', encoding='utf-8')
                random_num = round(random.uniform(5, 12), 2)
                time.sleep(random_num)
                get_answer(text, n, ASIN)
                asin_product.close()
                n = n + 1
            else:
                pass
            # 在此处写一个函数关于收集亚马逊上不存在的ASIN
        m = m + 1
    driver1.quit()
    # time.sleep(30000)
