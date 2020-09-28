import  datetime
# date  由year年份、month月份及day日期三部分构成
d=datetime.date.today()
print(d) # 返回当前日期
# __format__和strftime等价
print(d.__format__('%Y--%m--%d')) # 格式化日期输出 2020--09--28
print(d.strftime("%Y%m%d")) #  20200928
print(str(d.year)+'_'+str(d.month)+'_'+str(d.day)) # 拼接
d2=datetime.date(1988,3,17)
# 获取两个日期间隔天数
print(d.__sub__(d2))  # datetime.timedelta类型
print(d.__sub__(d2).days) # 正向
print(d.__rsub__(d2).days) # 反向
#iso 返回一个包含三个值的元组，三个值依次为：year年份，week number周数，weekday星期数
print(d2.isocalendar()) # (1988, 11, 4)  第11周，星期4
print(d2.isoformat()) #  1988-03-17

# time类由hour小时、minute分钟、second秒、microsecond毫秒和tzinfo五部分组成
a = datetime.time(12,20,59,899)
print(a)  #  12:20:59.000899 

# datetime 
now=datetime.datetime.now()
print(now) #  返回 2020-09-28 16:36:16.069609

now2=datetime.datetime.strftime(now,'%Y-%m-%d-%H-%M')
print(now2,type(now2))