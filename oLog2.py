import logging,os
from logging import handlers

logger=logging.Logger(__name__)
print(type(logger)) # <class 'logging.Logger'>
# setlevel
logger.setLevel(level=logging.DEBUG)

# handler  FileHandler
all_log_path=exc_path=os.path.abspath('pythonLearn/other/all_log.txt') 
rotating_log_path=os.path.abspath('pythonLearn/other/rotating.txt') # 回滚日志
#FileHandler 需要写入文档路径
handler=logging.FileHandler(all_log_path)
print(type(handler))  # <class 'logging.FileHandler'>
handler.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
print(type(formatter)) # <class 'logging.Formatter'>
handler.setFormatter(formatter)
# handler  StreamHandler
console=logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)
#  RrotatingHandler 回滚日志
rHandler=logging.handlers.RotatingFileHandler(rotating_log_path,maxBytes = 1*1024,backupCount = 3)
rHandler.setLevel(logging.DEBUG)
rHandler.setFormatter(formatter)
# logger 添加handler
logger.addHandler(handler)
logger.addHandler(console)
logger.addHandler(rHandler)

logger.info('-------------start to-------------')
logger.debug('this is a debug')
logger.info('this is a info')
logger.warning('warning  warning')
logger.error('errors to try')
logger.critical('critical critical critical')
logger.fatal('fatalfatalfatalfatalfatalfatalfatalfatalfatal')
try:
    open("sklearn.txt","rb")
except (SystemExit,KeyboardInterrupt):
    raise
except Exception:
    logger.error("Faild to open sklearn.txt from logger.error",exc_info = True)
 
logger.info("Finish")