import xlrd
import os
exc_path=os.path.abspath('pythonLearn/other/testcases.xlsx') 

# 读取excel，返回格式为 {{sheet1:[{key:value1},{key:value2}]},{sheet2:[{key1:value1},{key2:value2}]}}
class oExcel(object):
    def __init__(self):
        # exc_path 可以是固定路径的excel
        self.path=exc_path
        self.data=xlrd.open_workbook(self.path)
    def rdExcel(self):
        # 获取所有sheet的名称
        sheets=self.data.sheet_names()
        sheetDict={}
        # 遍历sheet
        for sheet in sheets:
            sheetList=[]
            # 根据sheet名称确定table
            table=self.data.sheet_by_name(sheet) 
            # 总行数
            nrows=table.nrows
            if nrows>1:
               # 每个sheet的第一行，即表头行作为dict的key，key是list
               key=table.row_values(0)
               # 从第一行开始
               for i in range(1,nrows):
                  row_value=table.row_values(i) # 获取每一行的值,list形式
                  # dict(zip)将key和每一行zip，得到一个dict,依次添加进sheetlist中
                  sheetList.append(dict(zip(key,row_value)))
                  i+=1 
               #  {sheetname:[每个sheet内容(包含key和每一行值组成的字典)]}
               sheetDict[sheet]=sheetList
            else:
               sheetDict[sheet]=[]
        return sheetDict
    def getData(self,sheetname):
      # 通过sheet名称获取sheetlist（pytest框架读取的是list)
         return self.rdExcel()[sheetname]

x=oExcel().rdExcel()
print(x)
y=oExcel().getData('Sheet1')
print(y)





        
