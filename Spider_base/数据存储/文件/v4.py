'''
csv写入
'''

import csv

with open('data.csv','w')as csvfile:
    #初始化写入对象,delimiter=' ' 可改变分隔符，默认逗号分隔
    writer = csv .writer(csvfile )
    #writerow写入每一行
    writer .writerow(['id','name','age'])
    writer .writerow (['10001','Mike',18])
    writer .writerow (['10002','ming',22])
    writer .writerow (['10003','fengzi',10])

    #也可以同时多行写入writes()
    writer .writerows([['10004','Bob',18],['10005','Kings',16],['10006','John',21]])

#字典数据写入,指定encoding='utf-8' 防止中文乱码
with open('data2.csv','w',encoding= 'utf-8')as csvfile :
    #定义字段
    fieldnames = ['id','name','age']
    #初始化字典对象
    writer = csv .DictWriter (csvfile ,fieldnames )
    #写入头部信息
    writer .writeheader()
    #写入字典
    writer .writerow({'id':'1234','name':'张伟','age':12})
    writer.writerow({'id': '123589', 'name': 'bbb', 'age': 16})
    writer.writerow({'id': '11234567', 'name': 'ccc', 'age': 20})

