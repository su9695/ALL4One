import re
# re.match 从字符串的起始位置匹配一个模式,如果不是起始位置匹配成功的话，match()就返回none。
line ='Cats are smarter than dogs'

matchObj=re.match(r'(.*) are (.*?) .*',line,re.I|re.M)
print(matchObj.group(),type(matchObj))  # <class '_sre.SRE_Match'>
print(matchObj.group(1))
print(matchObj.group(2))

# search 扫描整个字符串并返回第一个成功的匹配
line = "Cats111 are222 smarter333 than444 dogs555"
searchObj=re.search('(\d+)',line,re.I|re.M)
print(searchObj.group())

# sub 替换 re.sub(pattern, repl, string, count=0, flags=0)
'''
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配
'''
phone = "2004-959-559 # 这是一个国外电话号码"

phone1=re.sub(r'#.*$',"",phone) # 将 #后面的用空白代替 2004-959-559
print(phone1)
phone2=re.sub('\D+',"",phone) # 将非数字用空白代替 2004959559
print(phone2)
#repl 是个函数
# 将匹配的数字乘以 2
def double(matched): #<class '_sre.SRE_Match'>matched类型
    '''
    查找s中能被${..}形式找到的str，利用切片找到{ } 找到里面的内容，然后进行计算后替换 输出替换后的内容
    '''
    value = int(matched.group('value')[2:-1]) 
    return str(value * 2)
s = 'A${23}G4HFD${567}'
print(re.sub('(?P<value>\${.+?})', double, s))  


inputStr = "hello 123 world 456"
replacedStr = re.sub("\d+", "222", inputStr)
print(replacedStr)

'''
替换字符串中的数字，各加100,count=2 控制替换的数量
'''
inputStr = "hello 123 world 456,nihao 999"
def addd(match_obj):
    s1=match_obj.group()
    ints=int(s1)
    return str(ints+100)
rrr=re.sub('(\d+)',addd,inputStr,2)
print(rrr)
# re.complie  函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用
rx=re.compile(r'\d+')
inputStr = "one12twothree34four"
m=rx.match(inputStr) # 从头开始，返回None
print(m)
m=rx.match(inputStr,3,10) # 从第3位开始
print(m,m.span()) # <_sre.SRE_Match object; span=(6, 9), match='12'>  m.span()  索引范围
print(m.group(),type(m.group()))
# re.findall  在字符串中找到正则表达式所匹配的所有子串
inputStr='"BuyerBillGuid":"${guid}","BuyerBillOrderInfoList":"${code}"'
inputStr2='"BuyerBillGuid":"{guid}","BuyerBillOrderInfoList":"{code}"'
rx=re.compile('\${.+?}')
outputStr=rx.findall(inputStr)
outputStr2=rx.findall(inputStr2)
print(outputStr,type(outputStr)) # 返回 ['${guid}', '${code}'] <class 'list'>
print(outputStr2,type(outputStr2)) # 返回[] <class 'list'>
# re.finditer 返回一个迭代器
it = re.finditer(r"\d+","12a32bc43jf3") 
print(type(it))  # <class 'callable_iterator'>  需要用循环读出
# re.split  按照能够匹配的子串将字符串分割后返回列表
line = 'aaa bbb ccc;ddd eee, fff'
# 单切
m=re.split(r';',line)
print(m)   # ['aaa   bbb ccc', 'ddd   eee,  fff']
# 两个字符以上切割需要放在 [ ] 中
m=re.split(r'[;,]',line)
print(m)  # ['aaa   bbb ccc', 'ddd   eee', '  fff']  先根据；切割，再根据，切割
# 所有空白字符切割
m=re.split(r'[;,\s]',line)
print(m)  # ['aaa', 'bbb', 'ccc', 'ddd', 'eee', '', 'fff']
# 使用括号捕获分组，默认保留分割符
m=re.split(r'([;])',line)
print(m) #  ['aaa bbb ccc', ';', 'ddd eee, fff']  

#subn   返回(sub(repl, string[, count]), 替换次数)。
p = re.compile(r'(\w+) (\w+)')
s= 'i say, hello world!'
print (p.subn(r'\2 \1', s)) # 返回tuple
m=re.subn(r'(\w+) (\w+)','hi',s)
print(m)