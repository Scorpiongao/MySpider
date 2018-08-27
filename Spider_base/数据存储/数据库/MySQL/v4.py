'''
mysql查询数据
'''

import pymysql

#声明mysql连接对象db
db = pymysql .connect (host='localhost',user='root',password='ming123',port=3306,db='my_spiders')
#获取mysql操作游标
cursor = db.cursor()

table = 'students'

condition = 'age > 18'

sql = 'select * from {table} where {condition}'.format(table = table ,condition = condition )

try:
    cursor .execute(sql)
    #符合的结果数量
    print('Count: ',cursor .rowcount )

    #拿取一条符合结果
    row = cursor .fetchone()
    print('One: ',row)

    #用while循环获取所有数据
    while row:
        print('row: ',row )
        row = cursor .fetchone()

    #拿到所有结果
    # results = cursor .fetchall()
    # print(results)
    # print('Type of results: ',type(results ))
    #
    # for row in results :
    #     print(row)
except :
    print('Error')