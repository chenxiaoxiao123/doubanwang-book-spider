# doubanwang-book-spider
## 豆瓣读书爬虫

Python所写，豆瓣读书的爬虫，方便大家搜罗各种美美书！


### 更新

最近爬下了豆瓣所有的图书信息（5000多本）。 注：这里的代码不是爬下所有书籍所用的代码，仅供参考。


### 实现功能

1 可以爬下豆瓣读书标签下的所有图书 

2 按评分排名依次存储

3 存储到Excel中，可方便大家筛选搜罗，比如筛选评价人数>1000的高分书籍；可依据不同的主题存储到Excel不同的Sheet 

4 采用User Agent伪装为浏览器进行爬取，并加入随机延时来更好的模仿浏览器行为，避免爬虫被封（更新于 2015-5-20）


#运行条件：
python 3.6
import sys
import time
import urllib
import urllib.request
import importlib,sys
import requests
import numpy as np
from bs4 import BeautifulSoup
from openpyxl import Workbook
import lxml







