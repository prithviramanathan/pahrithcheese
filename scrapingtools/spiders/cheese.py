import scrapy

from scrapingtools.items import *
import re
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

cheeses = 'parmesan gouda cheddar feta mozzarella brie pepper-jack'
cheese_array = cheeses.split()

class CheeseSpider(scrapy.Spider):
	name = "scrapingtools"

	def start_requests(self):
		for cheese in cheese_array:
			url = 'http://cheese.com/' + cheese
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		# print("response:", response.body)
	    cheese = CheeseItem()
	    title_info = response.xpath('//title').extract()
            for item in title_info:
                item = cleanhtml(item)
        	a = item.split(' ')
		cheese['name'] = a[0]
		break
	    description = response.xpath('//meta').extract()
            for item in description:
                if 'description' in item:
                    a = item.split('content=')
                    cheese['description'] = a[1].split('\"')[1]
                    break
	    other_info = response.xpath('//p').extract()
	    for item in other_info:
			text = cleanhtml(item)
			words = text.split(':')[1]
			if 'Region' in text:
                cheese['region'] = words
			if 'Family' in text:
		    	cheese['family'] = words
			if 'Fat content' in text:
				cheese['fat_content'] = words
			if 'Colour' in text:
				cheese['colour'] = words
			if 'Flavour' in text:
				cheese['flavour'] = words
			if 'Aroma' in text:
				cheese['aroma'] = words
			if 'Texture' in text:
				cheese['texture'] = words
			if 'Country of origin' in text:
				cheese['country_of_origin'] = words
			if 'Type' in text:
				cheese['type'] = words
		yield cheese
                return
