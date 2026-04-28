from openpyxl import Workbook
from openpyxl.drawing.image import Image
from io import BytesIO
import requests
from PIL import Image as PILImage
import time

# 创建一个Excel工作簿
workbook = Workbook()
sheet = workbook.active

# 设置第一行的标题
sheet['A1'] = 'URL'
sheet['B1'] = 'Image'

def insert_image(url, row):
    while True:
        try:
            response = requests.get(url)
            time.sleep(5.0)
            image_content = response.content

            # 将图片转换为PILImage对象
            pil_image = PILImage.open(BytesIO(image_content))

            # 计算最终图像的大小
            cell_width = 50.0
            cell_height = 50.0
            sheet.row_dimensions[row].height = 45

            # 转换图片格式
            img_io = BytesIO()
            pil_image.save(img_io, 'JPEG')
            img_io.seek(0)

            # 使用openpyxl将图像插入单元格
            img = Image(img_io)
            img.width = cell_width
            img.height = cell_height
            sheet.add_image(img, f'B{row}')
            break

        except Exception as e:
            print(f"Failed to insert image from URL: {url}")
            print(str(e))

def read_urls_from_file(file_path):
    urls = []
    with open(file_path, 'r+') as file:
        for line in file:
            url = line.strip()
            if url:
                urls.append(url)
    return urls

# 从文件中读取图片链接
file_path = 'Tu链接.txt'
urls = read_urls_from_file(file_path)

# 将链接和图片插入Excel表格
for i, url in enumerate(urls, start=2):
    sheet[f'A{i}'] = url
    insert_image(url, i)

# 保存Excel文件
workbook.save('image_download.xlsx')

print("插入完成！")