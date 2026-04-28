import os
import requests
from concurrent.futures import ThreadPoolExecutor

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
            print(f"图片 {save_path} 下载完成！")
    else:
        print(f"图片 {url} 下载失败！")

def download_images(image_urls, save_folder):
    # 创建保存图片的文件夹
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    with ThreadPoolExecutor() as executor:
        # 遍历图片链接并提交下载任务给线程池
        for url_image in image_urls:
            url = str(url_image).split('##')[0]
            image_name = str(url_image).split('##')[1]
            # 拼接保存路径和文件名
            save_path = os.path.join(save_folder, f"{image_name}.jpg")
            # 提交下载任务给线程池
            executor.submit(download_image, url, save_path)

def get_images_name_url():
    product0 = open('images.txt', 'r+', encoding='utf-8')
    products = product0.readlines()
    products1 = [str(i).replace('\n', '') for i in products]
    return products1

if __name__ == '__main__':
    image_urls = get_images_name_url()
    print(image_urls)
    save_folder = 'G:\图片库'
    download_images(image_urls, save_folder)