# celery-redundant-scheduler

[Celery](http://celeryproject.org) beat scheduler providing ability to run multiple `celerybeat` instances.


# Problem
Production level deployment requires redundancy and fault-tolerance environment. Unfortunately [Celery](http://celeryproject.org) doesn't provide periodic tasks scheduling redundancy out of the box. Running multiple `celerybeat` instances results multiple scheduled tasks queuing. This package provides synchronized scheduler class. By default `redis` backend used, but developers are free too use their own based on package primitives.


# Installation
```#bash
pip install celery-redundant-scheduler
pip install git+https://github.com/MnogoByte/celery-redundant-scheduler.git
```


# Usage
1. Setup scheduler synchronization backend:
```
    CELERYBEAT_REDUNDANT_BACKEND_OPTIONS = {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': 'secret'
    }
```
2. Provide `--scheduler=celery_redundant_scheduler:RedundantScheduler` option running your `worker` or `beat` instance.


# Settings
- `CELERYBEAT_REDUNDANT_BACKEND_OPTIONS` - redis connection options.
- `CELERYBEAT_REDUNDANT_REDIS_KEYPREFIX` - prefix for redis keys. Default is `redundant-scheduler`.
- `CELERYBEAT_REDUNDANT_REDIS_LOCK_EXPIRES` - redis lock timeout. Default is 60 seconds.


# Using custom scheduler synchronization backend
1. Define subclass of `celery_redundant_scheduler.backends.base:BaseBackend`.
2. Override back-end interaction methods.
3. Provide backend options with `CELERYBEAT_REDUNDANT_BACKEND_OPTIONS`
4. Claim using your subclass providing `CELERYBEAT_REDUNDANT_BACKEND` setting or environment variable.


# Author

[Antonov Mikhail](https://github.com/atin65536)

# License

BSD - 3
