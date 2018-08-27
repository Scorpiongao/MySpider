'''
MongoDB数据库操作
'''

import pymongo
#连接MongoDB，创建一个MongoDB连接对象
client = pymongo .MongoClient (host= 'localhost',port= 27017)

#指定数据库，以下两种方式等价
# db = client .test
db = client ['test']

#指定集合
table = db.students
# table = db['students']

#插入数据
student1 = {
    'id':'12222221',
    'name':'John',
    'gender':"male",
    'age':21
}

student2 = {
    'id':'15555525',
    'name':'Mike',
    'gender':"male",
    'age':18
}
student3 = {
    'id':'22222222',
    'name':'Lisa',
    'gender':"female",
    'age':16
}

# result = table .insert(student1)
#mongodb中，每条数据都有一个_id属性来唯一标识，insert()返回结果为_id值
# print(result)

#可以使用insert_one()方法
result = table .insert_one(student1)
#mongodb中，每条数据都有一个_id属性来唯一标识，insert()返回结果为_id值
print(result )#返回为InsertManyResult对象
print(result.inserted_id)#调用insert_id属性查看_id

#同时插入多条数据，以列表形式插入
# result = table.insert([student2 ,student3 ])
# print(result)

result = table.insert_many([student2 ,student3 ])
print(result)
print(result .inserted_ids)
