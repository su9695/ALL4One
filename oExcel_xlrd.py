import xlrd
import os
exc_path=os.path.abspath('pythonLearn/other/testcases.xlsx') 
print(exc_path,type(exc_path)) 
# 打开excle读取数据
data=xlrd.open_workbook(exc_path)
# sheet
sheet=data.sheet_by_index(0)
print(sheet.name) # 第一个sheet的name
sheet=data.sheets()[1]
print(sheet.name,type(sheet))
sheets=data.sheet_names() 
print(sheets,type(sheets)) # ['login', 'lines'] <class 'list'> 返回一个list
for s in sheets:
    print(data.sheet_by_name(s))  # <xlrd.sheet.Sheet object at 0x000000000297CA58>
# row,colocum
rows=data.sheet_by_name('login').nrows
cols=data.sheet_by_index(0).ncols
print(rows,cols)  # 返回总的行数和列数
r=data.sheet_by_name('login').row_values(1) 
print(r,type(r))# 第2行的值,返回list
c=data.sheet_by_index(0).col_values(2)
print(c,type(c))# 第3列的值,返回list
cell_value=data.sheet_by_index(0).cell(0,0).value
print(cell_value) # 第一行第一列的值

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
            # 每个sheet的第一行，即表头行作为dict的key，key是list
            if nrows>1:
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




        
