# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
import requests


class Book(models.Model):
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=30, db_index=1)
    title = models.CharField(max_length=255, db_index=1)
    publisher = models.CharField(max_length=50, db_index=1)
    category = models.CharField(max_length=50, db_index=1)
    thumb = models.CharField(max_length=255, blank=1)

    @classmethod
    def crawl_from_daum(cls, search_dic):
        params = {
            'output': 'json',
            'apikey': settings.DAUM_API_KEY,
        }
        params.update(search_dic)
        r = requests.get('https://apis.daum.net/search/book', params=params)
        if r.status_code == 200:
            data = r.json()
            items = data.get('channel').get('item', [])

            books = []
            for item in items:
                book = cls(author=item.get('author'),
                           title=item.get('title'),
                           category=item.get('category'),
                           publisher=item.get('pub_nm'),
                           isbn=item.get('isbn'))
                book.save()
                books.append(book)
            return books
        return []

    @classmethod
    def crawl_by_isbn(cls, isbn=''):
        return cls.crawl_from_daum({
            'searchType': 'isbn',
            'q': isbn,
        })

    class Meta:
        db_table = 'book'
