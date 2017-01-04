
# Django Celery Heartbeat

This small Django app enables you to get notifications if your celery workers
start falling behind. The principle of operation is that there is a celery
task which should be run frequently to update a value in a data store with
the current timestamp, and a Django command to check whether the latest
updated timestamp is too far in the past. If it is, the command uses standard
Django logging facility to log an error.

## Configuration

Configuring django-celery-heartbeat is straightforward. The only requirement
is that you have already configured the Django cache.

**Step 1.**: Install django-celery-heartbeat:

    pip install django-celery-heartbeat

**Step 2.**: Add it to your `INSTALLED_APPS` in your settings.py:

    INSTALLED_APPS = [
        ...
        'celery_heartbeat',
        ...
    ]

**Step 3.**: Configure logging in your settings.py:

    LOGGING = {
        ...
        'loggers': {
            ...
            'celery_heartbeat': {
                'handlers': ['mail_admins'],
                'level': 'WARNING',
                'propagate': False,
            },
        },
        ...
    }

You can use whatever method you'd like for sending out the notification, but `mail_admins` is one of the simplest.

**Step 4.**: Configure the timestamp update task.

You can do this using either your system's cron daemon, or using Celery's built-in scheduler (Celery beat). To do it using cron:

     * * * * * APP_USER_NAME  /path/to/manage.py trigger_celery_heartbeat

If you would prefer to set it up using Celery beat, add this to your settings.py:


    CELERYBEAT_SCHEDULE = {
        ...
        'heartbeat': {
            'task': 'endorfyn.heartbeat',
            'schedule': crontab(minute='*'),
        },
        ...
    }

**Step 5.**: Configure the heartbeat check command to run periodically.

This command cannot be run by Celery beat because if celery is falling behind, it would not be run with the correct frequency. Your system's cron daemon is probably the simplest choice:

     * * * * * APP_USER_NAME  /path/to/manage.py check_celery_heartbeat

## Additional options

django-celery-heartbeat has the following options you can specify in your settings.py

`CELERY_HEARTBEAT_CACHE_KEY` specifies the name of the key in your cache to use for storing the timestamp. The default is `CELERY_HEARTBEAT_CACHE_KEY`.

`CELERY_HEARTBEAT_DELAY_THRESHOLD` specifies the number of seconds by which celery can fall behind before the error is logged. The default is 5 minutes.

