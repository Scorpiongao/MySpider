'''
mongodb 数据查询
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

result = table .find_one({'name':'John'})
print(result )
print(type(result))

result = table .find_one({'_id':ObjectId('5b842123321c1507b4f99b4b')})
print(result )
print(type(result))

result = table .find({'age':{'$gt':17}})
print(result)
print(type(result ))
for item in result :
    print(item)
    print(type(item ))

result = table .find({'name':{'$regex':r'^M.*'}})
print(result)
print(type(result ))
#计数
count = table .find({'name':{'$regex':r'^M.*'}}).count()
print('count: ',count )
for item in result :
    print(item)
    print(type(item ))

#排序
count = table .find().count()
print('count: ',count )
results = table .find ().sort('name',pymongo .ASCENDING )
print([result ['name'] for result in results ])

#偏移skip(number)忽略前几个数，从第number+1个元素开始,限制结果数量limit()
results = table .find ().sort('name',pymongo .ASCENDING ).skip(2)
print([result ['name'] for result in results ])

#限制结果数量limit(),截取前几个结果
results = table .find ().sort('name',pymongo .ASCENDING ).skip(2).limit(4)
print([result ['name'] for result in results ])