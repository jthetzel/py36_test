# -*- coding: utf-8 -*-


import sys
import logging


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def log_message(message='Hello World'):
    logger.info('Hello World')


if __name__ == '__main__':
    pass
