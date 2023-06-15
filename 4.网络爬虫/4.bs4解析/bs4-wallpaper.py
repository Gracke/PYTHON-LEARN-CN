"""
1. 拿到主页面的源代码
2.通过href拿到子页面的内容。从子页面找到图片的下载地址
"""
import requests
from bs4 import BeautifulSoup
url = "https://wallhaven.cc/hot?page=2"
resp = requests.get(url)

main_page = BeautifulSoup(resp.text, 'html.parser')

wallpaper = main_page.find_all("a", class_="preview")
for i in wallpaper:
    href = i.get('href')    # 获取href的属性
    # 拿到子页面的源代码
    child_page_resp = requests.get(href)
    # 编码 utf-8
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text
    # 从子页面中获取源代码的下载路径
    child_page = BeautifulSoup(child_page_text,'html.parser')
    p = child_page.find("meta", property="og:image")
    img = p.get("content")
    img_resp = requests.get(img)
    img_name = img.split("/")[-1]
    with open("img/"+img_name, mode='wb') as f:
        f.write(img_resp.content)

        # img_resp.content 拿到字节
