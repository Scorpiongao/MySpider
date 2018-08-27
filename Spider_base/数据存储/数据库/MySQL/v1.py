'''
创建数据库与表
'''

import pymysql

# #声明mysql连接对象db
db = pymysql .connect (host='localhost',user='root',password='ming123',port=3306)
# #获取mysql操作游标
cursor = db.cursor()
# #执行语句：查看版本号
cursor .execute('SELECT VERSION()')
# #获得第一条语句结果
data = cursor .fetchone()
print('Database version: ',data)
#
# #mysql语句：创建数据库
sql = 'create database my_spiders DEFAULT CHARACTER SET utf8'
# #执行mysql的语句sql
cursor .execute(sql)
#
# #关闭连接
db.close()



#创建表
#声明mysql连接对象db
db = pymysql .connect (host='localhost',user='root',password='ming123',port=3306,db='my_spiders')
#获取mysql操作游标
cursor = db.cursor()

sql = 'create table if not exists students(id VARCHAR (255) NOT NULL ,name VARCHAR (255)NOT NULL ,age INT NOT NULL ,PRIMARY KEY (id))'

cursor .execute(sql)
print('table students has been created.')
db.close()