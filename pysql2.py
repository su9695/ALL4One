import pymssql
import json
class Sql():
    def __init__(self):
        '''
        此处的信息可以从配置表里读取
        '''
        servername='192.168.0.45'
        username='OCTOPUS3.0'
        password='xxxxxxxxxxxxxx'
        dbname='OCTOPUS3.0_TEST_D'
        self.conn=pymssql.connect(server=servername,user=username,password=password,database=dbname)
    def oSelect(self,sql,many=999):
        try:
            cursor=self.conn.cursor(as_dict=True)
            cursor.execute(sql)
            # 固定参数many，若传大于0小于999的数，默认使用fetchmany
            if many>0 and many<999:
                rList=cursor.fetchmany(many) # 返回结果为 [{},{}] ，但字典中的value值都不全是str模式
                '''
                将List中字典的value值均转换为str后再存到strList
                '''
                strList=[]
                for l in rList:
                    strDict={}
                    for k,v in l.items():
                        strDict[k]=str(v)
                    strList.append(strDict)
                return strList
            # 默认many=0时，使用fetchall
            elif many==0:
                rList=cursor.fetchall() # # 返回结果为 [{},{}] ，但字典中的value值都不全是str模式
                strList=[]
                for l in rList:
                    strDict={}
                    for k,v in l.items():
                        strDict[k]=str(v)
                    strList.append(strDict)
                return strList
            else:  # many不传值时，默认使用 fetchone 也是经常使用的查询方式
                rList=cursor.fetchone()
                strDict={}
                for k,v in rList.items():
                    strDict[k]=str(v)
                return strDict  # fetchone 返回的直接是dict，不是[{}] 形式，只需要将value值转换为str即可
            cursor.close()
        except Exception as e:
            print('数据库查询失败',e)
        finally:
            self.conn.close()
    def oUpdate(self,sql):
        try:
            cursor=self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
            print('update操作成功')
        except Exception as e:
            print('数据库update执行失败',e)
            self.conn.rollback()
        finally:
            self.conn.close()
    def oDelete(self,sql):
        try:
            cursor=self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
            print('delete操作成功')
        except Exception as e:
            print('数据库delete执行失败',e)
            self.conn.rollback()
        finally:
            self.conn.close()
