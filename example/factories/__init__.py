# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import factory
from faker import Factory as FakerFactory
from example.models import Blog, Author, Entry

faker = FakerFactory.create()
faker.seed(983843)

class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    name = factory.LazyAttribute(lambda x: faker.name())


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.LazyAttribute(lambda x: faker.name())
    email = factory.LazyAttribute(lambda x: faker.email())


class EntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Entry

    headline = factory.LazyAttribute(lambda x: faker.sentence(nb_words=4))
    body_text = factory.LazyAttribute(lambda x: faker.text())

    blog = factory.SubFactory(BlogFactory)

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if extracted:
            if isinstance(extracted, (list, tuple)):
                for author in extracted:
                    self.authors.add(author)
            else:
                self.authors.add(extracted)
