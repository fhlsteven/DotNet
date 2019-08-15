# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DBMovieItem(scrapy.Item):
    # 排名
    ranking = scrapy.Field()
    # movie name
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评论人数
    score_num =scrapy.Field()

class Population(scrapy.Item):
    # 世界排名
    ranking = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 人口数量
    num = scrapy.Field()
    # 增长率
    rate = scrapy.Field()
    # 人口密度（公里²）
    density = scrapy.Field()
    # 详情链接
    deteil_url = scrapy.Field()
    # 国旗
    flag_url = scrapy.Field()


