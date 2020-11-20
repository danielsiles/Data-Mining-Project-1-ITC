from infra.scrapers.base_scraper import BaseScraper


class MatchReportScraper(BaseScraper):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def scrape(self):
        """
        Get the html page with the report of a match
        :return: Html element scraped by the driver
        """
        self._driver.get(self._url)
        return self._driver.execute_script("return document.documentElement.outerHTML;")