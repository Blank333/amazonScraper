
# AmazonScraper

AmazonScraper is a Python web scraping project built with Scrapy that allows you to extract product information from Amazon.com. It retrieves details such as product names, prices, ratings, and reviews for a given search query on Amazon.

This project demonstrates how to use Scrapy with ScrapeOps Proxy for web scraping with JavaScript rendering. It provides a basic setup for rendering JavaScript content and routing requests through the ScrapeOps proxy network.

## Features

- Search and scrape product information from Amazon.in.
- Extract product details.
- Save the scraped data to a CSV file for further analysis.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Blank333/amazonScraper.git
   ```

2. Navigate to the project directory:
   ```bash
   cd amazonScraper
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   This will install Scrapy, ScrapeOps Proxy, and ipython along with their dependencies.

5. Configure Scrapy with ScrapeOps Proxy:
   - Open the `settings.py` file and update the `SCRAPEOPS_API_KEY` variable with your ScrapeOps API key.

7. Run the spider:
   ```bash
   scrapy crawl amazonSpider
   ```

   The spider will now use ScrapeOps Proxy to render JavaScript content and route requests through the ScrapeOps proxy network.

## Additional Notes

- Adjust the spider logic in `spiders/your_spider.py` to define the specific scraping behavior you need.
- Modify the proxy as per your requirements.

## License

This project is licensed under the [MIT License](LICENSE).
