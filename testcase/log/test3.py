# import logging
# import logging.handlers
# import datetime
#
# # 初始化过程
# logger = logging.getLogger('mylogger')
# logger.setLevel(logging.DEBUG)
#
# rf_handler = logging.handlers.TimedRotatingFileHandler('C:/python3.7.0/selenium_project01/logs/all.log', when='midnight', backupCount=7, atTime=datetime.time(0, 0, 0, 0))
# rf_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
#
# f_handler = logging.FileHandler('C:/python3.7.0/selenium_project01/logs/error.log')
# f_handler.setLevel(logging.ERROR)
# f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
#
# logger.addHandler(rf_handler)
# logger.addHandler(f_handler)


from util import util

logger = util.get_logger()

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

