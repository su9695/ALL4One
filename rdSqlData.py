import json
from pysql2 import  Sql
import re  

sql="SELECT guid,code FROM T_LINE_LINE WHERE CODE='L00391991'"
data3={"parameter":{"BuyerBillGuid":"${guid}","BuyerBillOrderInfoList":[{"OrderGuid":"${guid}","OrderCode":"${code}","OrderType":"9","FXSConfirmType":"0","FXSRemark":""}]}}
s=json.dumps(data3)
sqlData=Sql().oSelect(sql)
'''
背景：接口传参时，参数值可能依赖于之前的数据，此类数据可以通过数据库查询，替换到接口参数中的变量
regex='\${.+?}'  替换 接口str中此类型的数据
re.sub(regex,repl,text)  返回 sql查询结果(dict) 匹配KEY 的value值
'''

def oRpl(text,adict,regex='\${.+?}',start_index=2,end_index=-1):
   if not  isinstance(text,str):
      raise TypeError('text must be str!')
   if not  isinstance(adict,dict):
      raise TypeError('adict must be dict!')
   def rpl(match_obj):
      return adict.get(match_obj.group()[start_index:end_index])
   return re.sub(regex,rpl,text)

x=oRpl(s,sqlData)
print(x)