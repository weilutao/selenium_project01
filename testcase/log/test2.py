import logging

my_format = '%(asctime)s-%(levelname)s-%(message)s'

logging.basicConfig(
    filename='E:/selenium_project01/logs/my.log',
    level=logging.INFO,
    format=my_format
)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')