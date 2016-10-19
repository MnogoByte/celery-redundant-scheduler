# celery-redundant-scheduler

[Celery](http://celeryproject.org) beat sheduler provides ability to run multiple `celerybeat` instances.

# Problem
Prodaction deployment of periodic tasks requires fail-over for `celerybeat`. But, when you run multiple `celerybeat` instances, tasks would be duplicated. This scheduler resolves this problem by using `redis` for synchronization.

# Installation
```#bash
pip install git+https://github.com/MnogoByte/celery-redundant-scheduler.git
```

# Usage
Add `--scheduler=celery_redundant_scheduler:RedundantScheduler` option to your `worker` or `beat` service.

# Settings
- `CELERYBEAT_REDUNDANT_BACKEND_OPTIONS` - redis connection options.
- `CELERYBEAT_REDUNDANT_REDIS_KEYPREFIX` - prefix for redis keys. Default is `redundant-scheduler`.
- `CELERYBEAT_REDUNDANT_REDIS_LOCK_EXPIRES` - redis lock timeout. Default is 60 seconds.

# Write your own backend
1. Write subclass of `celery_redundant_scheduler.backends.base:BaseBackend`.
2. Set `CELERYBEAT_REDUNDANT_BACKEND` setting.

# Author

[Antonov Mikhail](https://github.com/atin65536)

# License

BSD - 3
