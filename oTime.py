import time
'''
 timestamp 格林威治时间   时间戳
 struct_time时间元组，共有九个元素组 
 format time 格式化时间
 timestamp----localtime--->struct-time---->strftime-->format time
  timestamp<----mktime<---struct-time<----strptime<--format time
'''
# 生成timestamp
t1=time.time()
print(t1,type(t1))
# 生成 struct_time
t2=time.localtime(t1) 
print(t2,type(t2)) # <class 'time.struct_time'>  
#  time.struct_time(tm_year=2020, tm_mon=9, tm_mday=28, tm_hour=16, tm_min=2, tm_sec=0, tm_wday=0, tm_yday=272, tm_isdst=0)
t3=time.gmtime(time.time())
print(t3,type(t3))
# 生成format time
t4=time.strftime('%Y-%m-%d',t2)
print(t4)
t5=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
print(t5)