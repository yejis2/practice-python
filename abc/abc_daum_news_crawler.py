
from abc_crawlerBase import CrawlerBase

class DaumNewsCrawler(CrawlerBase):
    def run(self):
        print('daum run')

    def parse_html(self, text):
        pass


if __name__ == '__main__':
    daum_news_crawler = DaumNewsCrawler()
    daum_news_crawler.run()