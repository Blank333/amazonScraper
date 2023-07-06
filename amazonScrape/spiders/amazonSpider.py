import scrapy


class AmazonspiderSpider(scrapy.Spider):
    name = "amazonSpider"
    allowed_domains = ["www.amazon.in", "proxy.scrapeops.io"]
    start_urls = ["https://www.amazon.in/s?k=bags"]

    #First request
    def start_requests(self):
         yield scrapy.Request(url=self.start_urls[0], callback=self.parse)


    def parse(self, response):

        #Get the individual product cards and follow them for details
        products = response.css('div.s-result-item[data-component-type=s-search-result]')
        for product in products:
            product_url =  product.css('h2>a::attr(href)').get()

            if product_url is not None:
                product_url = 'https://www.amazon.in' + product_url
                yield scrapy.Request(url=product_url, callback = self.parse_product)

        #Go through all pages recursively
        next_url = response.css('.s-pagination-next::attr(href)').get()     
        if next_url is not None:
            next_url = 'https://www.amazon.in' + next_url
            yield scrapy.Request(url=next_url, callback = self.parse)
 
    def parse_product(self, response):

        #Get the ASIN and Manufacturer through loops as they can be unordered
        ASIN = ''
        Manufacturer = ''
        for i in range(1,len(response.xpath("//div[@id='detailBullets_feature_div']/ul/li").getall()) + 1 ):
            if(response.xpath(f"//div[@id='detailBullets_feature_div']/ul/li[{i}]/span/span[1]/text()").get().split('\n')[0] == 'ASIN'):
                ASIN = response.xpath(f"//div[@id='detailBullets_feature_div']/ul/li[{i}]/span/span[2]/text()").get()
            elif(response.xpath(f"//div[@id='detailBullets_feature_div']/ul/li[{i}]/span/span[1]/text()").get().split('\n')[0] == 'Manufacturer'):
                Manufacturer = response.xpath(f"//div[@id='detailBullets_feature_div']/ul/li[{i}]/span/span[2]/text()").get()

        #Get the details of the product
        yield {
            'Name': response.css('#productTitle::text').get().strip(),
            'Price': response.css('.a-price-whole::text').get(),
            'Rating': response.css('#acrPopover>span>a>span::text').get().strip(),
            'No. of Reviews':  response.css('#acrCustomerReviewText::text').get().split()[0],
            'URL': response.url,
            'Description': response.xpath("//div[@id='productDescription']/p/span/text()").get(),
            'Manufacturer': Manufacturer,
            'ASIN': ASIN

        }
