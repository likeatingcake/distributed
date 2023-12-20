# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo as pymongo
import scrapy
# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline


class FilePipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        file_name = item['file_name']
        return file_name

    def get_media_requests(self, item, info):
        file_link = item['file_urls']
        yield scrapy.Request(url=file_link, meta={'file_name': item['file_name']})

    def process_item(self, item, spider):
        result = super().process_item(item, spider)
        return result


class MongoPipeline(object):
    collection_name = 'files'  # Change this to your desired collection name

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # Use the 'url' field as a unique identifier or adjust as per your needs
        identifier = item['file_name']

        # Convert item to a dictionary
        # 准备存储到数据库的数据
        data_to_store = {
            'file_name': item.get('file_name'),
            'file_urls': item.get('file_urls')
        }

        # Update or insert the item into MongoDB
        self.db[self.collection_name].update_one({'file_name': identifier}, {'$set': data_to_store}, upsert=True)

        return item