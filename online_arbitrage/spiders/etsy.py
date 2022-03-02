from time import time
import scrapy
import csv
from datetime import datetime
from scrapy_splash import SplashRequest
from googletrans import Translator
import time
from glob import glob
import os
class EtsySpider(scrapy.Spider):
    name = 'etsy'
    allowed_domains=['www.etsy.com']
    
    path = '../online_arbitrage_files/ciceksepeti'
    all_files = glob(os.path.join(path, 'ciceksepeti_*.csv'))
    file = all_files[0]
    
    custom_settings = {
        'FEED_URI': '../online_arbitrage_files/etsy/etsy_' + os.path.basename(file),
        'FEED_FORMAT': 'csv',
    }
    
    #file_path = '../online_arbitrage_files/ciceksepeti/' + file
    def start_requests(self):
        
        
        with open(self.file, encoding='utf-8') as csv_file:
            # https://www.ciceksepeti.com/Arama?query=spectrum dijital suya dayanıklı kol saati d220278&qt=spectrum dijital suya dayanıklı kol saati d220278
            csv_reader = csv.reader(csv_file, delimiter=';')
            next(csv_reader)

            for count, row in enumerate(csv_reader):
                name_cs = row[0]
                price_cs = row[1]
                comm_cs = row[2]            
                note_cs = row[3]
                link_cs = row[4]
                image_cs = row[5]
                
                translator = Translator()
                name_et = translator.translate(name_cs, src='tr').text.replace(' ', '+')
                
                # 10 saniyede bir 10 saniye, diğer türlü 2 saniye
                if count % 10 == 0:
                    time.sleep(10)
                else:
                    time.sleep(2)
                
                
                
                #https://www.etsy.com/search?q=Original+Agate+Stone+Rosary+with+Personalized+Name&order=highest_reviews
                url = 'https://www.etsy.com/search?q=' + name_et + '&order=highest_reviews&ship_to=SA'
                yield SplashRequest(url=url,
                                    callback=self.parse,
                                    meta={'name_cs': name_cs,
                                        'price_cs': price_cs,
                                        'comm_cs': comm_cs,
                                        'note_cs': note_cs,
                                        'link_cs': link_cs,
                                        'image_cs': image_cs})

    def parse(self, response):
        products = response.css(
            'div.js-merch-stash-check-listing.v2-listing-card.wt-mr-xs-0.search-listing-card--desktop')
        #cStart=0 ()
        cStart=0
        #cStop=len(products)+1
        cStop=6
        for product in products[cStart:cStop]:
            name_et = product.css(
                'h3.wt-mb-xs-0.wt-text-truncate.wt-text-caption::text').get().strip()
            
            price_et = product.css(
                'p.wt-text-title-01 span.currency-value::text').get()
            price_et = round(float(price_et.replace(',', '')),2)
            
            comm_et = product.css(
                'span.wt-text-body-01.wt-text-gray.wt-display-inline-block.wt-nudge-b-1::text').get()
            
            if comm_et is not None:
                comm_et = float(comm_et.strip()[1:-1].replace(',', ''))
            
            rating_et = product.css(
                'span.stars-svg.stars-smaller input::attr(value)').get()
            if rating_et is not None:
                rating_et = round(float(rating_et),2)
            
            link_et = product.css(
                'a.listing-link::attr(href)').get()
            
            image_et = product.css(
                'div.height-placeholder img::attr(src)').get()
            
            price_cs = response.meta['price_cs']
            price_cs = float(price_cs.replace(',', ''))
            
            # Net kar hesaplaması
            brut_kar = price_et - price_cs
            
            # 100 gr, Saudi Arabia, PTT
            ship_fee = 16.5
            
            list_fee_tl = 1.41
            
            trans_fee_per = 0.05
            trans_fee = price_et * trans_fee_per
            
            vat_trans_fee_per = trans_fee_per * 0.18
            vat_trans_fee = price_et * vat_trans_fee_per
            
            etsy_pp_fee_tl = 3
            vat_etsy_pp_fee_tl = 3 * 0.18
            
            etsy_pp_fee_per= 0.065
            etsy_pp_fee = price_et * etsy_pp_fee_per
            
            vat_etsy_pp_fee_per = etsy_pp_fee_per * 0.18
            vat_etsy_pp_fee = price_et * vat_etsy_pp_fee_per
            
            all_et_fees_tl = list_fee_tl + trans_fee + vat_trans_fee + etsy_pp_fee_tl + vat_etsy_pp_fee_tl + etsy_pp_fee + vat_etsy_pp_fee
            
            net_kar = brut_kar - ship_fee - all_et_fees_tl
            
            yield {

                'name_cs': response.meta['name_cs'],
                'name_et': name_et,
                'price_cs': price_cs,
                'price_et': price_et,
                'brut_kar': brut_kar,
                'all_et_fees_tl': all_et_fees_tl,
                'net_kar': net_kar,
                'com_count_cs': response.meta['comm_cs'],
                'com_count_et': comm_et,
                'rating_et': rating_et,
                'note_cs': response.meta['note_cs'],
                'link_et': link_et,
                'link_cs': response.meta['link_cs'],
                'image_et': image_et,
                'image_cs': response.meta['image_cs'],
                
            }
