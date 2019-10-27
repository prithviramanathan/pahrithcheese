import scrapy

from scrapingtools.items import *

class CheeseSpider(scrapy.Spider):
	name = "cheese"

	def start_requests(self):
		urls = [
			'http://cheese.com',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		if response.url == 'http://cheese.com':
			info = ['parmesan']
			# print(info)
			# print(len(info))
			base_url = 'http:cheese.com/'
			for page in info:
				page = base_url + page
				yield scrapy.Request(page, callback=self.parse)
			return
		print("response:", response.body)
		"""
		pol_info = response.xpath('//font[@face="Verdana, Arial, Tahoma, Helvetica, Sans-Serif"]/b/text()').extract()
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
