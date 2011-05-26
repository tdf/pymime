#! /usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='PyMIME',
      version='0.2',
      description='A MIME formatter in python',
      author='Alexander Werner',
      author_email='alex@documentfoundation.org',
      url='https://github.com/awerner/pymime',
      packages=['pymime',
                'pymime.plugins',
                'pymime.django_app',
                'pymime.django_app.pymime_attachmentservice',
                'pymime.django_app.pymime_attachmentservice.management',
                'pymime.django_app.pymime_attachmentservice.management.commands',],
      package_data={'pymime': ["*.conf.default"],
                    'pymime.plugins': ["*.conf.default", "footer.en"],
                    'pymime.django_app.pymime_attachmentservice': ["templates/*", "static/*"]},
      scripts=['pymimec', 'pymimed'],
      data_files=[("/etc/pymime", ["pymime/pymime.conf.default",
                                   "pymime/plugins/plugin_attachmentservice.conf.default",
                                   "pymime/plugins/plugin_footer.conf.default",
                                   "pymime/plugins/footer.en"])],
     )
