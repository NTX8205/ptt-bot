import requests
from bs4 import BeautifulSoup
import re
import json

url = "https://www.ptt.cc/bbs/HardwareSale/index.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = []
    lists = []
    for div in soup.find_all("div", class_="r-ent"):
        if div.find_next("div", class_="r-list-sep"):
            elements.append(div)

    # 打印找到的元素
    for element in elements:
        # 找到标题和日期
        title_element = element.find("div", class_="title")
        title = title_element.text.strip()
        date = element.find("div", class_="date").text.strip()
        try :
            link = title_element.a["href"]
        except TypeError:
            pass
        # 打印标题和日期
        # print("标题:", title)
        # print("日期:", date)
        print("https://www.ptt.cc"+link)

        # 创建包含数据的字典
        data = {
            "title": title,
            "date": date,
            "link": link
        }
        lists.append(data)

    # 将数据转换为JSON格式

    # 打印JSON数据
    # print(json_data)
    # print(lists[0]["link"])
    # for i in json_data:
    #     print("https://www.ptt.cc"+i)