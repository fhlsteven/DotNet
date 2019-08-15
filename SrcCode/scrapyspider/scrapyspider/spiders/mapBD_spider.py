import scrapy
import pickle

class MapBDSpider(scrapy.Spider):
    name = "mapBD"

    def start_requests(self):
        urls =[
            'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=atm&c=131&src=0&wd2=&pn=0&sug=0&l=13&b=(12924200,4814543;12967656,4856271)&from=webmap&biz_forward={"scaler":1,"styles":"pl"}&sug_forward=&auth=Z7g6eIw519IEZE6UBbxaWxSayJObzHYcuxHLHNLBLBxtDpnSCE@@B1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3Guxt58Jv7uUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7ucvY1SGpuxVthgW1GDfvyuf0wd0vyIMIOMCM7Sulp55CNBwbb9z8&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12962160,4832407&ie=utf-8&t=1565763642122',
            'http://quotes.toscrape.com/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
        
    def parse(self,response):
        self.log(response.body)
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        self.log('Saved file %s' % filename)