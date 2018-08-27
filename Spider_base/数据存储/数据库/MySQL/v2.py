'''
mysql插入数据
'''

import pymysql

id = '123456'
name = 'Bob'
age = 18

#声明mysql连接对象db
db = pymysql .connect (host='localhost',user='root',password='ming123',port=3306,db='my_spiders')
#获取mysql操作游标
cursor = db.cursor()

#这种不便动态数据更改
# sql = 'insert into students(id,name,age) VALUES (%s,%s,%s)'
#
# try:
#     cursor .execute(sql,(id,name,age))
#     db.commit()
#     print('insert into students successfully!')
# except :
#     db.rollback()
#     print('error')
#
# db.close()


#可动态更改数据结构
#先改表字段

table = 'students'
#删除旧表
sql = 'drop table {table}'.format(table =table )
cursor .execute(sql)
print('table dropped')

sql = 'create table if not exists {table}(id VARCHAR (255) NOT NULL ,name VARCHAR (255)NOT NULL ,age INT NOT NULL ,gender VARCHAR (64) NOT NULL ,PRIMARY KEY (id))'.format(table=table)

cursor .execute(sql)
print('table created')

data = {
    'id':'12345678',
    'name':'john',
    'age':20,
    'gender':'male'
}

keys = ','.join(data.keys() )
values = ','.join(['%s']*len(data) )
sql = 'insert into {table}({keys}) VALUES ({values})'.format(table =table ,keys =keys ,values =values )

try:
    if cursor .execute(sql ,tuple (data.values() )) :
        print('Successful')
        db.commit()
except :
    print('Failed')
    db.rollback()
db.close()