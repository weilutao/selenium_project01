import logging
import logging.handlers
import datetime

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

rt_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='mignight', interval=1, backupCount=7,
                                                       atTime=datetime.time(0, 0, 0, 0))
rt_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))


