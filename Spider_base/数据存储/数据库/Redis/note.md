# Redis
- 基于内存的高效的键值型非关系型数据库，存取效率极高，支持多种存储数据结构
### 1. 连接redis数据库
    - 案列v1
    - 方式一
    `redis = StrictRedis (host= 'localhost',port= 6379,db=1,password= None )`
    - 方式二
    ```
    #传入redis地址localhost,端口port=6379,使用的数据库 db1,密码password=None
    pool = ConnectionPool (host='localhost',port=6379,db=1,password=None )

    redis = StrictRedis (connection_pool= pool )

    ```
    
### 2. 键操作
```
方法                  作用                            示例
exists(key)        判断一个键是否存在             redis.exists('name')
delete(key)        删除一个键                    redis.delete('name')
type(key)          判断键类型                    redis.type('name')
keys(pattern)      获取所有符合规则的键            redis.keys('^n.*')
randomkey()        获取随机的一个键                redis.randomkey()
rename(src,dst)    重命名键                      redis.rename('name','nickname')
dbsize()           获取当前数据库中键的数目        redis.dbsize()
expire(key,time)  设定键的过期时间（秒）           redis.expire('name',3)
ttl(name)         获取键的过期时间（-1表示永久不过期） redis.ttl('name')
move(key,db)      将键移动到其他数据库               redis.move('name',2)
flushdb()          删除当前数据库中所有键          redis.flushdb()
flushall()         删除所有数据库中所有键          redis.flushall()
```

### 3. 字符串操作
- redis支持最基本的键值对形式存储，用法如下
```

set(key,value)              给键赋值                     redis.set('name','ming')
get(key)                    获取键值                     redis.get('name')
getset(key,value)          给键赋值并获取键值             redis.getset('name','ming')
mget(keys,*args)           获取多个键的值(list)          redis.mget(['name','nickname'])
mset(mapping)              批量赋值(dict)               redis.mset({'name1':'ming','name2':'fengzi'})
append(key,value)          键值后面追加value             redis.append('name','sb')
substr(key,start,end=-1)  截取键的string的一部分          redis.substr('name',1,4)
getrange(key,start,end)   截取键值value的一部分           redis.getrange('name',1,4)
```
### 4. 列表操作
- 当key的value对象类型为列表时
```
方法                          作用                          示例
rpush(key,*values)        列表末端添加元素              redis.rpush('l1',1,2,3)
lpush(key,*value)         XXX头部                      redis.lpush('l1',1,2,3)
llen(key)                 列表长度                     redis.llen('l1')
lrange(key,start,end)    返回列表中start-end之间元素   redis.lrange('l1',2,4)
lindex(key,index)         返回列表索引的元素            redis.lindex('l1',1)
lset(key,index,value)     给列表索引元素赋值            redis.lset('l1',1,'aa')
lpop(key)                 删除列表中首个元素            redis.lpop('l1')
rpop(key)                 XXXX最后                    redis.rpop('l1')
```

### 5. 集合操作
- 当key的value对象类型为集合（集合元素不重复）时
- 方法
    - sadd(key,*value)
    - spop(key)
    - sinter(keys,*value) : 集合的交集
    - sinterstore(dest,keys,*value) : 交集存储到dest键中
    - sunion(keys,*value) : 并集
    - sunionstore(dest,keys,*value) : 存储并集
    - sdiff(keys,*value) : 差集
    - sdiffstore(dest,keys,*value) : 存储差集
    - smembers(key) : 返回键的所有元素
    - srandmember(key) : 随机返回一个元素

### 6. 有序集合
- 有序集合比集合多了一个分数字段，利用它可以对集合中的数据进行排序
```
     方法                                                                 作用                        示例
zadd(key,*args,**kwarg)                                               添加元素，分数用于排序        redis.zadd('grade',100,'Bob',90,'Mike')
zrem(key,*value)                                                        删除                     redis.zrem('grade')
zincrby(key,value,amount=1)                                           键值分数变化                redis.zincrby('grade','Mike',-5)
zrank(key,value)                                                      返回value的排名（小-->大）   redis.zrank('grade','Bob')
zrevrank(key,value)                                                   倒序排名                   redis.zrevrank('grade','Bob')
zcount(key,min,max)                                                   返回分数区间的数量          redis.zcount('grade',80,95)
zcard(key)                                                            元素数量                   redis.zcard('grade')
zrevange(key,start,end,withscorres=Flase)                             倒序索引截取                redis.zrevrange('grade',1,3)
zrangebyscore(key,min,max.start=None,end=None,withscores=Flase)       给定区间元素                redis.zrangebyscore('grade',80,95)
```

### 7. 散列操作
- 散列表的数据结构，key的value为为一个散列表，表内存储了各个键值对
- 用法如下
```
     方法                       作用                            示例
hset(key,key1,value)        向key键添加键值对key1与value     redis.hset('price','cake',66)
hsetnx(key,key1,value)      key1不存在时添加value            redis.hsetnx('price','cake',66)
hget(key,key1)              获取散列列表中键值                redis.hget('price','cake')
hmget(key,keys,*args)        获取散列中多个键值               redis.hmget('price',['cake','orange'])
hmset(key,mapping)          批量添加散列映射                  redis.hmset({'banana':2,'pear':6})
hexists(key,key1)           判断是否存在                      redis.hexists('price','pear')
hdel(key,*keys)               删除                           redis.hdel('price','banana')
hlen(key)                    长度                            redis.hlen('price')
hkeys(key)                   获取键名                         redis.hkeys('price')
hvals(key)                   获取键值                         redis.hvals('price')
hgetall(key)                 获取键值对                       redis.hgettall('price')

```