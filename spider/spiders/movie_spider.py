import scrapy
from spider.items import MovieItem

class QuotesSpider(scrapy.Spider):
    name = "movies"
    domain = "https://www.nunuyy5.org"
    def start_requests(self):
        urls = [
        self.domain + '/dianying/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
        # movie_item = {}
        # print("#######################################")
        for li in response.css('div.lists-content')[1].css("li"):
            link = response.urljoin(li.css('a::attr(href)').get())
            # movie_item['name'] = li.xpath('h2/a/text()').get()
            # movie_item['year'] = li.css('div.countrie span::text')[0].get()
            # movie_item['country'] = li.css('div.countrie span::text')[1].get()
            # movie_item['rate'] = li.css('footer span.rate::text').get()
            # detail = yield
            # if not response.css('div.product-excerpt'):
            # yield scrapy.Request(url=movie_item['link'], callback=self.parse_detail, cb_kwargs={"movie_item": movie_item})
            yield scrapy.Request(url=link, callback=self.parse_detail)
        next_page = response.css("li.next-page a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_detail(self, response):
        # movie_item = kwargs.get("movie_item")
        # detail = response.css('div.product-excerpt')
        # director = detail[0].xpath('span/a/text()').getall()
        # actor = detail[1].xpath('span/a/text()').getall()
        # category = detail[2].xpath('span/a/text()').getall()
        # summary = detail[5].xpath('span/text()').getall()
        # print("=========================================")
        # movie_item = {}
        # movie_item['name'] = li.xpath('h2/a/text()').get()
        # movie_item['year'] = li.css('div.countrie span::text')[0].get()
        # movie_item['country'] = li.css('div.countrie span::text')[1].get()
        # movie_item['rate'] = li.css('footer span.rate::text').get()
        # movie_item['director'] = director
        # movie_item['actor'] = actor
        # movie_item['category'] = category
        # movie_item['summary'] = summary
        # print("=========================================")
        detail = response.css('div.product-excerpt')
        yield {
            'name': response.css('h1.product-title::text').get(),
            'category':  detail[2].xpath('span/a/text()').getall(),
            'year': response.css('h1.product-title  span::text').get(),
            'country': detail[3].xpath('span/a/text()').getall(),
            'rate': response.css('h1.product-title  span.rate::text').get(),
            'director': detail[0].xpath('span/a/text()').getall(),
            'actor': detail[1].xpath('span/a/text()').getall(),
            'summary': detail[5].xpath('span/text()').get(),
            'link': response.url
        }

