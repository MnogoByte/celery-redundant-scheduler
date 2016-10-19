# -*- coding: utf-8 -*-

from __future__ import absolute_import

from celery.exceptions import ImproperlyConfigured

from .base import BaseBackend

try: 
    import cPickle as pickle
except ImportError:
    import pickle

try:
    import redis
    Redis = redis.Redis
except ImportError:
    Redis = None


class Backend(BaseBackend):
    def __init__(self, *args, **kwargs):
        super(Backend, self).__init__(*args, **kwargs)
        self.key_prefix = getattr(self.app.conf, 'CELERYBEAT_REDUNDANT_REDIS_KEYPREFIX', 'redundant-scheduler')
        self.lock_expires = getattr(self.app.conf, 'CELERYBEAT_REDUNDANT_REDIS_LOCK_EXPIRES', 60)
        self._lock = None
        self.lock_count = 0

    def get_connection(self):
        if Redis is None:
            raise ImproperlyConfigured('`redis `library is not installed')

        return Redis(**self.options)

    def get_key_with_prefix(self, key):
        if self.key_prefix:
            return '{}-{}'.format(self.key_prefix, key)

        return key

    def lock(self):
        if self._lock is None:
            self._lock = self.connection.lock(self.get_key_with_prefix('lock'), self.lock_expires)
            self._lock.acquire()
            
        self.lock_count += 1

    def unlock(self):
        if self.lock_count > 0:
            self.lock_count -= 1

        if self._lock is not None and self.lock_count <= 0:
            self._lock.release()
            self._lock = None

    def get(self, key):
        result = self.connection.get(self.get_key_with_prefix(key))
        if result is not None:
            return pickle.loads(result)

        return result

    def set(self, key, value):
        return self.connection.set(self.get_key_with_prefix(key), pickle.dumps(value))

