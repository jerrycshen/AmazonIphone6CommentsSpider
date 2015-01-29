# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Amazoniphone6CommentsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    comment_content = scrapy.Field()
    comment_time = scrapy.Field()	
    # 评分
    comment_star = scrapy.Field()  	
    # # 多少人认为该评论有用，亚马逊特有的一种方式，格式例如5/7，说明七个人中五个人认为该评论有用
    # comment_useful = scrapy.Field()	
