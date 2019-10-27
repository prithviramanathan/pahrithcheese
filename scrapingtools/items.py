# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class CheeseItem(scrapy.Item):
	name = scrapy.Field()
	description = scrapy.Field()
	country_of_origin = scrapy.Field()
	region = scrapy.Field()
	type = scrapy.Field()
	fat_content = scrapy.Field()
	family = scrapy.Field()
	colour = scrapy.Field()
	flavour = scrapy.Field()
	texture = scrapy.Field()
	aroma = scrapy.Field()
        image = scrapy.Field()


class PoliticianItem(scrapy.Item):
	name = scrapy.Field()
	office = scrapy.Field()
	pic_url = scrapy.Field()
	issues = scrapy.Field()

class IssueItem(scrapy.Item):
    issue = scrapy.Field()
    stances = scrapy.Field()
