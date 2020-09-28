import os,sys
#OS
print(os.name) # nt  系统名称
print(os.environ)  # 返回环境变量
os.environ.update({'name':'suqiang'}) # 添加环境变量的值 update(**kw)
print(os.getenv('name'),(os.environ['name'])) # 都是获取环境变量name 的value值 suqiangqiang
print(os.getcwd()) # 返回当前的工作目录
#-----目录------
path='../pythonL/pythonLearn/other'
listDir=os.listdir(path)
print(listDir,len(listDir),type(listDir)) # 返回指定目录下所有文件及目录名,[]

print(os.path.isfile((os.path.join(path,'oExcel_openpyxl.py'))))  # 是否为文件
print(os.path.isdir((os.path.join(path,'testtest'))))  # 是否为目录
# path
print(os.path.basename(__file__)) # 返回文件名
print(os.path.dirname(__file__)) # 返回文件所在的目录  ../pythonL/pythonLearn/other
print(os.path.abspath(__file__)) # 返回文件的完整路径名称  ../pythonL/pythonLearn/other/os_sys.py
print(os.path.split(__file__)) # 返回tuple,tupe[0] 为路径，tuple[1]为文件名称
print(os.path.splitext(__file__)) # 返回tuple,tupe[0] 为完整路径(包括文件名)，tuple[1]为当前文件后缀
# 获取当前文件名称，不带后缀
logname=os.path.basename(__file__).split('.')[0] # os_sys
postfix=os.path.basename(__file__).split('.')[1] # py
print(logname,postfix)

# 时间
print(os.path.getatime(__file__))  # 输出最近访问时间
print(os.path.getctime(__file__)) # # 输出文件创建时间
print( os.path.getmtime(__file__) )   # 输出最近修改时间
# 练习 找出目录下最近修改的文件
path='../pythonL/pythonLearn/other'
def getLatestFile(path):
    list_dirs=os.listdir(path)
    list_dirs.sort(key=lambda l: os.path.getmtime(path+'\\'+l))
    file_path=os.path.join(path,list_dirs[-1])
    return file_path
x=getLatestFile(path)
print(x)  
# os.walk 和 os.path.walk 
path_walk='../pythonL/pythonLearn/other/os_walk'
print(os.walk(path_walk)) # <generator object walk at 0x0000000002160D00> 生成器
g=os.walk(path_walk,topdown=False) # topdown False 则先变量字目录，True 先变量根目录
for x in g:
    '''
    # 返回元祖，元祖有三个元素，分别为
     root 所指的是当前正在遍历的这个文件夹的本身的地址
     dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
     files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    '''
    print(x)   #(root,dirs,files)  #('../pythonL/pythonLearn/other/os_walk\\test_walk', [], ['test.txt']) 类似



def VisitDir(arg,dirname,names):
  for filespath in name:
    print (os.path.join(dirname,filespath))
print(os.path.walk(path,VisitDir,()))