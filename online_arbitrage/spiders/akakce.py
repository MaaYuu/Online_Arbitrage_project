import scrapy
import csv
from datetime import datetime
from scrapy_splash import SplashRequest

class AkakceSpider(scrapy.Spider):
    name = 'akakce'
    custom_settings = {
        'FEED_URI': '../online_arbitrage_files/' + datetime.today().strftime('%Y_%m_%d') +'/' + name + '.csv',
        'FEED_FORMAT': 'csv',
    }
    def start_requests(self):
        file_path = '../online_arbitrage_files/' + datetime.today().strftime('%Y_%m_%d') + '/ciceksepeti.csv'
        with open(file_path, encoding='utf-8') as csv_file:
            # https://www.ciceksepeti.com/Arama?query=spectrum dijital suya dayanıklı kol saati d220278&qt=spectrum dijital suya dayanıklı kol saati d220278
            csv_reader = csv.reader(csv_file, delimiter=';')
            next(csv_reader)

            for row in csv_reader:
                name_cs = row[0]
                price_cs = row[1]
                com_count_cs = row[2]
                note_cs = row[3]
                link_cs = row[4]
                #https://www.akakce.com/arama/?q=Papatya+G%C3%BCm%C3%BC%C5%9F+Bileklik&s=2
                url = 'https://www.akakce.com/arama?q=' + name_cs + '&s=2'
                yield SplashRequest(url=url,
                                     callback=self.parse,
                                     meta={'name_cs': name_cs,
                                           'price_cs': price_cs,
                                           'com_count_cs': com_count_cs,
                                           'note_cs': note_cs,
                                           'link_cs': link_cs})

    def parse(self, response):
        products = response.css('li.n-p.w')
        #cStart=0
        cStart=0
        #cStop=len(products)
        cStop=4
        for product in response[cStart:cStop]:
            name_ak = product.css('h3.pn_v8::text').get()
            price_ak = product.xpath('//article/span/span/text()').get()
            link_ak = product.css('a.pw_v8::attr(href)').get()
            kargo_ak = product.xpath('//em/text()').get()
            if kargo_ak is not None:
                kargo_ak = 0
            
    
            yield {

                'name_cs': response.meta['name_cs'],
                'name_ak': name_ak,
                'price_cs': response.meta['price_cs'],
                'price_ak': price_ak,
                'kargo_ak': kargo_ak,
                'com_count_cs': response.meta['com_count_cs'],
                'note_cs': response.meta['note_cs'],
                'link_ak': link_ak,
                'link_cs': response.meta['link_cs']
                
            }