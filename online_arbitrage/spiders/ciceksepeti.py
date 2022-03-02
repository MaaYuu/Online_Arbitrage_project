import scrapy
from datetime import datetime
#from scrapy_splash import SplashRequest

class CiceksepetiSpider(scrapy.Spider):
    name = 'ciceksepeti'
    allowed_domains=['www.ciceksepeti.com']
    custom_settings = {
        'FEED_URI': '../online_arbitrage_files/ciceksepeti/' + name  +'_' + datetime.today().strftime('%Y-%m-%d') + '_' + '%(kategori)s' + '_' + '%(fiyat)s' + '_' + '%(siralama)s' + '.csv',
        'FEED_FORMAT': 'csv'
    }

    def start_requests(self):
        #url_base = 'https://www.ciceksepeti.com/tum-urunler?df=2007101'
        categories_dict =   {'EvYasam': ',2007147',
                        'HediyeSetleri': ',2014253',
                        'Hediyelik': ',2009384',
                        'Hobi' : ',2008680',
                        'Kits': ',2089408',
                        'Kozmetik': ',2009388',
                        'Moda' : ',2009385',
                        'HediyeSetleri8' : ',2121501',
                        'OfisKirtasiye' : ',2008044',
                        'OtoAksesuar' : ',2009386',
                        'Oyuncak' : ',2009387',
                        'SporOutdoor' : ',2008662',
                        'TakiSaatAksesuar' : ',2009390',
                        'KisiyeOzel' : ',2007217'
                            }
        
        fiyat_dict = {'Max50': '1',
                      'Max100': '1,2',
                      'Max150': '1,2,3',
                      'Max200': '1,2,3,4',
                      'Max250': '1,2,3,4,5',
                      'Max500': '1,2,3,4,5,6',
                      'Max1000':'1,2,3,4,5,6,7',
                      'Min1000': '1,2,3,4,5,6,7,8'
                      }
        
        siralama_dict = {'CokSatilan':'1',
                         'Pahali': '2',
                         'Ucuz': '3',
                         'Begenilen': '7',
                         'Degerlendirilen': '8',
                         'Yeni': '9',
                         '':''
                        }
        
        url = 'https://www.ciceksepeti.com/tum-urunler?df=2007101'
        
        # Argümanlar
        
        if self.kategori != '':
            kategoriler = self.kategori.split(',')
            for category in kategoriler:
                url = url + categories_dict[category]
        
        if self.fiyat != '':
            fiyat = self.fiyat
            fiyat_url = '&priceID=' + fiyat_dict[fiyat]
            url = url + fiyat_url
        
        if self.siralama != '':
            siralama = self.siralama
            siralama_url = '&orderby='+ siralama_dict[siralama]
            url = url + siralama_url
            
        yield scrapy.Request(url=url, callback=self.parse)
        

    def parse(self, response):
        products = response.css(
            'div.products__item.js-category-item-hover.js-product-item-for-countdown')
        #cStart=0
        cStart=0
        #cStop=len(products)+1
        cStop=21
        for product in products[cStart:cStop]:
            name = product.css('p.products__item-title::text').get()
            price = product.css('div.price.price--now::attr(data-price)').get()
            price = round(float(price.replace(',','')),2)
            comm  = product.css('span.products-stars__review-count::text').get()
            if comm is not None:
                comm = comm[1:-1]
            if comm == '999+':
                comm = float(comm[:-1])
            note = product.css('span.products__item-badge-text::text').get()
            link = product.css(
                'a.products__item-link.js-products__item-link::attr(href)').get()
            full_link = 'https://www.ciceksepeti.com' + link
            image = product.css('img::attr(data-src)').get()
            
            yield {
                'name'        : name,
                'price'       : price,
                'comm' : comm,
                'note': note,
                'full_link': full_link,
                'image': image
            }