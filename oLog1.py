import logging
logger=logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s - %(message)s-%(lineno)d-%(thread)d-%(threadName)s-%(process)d')
# logging中可以选择很多消息级别，如debug、info、warning、error以及critical
logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")