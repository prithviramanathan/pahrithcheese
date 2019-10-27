import scrapy

from scrapingtools.items import *
import re
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

class CheeseSpider(scrapy.Spider):
	name = "scrapingtools"

	def start_requests(self):
		urls = [
			'http://cheese.com/parmesan',
			'http://cheese.com/cheddar'
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		# print("response:", response.body)
		title_info = response.xpath('//title').extract()
                for item in title_info:
                    print('title: ', cleanhtml(item))
		description = response.xpath('//meta').extract()
                for item in description:
                    if 'description' in item:
                        a = item.split('content=')
                        print('desription:', a[1])
		other_info = response.xpath('//p').extract()
		for item in other_info:
			print('other info: ', cleanhtml(item))
		"""
		name_path = response.url.split("/")[-1].split(".")[0]
		pic_url = 'http://senate.ontheissues.org/pictures/' + name_path + '.jpg'

		politician = PoliticianItem(name=pol_info[1].rstrip(), office=pol_info[0], pic_url=pic_url)

		tables = response.xpath('//ul')
		names = response.xpath('//td[@align="center"]/font[@face="Arial"]/text()').extract()
		issues = list()
		for x in range(0, len(names)):
			#print("hey:", tables[x])
			items = tables[x].xpath('li/text()').extract()
			#print(items)
			# cool = tables[x].xpath('li')
			# print(cool)
			new_items = list()
			skip = False
			for item in items:
				if "Rated" in item:
					skip = True
				elif not skip:
					new_items.append(item)
				else:
					skip = False
			print(new_items)

			issue = IssueItem(issue=names[x].rstrip(), stances=new_items)
			issues.append(dict(issue))

		politician['issues'] = issues
		yield politician
		"""
