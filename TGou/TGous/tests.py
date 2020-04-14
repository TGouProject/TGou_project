from django.test import TestCase
import django
import os
import logging

#配置django运行环境
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstdjango.settings'
django.setup()

def logdemo():
    logger = logging.getLogger('django')
    logger.info('hello logging')
    logger.debug('hello debug log')


if __name__ == '__main__':
    logdemo()
