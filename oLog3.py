import logging
import os
import time

class Log(object):
    def __init__(self,logname):
        # 
        self.logger=logging.getLogger(logname)
        self.logger.setLevel(level=logging.INFO)
        # 获取当前时间并格式成'%Y_%m_%d_%H_%M_%S' 的字符串
        self.log_time=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
        # all_log存放路径
        self.all_log_path = os.path.join(os.path.dirname(__file__) + "\\all_log")
        # error_log存放路径
        self.error_log_path=os.path.join(os.path.dirname(__file__) + "\\error_log")
        # 不存在则创建文件夹
        if os.path.exists(self.all_log_path) and  os.path.isdir(self.all_log_path):
            pass
        else:
            os.mkdir(self.all_log_path)
        if os.path.exists(self.error_log_path) and  os.path.isdir(self.error_log_path):
            pass
        else:
            os.mkdir(self.error_log_path)
        #存放日志的txt文件
        self.all_log_txt=os.path.join(self.all_log_path+'/'+self.log_time+'.txt')
        self.error_log_txt=os.path.join(self.error_log_path+'/'+self.log_time+'.txt')
        # 每次调用时判断 handler的list是否为空，不为空则使用之前存在的handler
        if not self.logger.handlers:
            # filehandler
            self.fHandler_all=logging.FileHandler(self.all_log_txt,encoding='utf-8')
            # 控制台handler
            self.cHandler=logging.StreamHandler()
            # 错误日志的handler
            self.fHandler_error=logging.FileHandler(self.error_log_txt,encoding='utf-8')
            # 各handler的日志等级
            self.fHandler_all.setLevel(level=logging.DEBUG)
            self.cHandler.setLevel(level=logging.DEBUG)
            self.fHandler_error.setLevel(level=logging.ERROR)
            # 各日志输出格式
            formatter_all=logging.Formatter('%(asctime)s - %(levelname)s --%(filename)s- %(name)s- %(message)s')
            formatter_error=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s[line:%(lineno)d]-%(name)s--%(message)s')
            #handler设置格式
            self.fHandler_all.setFormatter(formatter_all)
            self.cHandler.setFormatter(formatter_all)
            self.fHandler_error.setFormatter(formatter_error)
            #logger添加handler
            self.logger.addHandler(self.fHandler_all)
            self.logger.addHandler(self.cHandler)
            self.logger.addHandler(self.fHandler_error)
    def getlog(self):
        return self.logger


