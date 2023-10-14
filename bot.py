import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import re
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

# 創建一個Discord機器人客戶端
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# 修改你的機器人令牌
TOKEN = jdata["token"]

# 定義你的PTT爬蟲函數
def ptt_crawler():
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
            link = title_element.a["href"]

            # 创建包含数据的字典
            data = {
                "title": title,
                "date": date,
                "link": link
            }
            lists.append(data)

        return lists
    else:
        return []

# 定義一個機器人命令來觸發爬蟲
@bot.command()
async def ptt(ctx):
    print("success")
    links = ptt_crawler()
    await ctx.send("https://www.ptt.cc"+links[len(links)-1]['link'])

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# 在主函數中啟動機器人
if __name__ == '__main__':
    bot.run(TOKEN)
