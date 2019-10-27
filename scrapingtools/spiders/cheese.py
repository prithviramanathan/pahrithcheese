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
        	a = item.split('-')
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
		words = text.split(':')
		if 'Region:' in text:
                    cheese['region'] = words[1]
		if 'Family:' in text:
		    cheese['family'] = words[1]
		if 'Fat content:' in text:
		    cheese['fat_content'] = words[1]
		if 'Colour:' in text:
		    cheese['colour'] = words[1]
		if 'Flavour:' in text:
                    print(words)
		    cheese['flavour'] = words[1]
		if 'Aroma:' in text:
		    cheese['aroma'] = words[1]
		if 'Texture:' in text:
		    cheese['texture'] = words[1]
		if 'Country of origin:' in text:
		    cheese['country_of_origin'] = words[1]
		if 'Type:' in text:
		    cheese['type'] = words[1]
	    yield cheese
            return
