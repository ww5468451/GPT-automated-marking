from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
from exchangelib import Credentials, Account, Configuration, DELEGATE
import re
import time
import urllib.error
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib3
# ChatGpt账号:kyt1226@163.com
# ChatGpt密码:2787758kytwzj

# 1.先将ASIN页面的标题
# 2.将标题下面的body产品信息找出来
# 3.将五点描述爬取下来
# 4.将'//*[@id="aplus"]'里面的文本也爬取下来
# 5.由于chatgpt反爬虫和检测IP地址且检测VPN，故将chatgpt换成claude


chrome_options = webdriver.ChromeOptions()
# 使用headless浏览器模式，这样就可以在不打开浏览器的情况下模拟操作
# chrome_options.add_argument('--headless')
# 使用无头模式下缺少浏览器信息，或默认填充的浏览器信息带有爬虫痕迹，所以给其加上请求头
# chrome_options.add_argument('--incognito')# 添加无痕模式
prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
chrome_options.add_experimental_option("prefs", prefs)  # 禁止加载图片和CSS
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option('detach', True)#禁止浏览器在脚本结束后不会自动关闭
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-javascript") #禁用JavaScript
# chrome_options.add_argument('blink-settings=imagesEnabled=false')
# chrome_options.page_load_strategy = 'eager'
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(r'--user-data-dir=C:\Users\kyt\AppData\Local\Google\Chrome\User Data')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('window-size=1920x1080')# 页面动态加载的时候，无头模式默认size为0x0
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=chrome_options)
# chrome_options.add_argument('Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36')
# chrome_options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')

def get_outlook_code(method, account, password):
    credentials = Credentials(account, password)

    try:
        # 尝试使用自动发现功能创建 Account 对象
        account = Account(primary_smtp_address=account, credentials=credentials, autodiscover=True)
    except Exception as e:
        # 自动发现失败时，使用手动配置创建 Account 对象
        config = Configuration(server='outlook.office365.com', credentials=credentials)
        account = Account(primary_smtp_address=account, config=config, autodiscover=False, access_type=DELEGATE)
    try:
        for item in account.inbox.all().order_by('-datetime_received')[:1]:
            if method == 1:
                login_code = item.subject
                code = re.search(r'\d+', login_code).group()
                print(code)
                return code
            elif method == 2:
                login_code = item.text_body
                code = re.search(r'Your Poe verification code is:\s+(\d+)', login_code).group()
                code_ = re.search(r'\d+', code).group()
                print(code_)
                return code_
    except:
        pass



def main(url):
    print('该产品的url为：'+str(url))
    # url = "https://www.amazon.fr/dp/B000ZSW6EK"
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    m = 0
    title_text = ''
    while m < 5:
        try:
            title_text = driver.find_element(by=By.XPATH)
            # title_text = driver.find_element(by=By.ID, value='titleSection').text
            break
        except:
            time.sleep(20)
            driver.refresh()
            m = m + 1
    def have_product():
        try:
            see_more = driver.find_element(by=By.LINK_TEXT, value='See more')
            see_more.click()
        except:
            pass
        time.sleep(3.0)
        try:
            products = driver.find_element(by=By.ID, value='productOverview_feature_div').text
        except:
            products = ''
        # print(products)
        try:
            five_dec = driver.find_element(by=By.ID, value='feature-bullets').text
        except:
            five_dec = ''
        try:
            page_text = driver.find_element(by=By.ID, value="aplusBatch_feature_div").text
        except:
            page_text = ''

        # try:
        #     product_description = driver.find_element(by=By.ID, value='aplus_feature_div').text
        # except:
        #     product_description = ''

        try:
            product_detailed = driver.find_element(by=By.ID, value='detailBullets_feature_div').text
        except selenium.common.exceptions.NoSuchElementException:
            product_detailed = ''

        try:
            product_description = driver.find_element(by=By.ID, value='productDescription').text
        except selenium.common.exceptions.NoSuchElementException:
            product_description = ''

        try:
            product_detailed2 = driver.find_element(by=By.ID, value='productDetailsNonPets_feature_div').text
        except selenium.common.exceptions.NoSuchElementException:
            product_detailed2 = ''

        driver.quit()
        #如果有变体
        # products_description = title_text + '\n' + products + '\n' + five_dec + '\n' + page_text + '\n' + product_detailed + '\n' + 'Product Description:' +product_description + '\n' + product_detailed2 \
        #                        + '\n' + '请你回答我上述所有的信息中花盆架包含的主要材质(如层压板Laminated，复合木板等)有哪些，用不多于30个中文字符回答我，注意是花盆架，不是其他产品'
        # pyperclip.copy(products_description)
        # driver = webdriver.Chrome(options=chrome_options)
        # driver.get('https://chat12.aichatos.xyz/')
        # ## 登录ChatGpt
        # time.sleep(5.0)
        products_description = title_text + '\n' + products + '\n' + five_dec + '\n' + page_text + '\n' + product_detailed +'\n' + 'Product Description:' +product_description + '\n' + product_detailed2 \
                                + '请你回答我的问题，上述产品是给人用的不带床垫的提供了床脚和床板的一整张床架子或者床吗？材质可能是金属或者木头的，请你回答是或者否，如果没提到，就回答否即可，只用一个字回答'

        print(products_description)
        print('*****************************************************************************************************')
    if title_text != '':
        have_product()
    else:
        print('该ASIN在亚马逊上已不存在')
        driver.quit()




