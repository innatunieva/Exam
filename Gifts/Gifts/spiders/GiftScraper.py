# -*- coding: utf-8 -*-
import scrapy


class GiftscraperSpider(scrapy.Spider):
    name = "GiftScraper"
    allowed_domains = ["https://www.giftcardmall.am/"]
     start_urls = ['http://giftcardmall.am/en/all-cards']
    

    def parse(self, response):
       def parse(self, response):
        for i in response.css('div.card_animate.card.all_cards.col-lg-3.col-md-4.col-xs-6'):
        	if len(i.css('div.card-copy p::text').re('[0-9]+'))==2:
	        	yield{
	        	"name" : i.css('div.card-copy h4.card_title a::text').re('[A-Z].+')[0],
	        	"link" : i.css('div.card-image a::attr(href)').extract_first(),
	        	"price" : (float(i.css('div.card-copy p::text').re('[0-9]+')[0])+float(i.css('div.card-copy p::text').re('[0-9]+')[1]))/2	
	        	}	
	        else:
	        	yield{
	        	"name" : i.css('div.card-copy h4.card_title a::text').re('[A-Z].+')[0],
	        	"link" : i.css('div.card-image a::attr(href)').extract_first(),
	        	"price" : float(i.css('div.card-copy p::text').re('[0-9]+')[0])
	        	}
