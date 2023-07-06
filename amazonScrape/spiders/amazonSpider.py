import scrapy


class AmazonspiderSpider(scrapy.Spider):
    name = "amazonSpider"
    allowed_domains = ["www.amazon.in"]
    start_urls = ["https://www.amazon.in/s?k=bags"]

    def parse(self, response):
        products = response.css('div.sg-row')
        for product in products:
            product_url = 'https://www.amazon.in' + product.css('h2>a').attrib['href']

            if product_url is not None:
                yield response.follow(product_url, callback = self.parse_product)

        next_url = response.css('span>a.s-pagination-next').attrib['href']      
        if next_url is not None:
            yield response.follow(next_url, callback = self.parse)
 
    def parse_product(self, response):
        pass
