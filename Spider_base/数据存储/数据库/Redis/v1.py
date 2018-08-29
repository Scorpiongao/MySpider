'''
redis连接
'''

from redis import StrictRedis,ConnectionPool


#第一种连接方式
#传入redis地址localhost,端口port=6379,使用的数据库 db1,密码password=None
redis = StrictRedis (host= 'localhost',port= 6379,db=1,password= None )
#字符串操作
#存储键值对name=fengzi
redis .set('name','fengzi')
#返回类型为bytes类型
print(type(redis .get('name') ))
print(redis .get('name').decode() )


#第二种连接方式
pool = ConnectionPool (host='localhost',port=6379,db=1,password=None )

redis = StrictRedis (connection_pool= pool )


l1 = ['ming','love','her']
redis .set('love',l1)
#返回类型为bytes类型
print(type(redis .get('love') ))
print(redis .get('love').decode() )

#列表操作
#添加元素,删除元素
redis.rpush('l1','shadiao')
redis .lpush('l1','hello')

print(redis .lindex('l1',1))



#集合操作
redis.sadd('books','python','flask web','django','chinese')


#有序集合
redis.zadd('grade',100,'Bob',90,'Mike')
print(redis .zcount('grade',0,200) )
redis.zincrby('grade','Mike',-5)



#散列操作
redis.hset('price','cake',66)
redis .hmset('price',{'banana':2,'orange':6})
redis.hgetall('price')