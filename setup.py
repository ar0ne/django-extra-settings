#!/usr/bin/env python

import os
import sys

from setuptools import find_packages, setup

exec(open("extra_settings/version.py").read())

github_url = "https://github.com/fabiocaccamo"
sponsor_url = "https://github.com/sponsors/fabiocaccamo/"
twitter_url = "https://twitter.com/fabiocaccamo"
package_name = "django-extra-settings"
package_url = "{}/{}".format(github_url, package_name)
package_path = os.path.abspath(os.path.dirname(__file__))
long_description_file_path = os.path.join(package_path, "README.md")
long_description_content_type = "text/markdown"
long_description = ""
try:
    with open(long_description_file_path, "r", encoding="utf-8") as f:
        long_description = f.read()
except IOError:
    pass

setup(
    name=package_name,
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    include_package_data=True,
    version=__version__,
    description="easily manage typed extra settings using the django admin.",
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    author="Fabio Caccamo",
    author_email="fabio.caccamo@gmail.com",
    url=package_url,
    download_url="{}/archive/{}.tar.gz".format(package_url, __version__),
    project_urls={
        "Documentation": "{}#readme".format(package_url),
        "Issues": "{}/issues".format(package_url),
        "Funding": sponsor_url,
        "Twitter": twitter_url,
    },
    keywords=[
        "django",
        "admin",
        "extra",
        "settings",
        "options",
        "conf",
        "config",
        "editable",
        "custom",
        "dynamic",
        "typed",
        "constance",
    ],
    requires=[
        "django (>= 2.2)",
    ],
    install_requires=[
        "jsonfield >= 3.0.0",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Build Tools",
    ],
    license="MIT",
    test_suite="runtests.runtests",
)
