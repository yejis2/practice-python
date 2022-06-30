from abc import *

class CrawlerBase(metaclass=ABCMeta):

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def parse_html(self, text):
        pass