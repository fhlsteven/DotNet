from scrapy import Request
from scrapy.spiders import Spider
from scrapyspider.items import Population

class PopulationSpider(Spider):
    name = 'population'
    
    start_urls = ['https://www.phb123.com/city/renkou/rk.html']

    def parse(self,response):
        item = Population()
        items = response.xpath('.//table[@class="rank-table"]/tbody/tr')

        for i in items:
            if i.xpath('.//th'):
                self.log('...contine....')
                continue
            else:
                item['ranking'] = i.xpath('.//td[1]/text()').extract()[0]
                item['country'] = i.xpath('.//td[2]/a/p/text()').extract()[0]
                item['deteil_url'] = 'https://www.phb123.com'+i.xpath('.//td[2]/a/@href').extract()[0]
                item['flag_url'] =i.xpath('.//td[2]/a/span/img/@src').extract()[0]
                item['num'] = i.xpath('.//td[3]/text()').extract()[0]
                item['rate']= i.xpath('.//td[4]/text()').extract()[0]
                item['density']=i.xpath('.//td[5]/text()').extract()[0]
                yield item
        next_url = response.xpath('.//div[@class="page mt10"]/a[last()-1]/@href').extract()[0]
        last_url = response.xpath('.//div[@class="page mt10"]/a[last()]/@href').extract()[0]
        if next_url!=last_url:
            next_url ='https://www.phb123.com'+ next_url
            yield Request(next_url)
        
