import scrapy

class OLXMotorSpider(scrapy.Spider):
    name = "olx_motor"
    start_urls = [
        'https://www.olx.co.id/motor-bekas_c200',
    ]
    
    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,  
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    def parse(self, response):
        motor_links = response.xpath('//a[contains(@href, "/item/")]/@href').getall()
        
        for link in motor_links:
            absolute_url = response.urljoin(link)
            yield scrapy.Request(url=absolute_url, callback=self.parse_motor_detail)

        next_page = response.css('a.next::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_motor_detail(self, response):
        harga = response.css('span[data-aut-id="itemPrice"]::text').extract_first()
        tahun = response.css('span[data-aut-id="value_m_year"]::text').extract_first()
        km = response.css('span[data-aut-id="value_mileage"]::text').extract_first()
        brand = response.css('span[data-aut-id="value_make"]::text').extract_first()

        yield {
            'Harga': harga.strip() if harga else None,
            'Tahun': tahun if tahun else None,
            'KM': km if km else None,
            'Brand': brand if brand else None,
        }
    