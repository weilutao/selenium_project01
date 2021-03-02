import logging

my_format = '%(asctime)s'

logging.basicConfig(
    filename = 'logs/my.log',
    level = logging.INFO,
    format = my_format
)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')