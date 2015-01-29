#/usr/bin/python
#-*-coding:utf-8-*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy import log

from AmazonIphone6Comments.items import Amazoniphone6CommentsItem

class AmazonIphone6CommentsSpider(Spider):
    """docstring for AmazonIphone6CommentsSpider"""
    
    name = "AmazonIphone6CommentsSpider"
    download_delay = 3
    allowed_domains = ["amazon.cn"]

    global count
    count = 0

    start_urls = [
        "http://www.amazon.cn/s/ref=nb_sb_noss_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=node%3D665002051&field-keywords=iphone6&rh=n%3A664978051%2Cn%3A665002051%2Ck%3Aiphone6"
    ]

    def parse(self,response):
        sel = Selector(response)

        if "product-reviews" in response.url:
            comments = sel.xpath("//table[@id='productReviews']//div[@style='margin-left:0.5em;']")

            for comment in comments:
                
                global count

                count = count + 1
                print count

                item = Amazoniphone6CommentsItem()

                comment_content = comment.xpath("div[@class='reviewText']/text()").extract()
                comment_time = comment.xpath("div/span/nobr/text()").extract()
                comment_star = comment.xpath("div/span/span/span/text()").extract()
                # comment_useful = comment.xpath("")

                item["comment_content"] = [n.encode('utf-8') for n in comment_content]
                item["comment_time"] = [n.encode('utf-8') for n in comment_time]
                item["comment_star"] = [n.encode('utf-8') for n in comment_star]

                yield item

            for next_url in sel.xpath("//table[2]//div[@class='CMpaginate']/span/a[last()]/@href").extract():
                yield Request(next_url,callback=self.parse)

        else:
            goods = sel.xpath("//li[@class='s-result-item']")
        
            for good in goods:
                for comment_url in good.xpath("div/div/a[@class='a-size-small a-link-normal a-text-normal']/@href").extract():
                    yield Request(comment_url,callback=self.parse)

            for url in sel.xpath("//a[@id='pagnNextLink']/@href").extract():
                yield Request("http://www.amazon.cn"+url,callback=self.parse)