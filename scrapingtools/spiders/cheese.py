import scrapy

from scrapingtools.items import *
import re
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

# cheeses = 'parmesan gouda cheddar feta mozzarella brie pepper-jack alphabetical'
alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
letter_array = alphabet.split()

class CheeseSpider(scrapy.Spider):
	name = "scrapingtools"

	def start_requests(self):
		for letter in letter_array:
			url = 'http://cheese.com/alphabetical/?per_page=100&i=' + letter
			yield scrapy.Request(url=url, callback=self.parse)


	def parse(self, response):
            if 'https://cheese.com/alphabetical/' in response.url:
		info = response.xpath('//h3/a/@href').extract()
                info = list(info)
                info = set(info)
                # print('cheeses: ', info)
                base_url = 'http://cheese.com/'
                for page in info:
                    page = base_url + page
                    yield scrapy.Request(page, callback = self.parse)
                return
		# print("response:", response.body)
	    cheese = CheeseItem()
	    title_info = response.xpath('//title').extract()
            for item in title_info:
                item = cleanhtml(item)
        	a = item.split('-')
		cheese['name'] = a[0].strip()
		break
	    description = response.xpath('//meta').extract()
            got_description = False
            got_image = False
            for item in description:
                if 'description' in item and not got_description:
                    a = item.split('content=')
                    cheese['description'] = a[1].split('\"')[1].strip()
                    got_description = True
                if 'twitter:image' in item and not got_image:
                    a = item.split('content=')
                    cheese['image'] = a[1].split('\"')[1].strip()
                    got_image = True
	    other_info = response.xpath('//p').extract()
	    for item in other_info:
		text = cleanhtml(item)
		words = text.split(':')
		if 'Region:' in text:
                    cheese['region'] = words[1].strip()
		if 'Family:' in text:
		    cheese['family'] = words[1].strip()
		if 'Fat content:' in text:
		    cheese['fat_content'] = words[1].strip()
		if 'Colour:' in text:
		    cheese['colour'] = words[1].strip()
		if 'Flavour:' in text:
                    # print(words)
		    cheese['flavour'] = words[1].strip()
		if 'Aroma:' in text:
		    cheese['aroma'] = words[1].strip()
		if 'Texture:' in text:
		    cheese['texture'] = words[1].strip()
		if 'Country of origin:' in text:
		    cheese['country_of_origin'] = words[1].strip()
		if 'Type:' in text:
		    cheese['type'] = words[1].strip()
	    yield cheese
            return
