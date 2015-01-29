# -*- coding: utf-8 -*-

# Scrapy settings for AmazonIphone6Comments project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'AmazonIphone6Comments'

SPIDER_MODULES = ['AmazonIphone6Comments.spiders']
NEWSPIDER_MODULE = 'AmazonIphone6Comments.spiders'

ITEM_PIPELINES = {
	'AmazonIphone6Comments.pipelines.Amazoniphone6CommentsPipeline' :300
}

COOKIES_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'AmazonIphone6Comments (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
	'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
     'AmazonIphone6Comments.spiders.rotate_useragent.RotateUserAgentMiddleware' :400
}