def get_url():
    ASIN0 = open('ASIN.txt', 'r+', encoding='utf-8')
    ASINS = ASIN0.readlines()
    urls = ['https://www.amazon.fr/dp/'+str(i).replace('\n', '') for i in ASINS]
    return urls
def get_claude_url(driver, account, password):
    # driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://claude.ai/login')
    time.sleep(5.0)
    while True:
        try:
            login_account = WebDriverWait(driver, 60, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]')))
            ActionChains(driver).move_to_element(login_account).perform()
            login_account.send_keys(account)
            submit_account = WebDriverWait(driver, 60, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/main/section/form/button')))
            ActionChains(driver).move_to_element(submit_account).perform()
            submit_account.click()
            time.sleep(30.0)
            code = get_outlook_code(1, account, password)
            time.sleep(5.0)
            if code != None:
                login_code = WebDriverWait(driver, 60, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="code"]')))
                ActionChains(driver).move_to_element(login_code).perform()
                login_code.send_keys(code)
                submit_login_code = WebDriverWait(driver, 60, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/main/section/form/button')))
                ActionChains(driver).move_to_element(submit_login_code).perform()
                submit_login_code.click()
                time.sleep(20.0)
                return True
            else:
                return False
        except selenium.common.exceptions.ElementNotInteractableException:
            driver.refresh()
        except selenium.common.exceptions.NoSuchElementException:
            driver.refresh()
        except selenium.common.exceptions.TimeoutException:
            driver.refresh()
        except TimeoutError:
            driver.refresh()
        except urllib.error.URLError:
            driver.refresh()
        except urllib3.exceptions.NewConnectionError:
            driver.refresh()
    # driver.quit()

def question_get_url_first(driver):
    # driver = webdriver.Chrome(options=chrome_options)
    while True:
        try:
            driver.get('https://claude.ai/login')
            time.sleep(5.0)
        # question_box = driver.find_element(by=By.XPATH, value='/html/body/main/div/div/fieldset/div[1]/div/div/div/p')
            question_box = WebDriverWait(driver, 60, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/fieldset/div[1]/div/div/div/p')))
            ActionChains(driver).move_to_element(question_box).perform()
            question_box.send_keys('你好，请你使用中文回答我下面的所有问题')
            question_box.send_keys(Keys.RETURN)
            time.sleep(6.0)
            real_url = driver.current_url
            return real_url
        except:
            driver.refresh()

def question_quit(driver, real_url):
    # driver = webdriver.Chrome(options=chrome_options)
    driver.get(real_url)
    time.sleep(3.0)
    while True:
        try:
            quit_account = WebDriverWait(driver, 60, 1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/button/img')))
            # quit_account = driver.find_element(by=By.XPATH, value='/html/body/div[2]/button/img')
            ActionChains(driver).move_to_element(quit_account).perform()
            quit_account.click()
            quit_account2 = WebDriverWait(driver, 60, 1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/button[2]/div')))
            # quit_account2 = driver.find_element(by=By.XPATH, value='/html/body/div[6]/button[2]/div')
            ActionChains(driver).move_to_element(quit_account2).perform()
            quit_account2.click()
            logout = WebDriverWait(driver, 60, 1).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Log out')))
            ActionChains(driver).move_to_element(logout).perform()
            logout.click()
            time.sleep(20.0)
            break
        except selenium.common.exceptions.ElementNotInteractableException:
            driver.refresh()
        except selenium.common.exceptions.NoSuchElementException:
            driver.refresh()
        except selenium.common.exceptions.TimeoutException:
            driver.refresh()
        except TimeoutError:
            driver.refresh()
        except urllib.error.URLError:
            driver.refresh()
        except urllib3.exceptions.NewConnectionError:
            driver.refresh()
    # driver.quit()

def delete_history_data():
    # 由于claude会记录浏览器的记录及访问次数，删除谷歌浏览器记录
    driver.get('chrome://settings/clearBrowserData')
    time.sleep(5.0)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 9)  # send right combination
    actions.perform()
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)  # confirm
    actions.perform()
    driver.close()
    # time.sleep(80)
def get_accounts_password_outlook():
    account_passwords = open('ACCOUNT.txt', 'r+', encoding='utf-8')
    line_raws = account_passwords.readlines()
    if len(line_raws) > 0:
        accounts = [line.split("$$")[0] for line in line_raws]
        passwords = [line.split("$$")[1].replace('\n', '') for line in line_raws]
        return accounts, passwords

# accounts, passwords = get_accounts_password_outlook()
# print(accounts)
# print(passwords)
urls = get_url()
# main(urls[20])
# def get_if_not_chance():
#     # 写一个函数关于账号是否还有次数，有次数则继续，没有则换一个账号
#
#     return False
# '/html/body/div[4]/div/div[5]/div/fieldset/div/div/div[2]/a'
#
# 'Get notified about paid plans'  link_text
#     return True
def Poe_AI(method, account, password):
    driver.get('https://poe.com/login')
    time.sleep(30.0)
    # 在这需要设立一个机制去将鼠标移动到某个位置，普通的那种selenium点击某个元素已经不行了，使用pyautogui操控鼠标去弄
    try:
        element = driver.find_element(By.CLASS_NAME, "ctp-label")
        element.click()
    except:
        pass
    account_login = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div/div[2]/form/input')
    account_login.send_keys('kyt1226@163.com')
    time.sleep(5.0)
    go = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div/button[1]')
    go.click()
    time.sleep(7.0)
    code = get_outlook_code(method, account, password)
    login_code = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div[3]/form/input')
    login_code.send_keys(code)
    time.sleep(5.0)
    submit_code = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/button[2]')
    submit_code.click()
    time.sleep(7.0)

