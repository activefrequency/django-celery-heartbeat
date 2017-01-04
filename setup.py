from __future__ import unicode_literals, print_function, absolute_import, division

from setuptools import setup

__version__ = '0.1.0'


description = """
Monitoring app for your celery queues.
"""

setup(
    name = "django-celery-heartbeat",
    url = "https://github.com/activefrequency/django-celery-heartbeat",
    author = "Active Ferquency, LLC",
    author_email = "info@activefrequency.com",
    version=__version__,
    packages = [
        "celery_heartbeat",
    ],
    description = description.strip(),
    zip_safe=False,
    include_package_data = True,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
