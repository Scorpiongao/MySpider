'''
mysql更新数据
'''

import pymysql

#声明mysql连接对象db
db = pymysql .connect (host='localhost',user='root',password='ming123',port=3306,db='my_spiders')
#获取mysql操作游标
cursor = db.cursor()

table = 'students'

# sql = 'update {table} set name=%s WHERE age=%s'.format(table =table )
# try:
#     cursor.execute(sql,('ming',20))
#     db.commit()
#     print('Successful')
# except :
#     db.rollback()
#     print('Failed')
#
# db.close()


#去重：数据存在则更新数据，不存在则插入
data = {
    'id':'12341234',
    'name':'MIKE',
    'age':27,
    'gender':'male'
}

keys = ','.join(data.keys() )
values = ','.join(['%s']*len(data) )
#主键存在则执行更新操作
sql = 'insert into {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table =table ,keys =keys ,values =values )
update = ','.join([" {key}=%s".format(key=key) for key in data ])
sql += update
try:
    if cursor .execute(sql ,tuple (data.values() )*2) :
        print('Successful')
        db.commit()
except :
    print('Failed')
    db.rollback()
db.close()