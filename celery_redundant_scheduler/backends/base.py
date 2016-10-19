# -*- coding: utf-8 -*-

from __future__ import absolute_import

from kombu.utils import cached_property

class BaseBackend(object):
    def __init__(self, app, **options):
        self.app = app
        self.options = options

    def get_connection(self):
        raise NotImplementedError('{} doe not implement `get_connection` method'.format(type(self)))

    @cached_property
    def connection(self):
        return self.get_connection()

    def lock(self):
        raise NotImplementedError('{} doe not implement `lock` method'.format(type(self)))

    def unlock(self):
        raise NotImplementedError('{} doe not implement `unlock` method'.format(type(self)))

    def get(self, key):
        raise NotImplementedError('{} doe not implement `get` method'.format(type(self)))
    
    def set(self, key, value):
        raise NotImplementedError('{} doe not implement `set` method'.format(type(self)))

