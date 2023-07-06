# Scrapy settings for amazonScrape project


BOT_NAME = "amazonScrape"

SPIDER_MODULES = ["amazonScrape.spiders"]
NEWSPIDER_MODULE = "amazonScrape.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

#Scrapeops settings
SCRAPEOPS_API_KEY = '1e8ac0b5-2e23-4910-b36e-37f92c6de5c7'
SCRAPEOPS_PROXY_ENABLED = True
SCRAPEOPS_PROXY_SETTINGS = {'country': 'in', 'render_js': 'true'} 
DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

#Create a csv file for the data
FEEDS = {
    'product_info.csv' : {'format': 'csv'}
}