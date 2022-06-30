
from abc_crawlerBase import CrawlerBase

class NaverNewsCrawler(CrawlerBase):
    def run(self):
        print("naver run")

    def parse_html(self, text):
        pass


if __name__ == '__main__':
    naver_news_crawler = NaverNewsCrawler()
    naver_news_crawler.run()
