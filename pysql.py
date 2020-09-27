import pymssql

host='192.168.0.45'
username='OCTOPUS3.0'
password='xxxxxxxxxxxx'
dbname='OCTOPUS3.0_TEST_D'

conn=pymssql.connect(server=host,user=username,password=password,database=dbname)
#-----------select--------------
# 返回一条查询记录多字段记录： tuple
cursor=conn.cursor()
sql="SELECT * FROM T_LINE_LINE WHERE CODE='L00391991'"
cursor.execute(sql)
row = cursor.fetchone()
print(row,type(row)) # <class 'tuple'>
for r in row:
    print(r,type(r))
# 返回一个字段记录 tuple
cursor=conn.cursor()
sql="SELECT code FROM T_LINE_LINE WHERE CODE='L00391991'"
cursor.execute(sql)
row = cursor.fetchone()[0] # 只有一个字段，即tuple的第一个元素
print(row,type(row))  # # <class 'tuple'>
# 返回一个字典
cursor=conn.cursor(as_dict=True)
sql="SELECT guid,code FROM T_LINE_LINE WHERE CODE='L00391991'"
cursor.execute(sql)
row=cursor.fetchone()
print(row,type(row))  # <class 'dict'>
cursor.close()
# 返回所有查询记录
sql='select * from  T_LINE_Line where CreateDate>(select CONVERT(varchar(10),GETDATE(),120))'
cursor=conn.cursor(as_dict=True)
cursor.execute(sql)
row=cursor.fetchall()
print(row,type(row)) #  <class 'list'>  多条记录组成的list 若as_dict=True，则格式为[{}{}]
cursor.close()
# 返回指定条数的记录
sql='select * from  T_LINE_Line where CreateDate>(select CONVERT(varchar(10),GETDATE(),120))  order by CreateDate asc'
cursor=conn.cursor(as_dict=True)
cursor.execute(sql)
row=cursor.fetchmany(1)  # 默认返回查询结果的第一条，list 若as_dict=True，则格式为[{}{}]
print(row,type(row))
cursor.close()
#----------update-----
sql="update T_LINE_Line  set  name='葫芦娃葫芦娃 一棵藤上七朵花2'  where code='L00391992'"
cursor=conn.cursor()
cursor.execute(sql)
conn.commit()
cursor.close()
# ---------delete-----
sql="delete from  T_LINE_Line where code='L00391992'"
cursor=conn.cursor()
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()