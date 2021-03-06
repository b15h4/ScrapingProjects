import scrapy
import csv
from ..items import BcassessmentItem
import json

class CollectLinks(scrapy.Spider):
	name = 'addresslinks'

	def start_requests(self):
		PID = []

		with open('PID.csv', mode='r') as csv_file:
			csv_reader = csv.reader(csv_file)
			for row in csv_reader:
				if not row:
					pass
				else:
					PID.append(','.join(row))
		
		for iii in PID:
			yield scrapy.Request('https://www.bcassessment.ca/Property/Search/GetByAddress?addr={}'.format(iii),callback=self.parse_items)

	def parse_items(self,response):
		try:
			jsonresponse = json.loads(response.body_as_unicode())
			Data = jsonresponse[0]
			Address = Data['value']		

			if 'A' in Address:
				yield {'response' : Address}
		except:
			pass