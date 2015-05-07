# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
import requests


class Book(models.Model):
    author = models.CharField(max_length=255)
    translator = models.CharField(max_length=255)
    isbn = models.CharField(max_length=30, db_index=1)
    title = models.CharField(max_length=255, db_index=1)
    publisher = models.CharField(max_length=50, db_index=1)
    category = models.CharField(max_length=50, db_index=1)
    thumb = models.CharField(max_length=255, blank=1)

    # CONSTANT
    ALLOWED_SEARCH_TYPES = ['all', 'title', 'keyword', 'isbn', 'contents', 'overview', 'publisher']
    DAUM_API_URL = 'https://apis.daum.net/search/book'

    @classmethod
    def crawl_from_daum(cls, search_dic):
        if search_dic.get('searchType', 'all') not in cls.ALLOWED_SEARCH_TYPES:
            return []

        params = {
            'apikey': settings.DAUM_API_KEY,
            'output': 'json',
            'result': 20,
        }
        params.update(search_dic)
        r = requests.get(cls.DAUM_API_URL, params=params)
        if r.status_code == 200:
            data = r.json()
            items = data.get('channel').get('item', [])

            searched_isbn_list = map(lambda i: i.get('isbn13'), items)
            books_from_database = cls.objects.filter(isbn__in=searched_isbn_list)
            books = [book for book in books_from_database]
            duplicated_isbn_list = map(lambda b: b.isbn, books)

            remove_highlight = lambda s: s.replace('&lt;b&gt;', '').replace('&lt;/b&gt;', '')
            for item in items:
                if item.get('isbn13') in duplicated_isbn_list:
                    continue

                defaults = {'author': remove_highlight(item.get('author')),
                            'translator': remove_highlight(item.get('translator')),
                            'title': remove_highlight(item.get('title')),
                            'category': remove_highlight(item.get('category')),
                            'publisher': remove_highlight(item.get('pub_nm')),
                            'thumb': item.get('cover_l_url')}
                book, created = cls.objects.get_or_create(isbn=item.get('isbn13'), defaults=defaults)
                books.append(book)
            return books
        return []

    @classmethod
    def search(cls, search_type, q):
        return cls.crawl_from_daum({
            'searchType': search_type,
            'q': q,
        })

    def to_json(self):
        return {'id': self.id,
                'author': self.author,
                'translator': self.translator,
                'isbn': self.isbn,
                'title': self.title,
                'publisher': self.publisher,
                'category': self.category,
                'thumb': self.thumb}

    class Meta:
        db_table = 'book'
