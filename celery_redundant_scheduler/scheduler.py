# -*- coding: utf-8 -*-

from __future__ import absolute_import

from celery.utils.imports import symbol_by_name
from celery.beat import Scheduler, ScheduleEntry

__all__ = ['RedundantSchedulerEntry', 'RedundantScheduler']


class RedundantScheduleEntry(ScheduleEntry):
    backend = None
    def get_last_run_at(self):
        return self.backend.get(self.name)

    def set_last_run_at(self, value):
        return self.backend.set(self.name, value)

    last_run_at = property(get_last_run_at, set_last_run_at)

    def __init__(self, name=None, task=None, last_run_at=None,
        total_run_count=None, schedule=None, args=(), kwargs={},
        options={}, relative=False, app=None):

        self.name = name
        last_run_at = last_run_at or self.last_run_at

        super(RedundantScheduleEntry, self).__init__(name, task, last_run_at, total_run_count, schedule, args, kwargs, options, relative, app)


class RedundantScheduler(Scheduler):
    Entry = RedundantScheduleEntry

    def __init__(self, app, *args, **kwargs):
        self.backend = symbol_by_name(getattr(app.conf, 'CELERYBEAT_REDUNDANT_BACKEND', 'celery_redundant_scheduler.backends.redis:Backend')) (
            app, **getattr(app.conf, 'CELERYBEAT_REDUNDANT_BACKEND_OPTIONS', {})
        )

        class Entry(self.Entry):
            backend = self.backend

        self.Entry = Entry

        super(RedundantScheduler, self).__init__(app, *args, **kwargs)

    def setup_schedule(self):
        self.merge_inplace(self.app.conf.CELERYBEAT_SCHEDULE)
        super(RedundantScheduler, self).setup_schedule()

    def tick(self, *args, **kwargs):
        try:
            self.backend.lock()
            result = super(RedundantScheduler, self).tick(*args, **kwargs)
            return result
        finally:
            self.backend.unlock()
