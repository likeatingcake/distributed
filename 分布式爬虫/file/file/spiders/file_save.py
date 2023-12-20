import scrapy
from ..items import FileItem
from scrapy import Spider


class FileSaveSpider(Spider):
    name = "file_save"
    allowed_domains = ["matplotlib.org"]
    start_urls = ["https://matplotlib.org/examples/"]

    def parse(self, response):
        # 获取包含了所有文件对象的列表
        message_list = response.xpath('//li[@class="toctree-l2"]')
        # 循环取出每一个文件对象
        for msg in message_list:
            # 提取文件对象中的href属性
            href = msg.xpath('./a/@href').extract_first()
            # 拼接完整路径,scrapy提供了response.urljoin提供了一个urljoin方法用于拼接路径，及其方便
            full_href = response.urljoin(href)
            # 设置回调函数get_file,发起二次请求，从链接中获取文件
            yield scrapy.Request(url=full_href, callback=self.get_file)

    def get_file(self, response):
        # 获取文件下载的地址
        file_url = response.xpath('//div[@class="section"]/p/a/@href').extract_first()
        # 拼接完整的文件下载地址
        full_file_url = response.urljoin(file_url)
        file_name = full_file_url.split('/')[-1]
        item = FileItem()
        item['file_name'] = file_name
        item['file_urls'] = full_file_url
        yield item
