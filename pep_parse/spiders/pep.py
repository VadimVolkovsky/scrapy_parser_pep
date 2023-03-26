import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import NAME, NUMBER, STATUS, ALLOWED_DOMAINS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        """Собирает информацию об URL-адресах всех PEP"""
        pep_list = response.css(
            '#numerical-index table.pep-zero-table tbody tr'
        )
        for pep in pep_list:
            pep_link = pep.css('a::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Собирает информацию со страницы конкретного PEP"""
        h1 = response.css('#pep-content > h1::text').get().split()
        number = h1[1]
        name = ' '.join(h1[3:])
        status = response.css('abbr::text').get()
        data = {
            NUMBER: number,
            NAME: name,
            STATUS: status,
        }
        yield PepParseItem(data)
