# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy


#
# class FengniaopsPipeline(object):
#     def process_item(self, item, spider):
#         return item

class FengniaopsPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['imgurl']:
            yield scrapy.Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_name = request.url.split('/')[-1]

        path = u'{}'.format(image_name)
        return path
