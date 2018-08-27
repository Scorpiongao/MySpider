'''
mongodb数据更新
'''

import pymongo
from bson .objectid import  ObjectId
#连接MongoDB，创建一个MongoDB连接对象
client = pymongo .MongoClient (host= 'localhost',port= 27017)

#指定数据库，以下两种方式等价
# db = client .test
db = client ['test']

#指定集合
table = db.students
# table = db['students']

condition = {'name':'Mike'}
student = {
    'id':'15533525',
    'name':'Mike',
    'gender':"male",
    'age':111
}
#默认update一条数据
#可实现去重操作，此时一般condition={'id':data.id}
result = table .update(condition ,{'$set':student},True )
print(result)
print(type(result))


#删除数据
#remove返回字典类型信息
result = table.remove({'name':'John'})
print(result )
print(type(result))

#delete返回对象为DeleteResult，调用属性deleted_count可以查看数据条数
result = table.delete_one({'name':'John'})
print(result.deleted_count )
print(type(result))

result = table.delete_many({'age':{'$gt':16}})
print(result.deleted_count)
print(type(result))

