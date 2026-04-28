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
# prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
# chrome_options.add_experimental_option("prefs", prefs)  # 禁止加载图片和CSS
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-javascript")  # 禁用JavaScript
# chrome_options.add_argument('blink-settings=imagesEnabled=false')
# chrome_options.page_load_strategy = 'eager'
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(r'--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data5')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('window-size=1920x1080')  # 页面动态加载的时候，无头模式默认size为0x0
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
    time.sleep(8.0)
    while m < 2:
        try:
            title_text = driver1.find_element(by=By.ID, value='titleSection').text
            break
        except:
            time.sleep(20)
            driver1.refresh()
            m = m + 1
    try:
        price = driver1.find_element(by=By.ID, value='corePriceDisplay_desktop_feature_div').find_element(by=By.CLASS_NAME, value='a-price').text.replace('\n', '.').replace('SAR', '')
    except:
        price = " "
    def have_product():
        try:
            time.sleep(3.0)
            see_more = driver1.find_element(by=By.LINK_TEXT, value='See more')
            see_more.click()
        except:
            pass
        time.sleep(3.0)
        try:
            close_ = driver1.find_element(by=By.XPATH, value='//*[@id="a-popover-2"]/div/header/button')
            close_.click()
        except:
            pass
        time.sleep(3.0)

        try:
            time.sleep(2.0)
            shuoming = driver1.find_element(by=By.ID, value='glance_icons_div').text
        except:
            shuoming = ''

        try:
            products = driver1.find_element(by=By.ID, value='productOverview_feature_div').text
        except:
            products = ''
        # print(products)
        try:
            five_dec = driver1.find_element(by=By.ID, value='feature-bullets').text
        except:
            five_dec = ''
        # try:
        #     page_text = driver1.find_element(by=By.ID, value="aplusBatch_feature_div").text
        # except:
        #     page_text = ''
        try:
            expan = driver1.find_element(by=By.XPATH, value='//*[@id="voyager-expand-all-btn"]')
            expan.click()
        except:
            pass

        # try:
        #     product_description_ = driver1.find_element(by=By.ID, value='aplus_feature_div').text
        # except:
        #     product_description_ = ''
        #
        # try:
        #     product_detailed = driver1.find_element(by=By.ID, value='detailBullets_feature_div').text
        # except selenium.common.exceptions.NoSuchElementException:
        #     product_detailed = ''

        time.sleep(5.0)
        try:
            product_description = driver1.find_element(by=By.ID, value='prodDetails').text
        except selenium.common.exceptions.NoSuchElementException:
            product_description = ''

        # try:
        #     product_detailed2 = driver1.find_element(by=By.ID, value='productDetailsNonPets_feature_div').text
        # except selenium.common.exceptions.NoSuchElementException:
        #     product_detailed2 = ''

        # products_description = shuoming+products+five_dec+page_text+product_detailed+product_description+product_detailed2
        #
        # products_description = shuoming+products+five_dec+page_text+product_description
        product_descriptions = products + five_dec + product_description
        print(product_descriptions)
        if product_descriptions != '':
            # if 'motion sensor light' in product_description.lower() or 'motion' in product_description.lower() or 'sensor' in product_description.lower():
            #     sport_light = '带运动传感灯'
            # else:
            #     sport_light = '不带运动传感灯'

            # if "wall mount" in product_descriptions.lower():
            #     install_method = '壁挂式'
            #
            # elif "recessed or surface" in product_descriptions.lower():
            #     install_method = '壁挂式/嵌入式'
            #
            # elif "recessed" in product_descriptions.lower():
            #     install_method = '嵌入式'
            # else:
            #     install_method = '标题无提及'

            # if 'mirror' in product_description.lower() or 'mirrored' in product_description.lower():
            #     mirror = '带镜子'
            # else:
            #     mirror = '不带镜子'
            #
            # if 'wireless' in product_description.lower() or 'remote' in product_description.lower():
            #     remote = '有无线遥控功能'
            # else:
            #     remote = '没有无线遥控功能'
            #
            # if 'usb' in product_description.lower() or 'socket' in product_description.lower() or 'outlet' in product_description.lower():
            #     charge = '有无线遥控功能'
            # else:
            #     charge = '没有无线遥控功能'
            #
            # if 'anti - fog' in product_description.lower() or 'defogger' in product_description.lower() or 'anti fog' in product_description.lower() or 'defog' in product_description.lower():
            #     chuwu = '有除雾功能'
            # else:
            #     chuwu = '没有除雾功能'
            #
            # if 'dimmable' in product_description.lower() or 'color adjustment' in product_description.lower() or 'stepless dimming' in product_description.lower() or '3 - color' in product_description.lower() or '3-Color' in product_description.lower() or 'Dimming' in product_description.lower() or 'dimmer' in product_description.lower():
            #     color_t = '有色调调节功能'
            # else:
            #     color_t = '没有色调调节功能'
            #
            # if 'temp' in product_description.lower():
            #     temp = '有温度显示功能'
            # else:
            #     temp = '没有温度显示功能'
            #
            # try:
            #     dimensions = re.search(r'Product dimensions\s*(.*?)(?:\n|$)',
            #                            product_descriptions.replace('Materials & Care', '')).group(1)
            #
            # except:
            #     try:
            #         dimensions = re.search(r'Product dimensions\s*(.*?)\n',
            #                                product_descriptions.replace('Materials & Care', '')).group(1)
            #     except:
            #         dimensions = " "
            # try:
            #     color = re.search(r'Colour\s*(.*?)(?:\n|$)', product_descriptions).group(1)
            # except:
            #     color = " "
            # # try:
            # # style = re.search(r'Item Firmness Description\s*(.*?)(?:\n|$)',products_description).group(1)
            # try:
            #     material = re.search(r'Material\s*(.*?)(?:\n|$)',
            #                          product_descriptions.replace('Materials & Care', '')).group(1)
            # except:
            #     try:
            #         material = re.search(r'Material\s*(.*?)\n',
            #                              product_descriptions.replace('Materials & Care', '')).group(1)
            #     except:
            #         material = " "

            # try:
            #     shape = re.search(r'Shape\s*(.*?)(?:\n|$)', product_description).group(1)
            # except:
            #     shape = " "

            # print(dimensions+"#"+install_method+"#"+material+"#"+sport_light+"#"+mirror+"#"+remote+"#"+charge+"#"+chuwu+"#"+color_t+"#"+temp)
            try:
                dimensions = re.search(r'Product Dimensions\s*(.*?)(?:\n|$)', product_descriptions.replace('Materials & Care', '')).group(1)

            except:
                try:
                    dimensions = re.search(r'Package Dimensions\s*(.*?)\n', product_descriptions.replace('Materials & Care', '')).group(1)
                except:
                    dimensions = " "
            try:
                material = re.search(r'Material\s*(.*?)(?:\n|$)',
                                     product_descriptions.replace('Materials & Care', '')).group(1)
            except:
                try:
                    material = re.search(r'Finish Type\s*(.*?)\n',
                                         product_descriptions.replace('Materials & Care', '')).group(1)
                except:
                    material = " "
            try:
                capacity = re.search(r'Capacity\s*(.*?)(?:\n|$)',
                                     product_descriptions.replace('Materials & Care', '')).group(1)
            except:
                capacity = " "

            print(dimensions + "#" + capacity + "#" + material)

            return dimensions + "#" + capacity + "#" + material

        else:

            return " "
        #     print(color)
        #     print(
        #         "#######################################################################################################")
        #
        #     # return dimensions+"#"+install_method+"#"+material+"#"+sport_light+"#"+mirror+"#"+remote+"#"+charge+"#"+chuwu+"#"+color_t+"#"+temp
        #     return color
        # else:
        #
        #     return " "

            # print(style)
            # return style
            # except:
            #     # print('无风格')
            #     # return '无风格'
            #     print('无项目 硬度 说明')
            #     return '无硬度'

    if title_text != '':
        random_num = round(random.uniform(8, 10), 2)
        time.sleep(random_num)
        title = driver1.find_element(by=By.ID, value='titleSection')
        title.click()
        # text = title_text+"#"+price
        text = have_product()
        return text
    else:
        print('该ASIN在亚马逊上已不存在')
        return ''

def get_url():
    ASIN0 = open('ASIN3.txt', 'r+', encoding='utf-8')
    ASINS = ASIN0.readlines()
    urls = ['https://www.amazon.com/dp/' + str(i).replace('\n', '') for i in ASINS]
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
            asin_product = open('ASIN_Products3.txt', 'a+', encoding='utf-8')
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
    # driver1.quit()
    # time.sleep(30000)
