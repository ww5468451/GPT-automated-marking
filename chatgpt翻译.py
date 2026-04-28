import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
import pyperclip
import openpyxl

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
    google_account.send_keys('krystalwyq0521@gmail.com')
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
    passwords.send_keys('iambking!')
    next_2 = WebDriverWait(driver, 30, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/span')))
    ActionChains(driver).move_to_element(next_2).perform()
    driver.execute_script("arguments[0].click();", next_2)
    while True:
        try:
            Your_bots = WebDriverWait(driver, 30, 1).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/aside/div/div/menu/section[2]/li/a/div[2]')))
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
    # time.sleep(5000.0)

def get_answer(text, n, ASIN):
    random_num = round(random.uniform(2, 5), 2)
    time.sleep(random_num)
    ask_question = WebDriverWait(driver, 30, 1).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div/div/div/div/footer/div/div/div[1]/textarea')))
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
            answers = driver.find_element(by=By.XPATH, value=f'//*[@id="__next"]/div[1]/div[2]/main/div/div/div/div/div[2]/div[{n}]/div[2]/div[2]/div[2]/div/div[1]/div/div')
            answers_text = answers.text
            if answers_text == '...' or '':
                print('还在加载回答......')
                random_num = round(random.uniform(2, 5), 2)
                time.sleep(random_num)
                driver.refresh()
            else:
                print('————————————————————————————————-已经加载出回答了————————————————————————————————————————')
                print(ASIN + "#" + answers_text)
                ws.append([ASIN, answers_text])
                wb.save(file_name)
                asin_product.write(ASIN + '#' + answers_text + '\n')
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
                EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/aside/div/div/menu/section[2]/li/a/div[2]')))
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
    df = pd.read_excel(r'D:\Personal\Downloads\20231117VOC 分析.xlsx')
    file_name = '翻译.xlsx'
    try:
        # 尝试打开文件，如果文件已存在则附加到现有文件中
        wb = openpyxl.load_workbook(file_name)
        ws = wb.active
    except FileNotFoundError:
        # 如果文件不存在则创建一个新文件，并添加一个工作表
        wb = openpyxl.Workbook()
        ws = wb.active
    m = 1
    ws.append(['ASIN', '翻译内容'])
    wb.save(file_name)
    # 必须要搞一个10次左右就重新发起一个对话，不然就卡住动不了了，刷新也没有用
    print(df)
    options = uc.ChromeOptions()
    options.add_argument("--incognito")
    prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
    options.add_experimental_option("prefs", prefs)
    driver = uc.Chrome(options=options)
    poe_login()
    n = 3
    i = 1
    chat_r = 0
    # 必须要搞一个10次左右就重新发起一个对话，不然就卡住动不了了，刷新也没有用
    random_num = round(random.uniform(8, 10), 2)
    time.sleep(random_num)
    for index, row in df.iterrows():
        print("********************************************这是第"+str(m)+"个"+"对话****************************************************")
        text = row['Content']+"请你将这段话翻译成中文，不用回答别的"
        ASIN = row['Asin']
        if chat_r < 10:
            asin_product = open('ASIN_Products0.txt', 'a+', encoding='utf-8')
            get_answer(text, n, ASIN)
            asin_product.close()
            n = n + 1
            chat_r = chat_r + 1
        else:
            chat_r = 0
            random_num = round(random.uniform(10, 15), 2)
            time.sleep(random_num)
            new_chat()
            n = 3
            asin_product = open('ASIN_Products0.txt', 'a+', encoding='utf-8')
            random_num = round(random.uniform(5, 12), 2)
            time.sleep(random_num)
            get_answer(text, n, ASIN)
            asin_product.close()
            n = n + 1
        m = m + 1


    # time.sleep(30000)
