# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import os

class Dz9WebPipeline:
    # def open_spider(self, spider):
    #     if os.path.exists(spider.custom_settings['FEED_URI']):
    #         os.remove(spider.custom_settings['FEED_URI'])

    def open_spider(self, spider):
        feed_uri = spider.custom_settings['FEED_URI']
        with open(feed_uri, 'w') as ff:
            ff.write('')
        
 
    
