#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : TOP250_MovieData.py
@Author: Xinzhe.Pang
@Date  : 2019/7/5 0:26
@Desc  : 
'''
# 1.网站分析
# 2.项目实践
    
import requests
from bs4 import BeautifulSoup
 
def get_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    movie_list = []
    for i in range(0, 10):# 共计10页
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers=headers, timeout=10)
        print(str(i + 1), "页面响应状态码：", r.status_code)
 
        soup = BeautifulSoup(r.text, "lxml")
        div_list = soup.find_all('div', class_='bd')
        for each in div_list:
            movie = each.p.text.strip()
            movie_list.append(movie)
        #print(r.text)
    return movie_list
 
movies = get_movies()
print(movies)