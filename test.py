import json
from pysql2 import  Sql
import re  


data3={"parameter":{"BuyerBillGuid":"${code}","BuyerBillOrderInfoList":[{"OrderGuid":"${guid}","OrderCode":"${code}","OrderType":"9","FXSConfirmType":"0","FXSRemark":""}]}}
s=json.dumps(data3)

sDict={'guid':'CB1157F8-3E8A-4671-BDCE-BDAE045CE7AA','code':'L00391991'}
def multiple_replace(text, adict):  
     def one_xlat(match): 
        return adict.get(match.group()[2:-1])
     return re.sub('\${.+?}',one_xlat, text) 
#  map 展示
print(list(map(re.escape, sDict)))  # 提取 sqlData字典的key,返回一个list  re.escape 可以将字符串中所有可能被解释为正则运算符的字符进行转译
print('|'.join(map(re.escape,sDict))) # 将字典key值组成的list 用|拼接

s2=multiple_replace(s,sDict)
print(s2)