# ptt-bot

 抓取 ptt 上的各種訊息，透過 discord_bot 發送

## 目錄

- [ptt-bot](#ptt-bot)
  - [目錄](#目錄)
  - [建置選項](#建置選項)
  - [本地運行](#本地運行)
    - [虛擬環境建置](#虛擬環境建置)
    - [相關套件安裝/記錄](#相關套件安裝記錄)
      - [安裝方式](#安裝方式)
      - [記錄已安裝套件](#記錄已安裝套件)
    - [環境檔設定](#環境檔設定)
      - [自訂環境設定](#自訂環境設定)
  - [使用 docker 建置並啟用](#使用-docker-建置並啟用)
    - [重新建置](#重新建置)
  - [使用方式](#使用方式)

## 建置選項

> 可以選擇在本地上運行，或是在docker上運行

## 本地運行

### 虛擬環境建置

> 建議使用虛擬環境以確保程式不會被其他項目影響
> 請先確定終端機、建置位置是否在本資料夾(ppt-bot)裡

![Current directory](readme/image/image2.png)

在終端機輸入下面這串指令即可在資料夾裡建置好環境

```bash
python -m venv .venv
```

啟動環境方式

windows

```bash
.venv\Scripts\activate
```

unix/macos

```bash
.venv/bin/activate
```

[環境建置相關文章(vscode in python)](https://code.visualstudio.com/docs/python/environments)

### 相關套件安裝/記錄

> 請先確定安裝前環境是否在虛擬環境(.venv 要存在)裡

![.venv](readme/image/image.png)

#### 安裝方式

將所有套件一次安裝

```bash
pip install -r requirements.txt
```

#### 記錄已安裝套件

將在虛擬環境上的套件記錄到 requirements.txt 裡

```bash
pip freeze > requirements.txt
```

不想讓 requirements.txt 裡的套件有版本限制的話可以使用下面的指令只留下安裝套件

```bash
pip freeze | sed 's/==.*$/''/' > requirements.txt
```

### 環境檔設定

將 .env-example.json 複製並改名成 .env  
並將裡面的範例文字取代成自己的設定值，填寫完畢後輸入下面的指令

```bash
py bot.py
```

即可啟動成功

#### 自訂環境設定

> 此設定並不影響運行

將 setting-example.json 複製並改名成 setting.json  
可將裡面的範例文字取代成自己的設定值

## 使用 docker 建置並啟用

> 如果不想在本地建置環境，可以使用docker建置  
> 請先確認 docker 是否有安裝，以及[環境檔](#環境檔設定)是否已設定完成

輸入輸入下面的指令即可啟動成功

```bash
docker-compose up 

# 在背景執行
docker-compose up -d
```

### 重新建置

當有更新一些內容需要重新建置並啟動，可以用這段指令

```bash
docker-compose up --build

# 在背景執行
docker-compose up --build -d
```

## 使用方式

輸入 `!ptt` 即可獲取最新的貼文

![success](/readme/image/image3.png)
