# MongoDB

- 非关系型数据库
- 集合代替表，使用文档代替记录
- 特点：减少了表的数量，却增加了数据重复（也提升了查询速度）
- python支持PyMongo
- 命令行启动MongoDB服务
    - `cd D:\MongoDB\Server\bin`
    - `mongod --dbpath D:\MongoDB\Server\data\db`

## 1. 连接数据库与集合
    ```
    import pymongo
    #连接MongoDB，创建一个MongoDB连接对象
    client = pymongo .MongoClient (host= 'localhost',port= 27017)

    #指定数据库，以下两种方式等价
    # db = client .test
    db = client ['test']

    #指定集合
    table = db.students
    # table = db['students']
    ```

## 2. 插入数据
- 一条数据
    - insert(data)
    - insert_one(data)
- 多条数据
    - insert([data1,data2...])
    - insert_many([data1,data2...])
- 案例v1

## 查询数据
- find_one(condition) : 返回一条符合的结果
- find(condition) : 返回生成器对象
- 比较符号
    ```
    符号     含义          例子
    $lt      小于         {'age':{'$lt':20}}
    $gt      大于         {'age':{'$gt':20}}
    $lte     小于等于     {'age':{'$lte':20}}
    $gte     大于等于     {'age':{'$gte':20}}
    $ne     不等于        {'age':{'$ne':20}}
    $in     在范围内      {'age':{'$in':[20,30]}}
    $nin    不在范围内     {'age':{'$nin':[20,30]}}
    ```
- 功能符号
    ```
    符号       含义                  例子
    $regex   正则表达式匹配         {'name':{'$regex':'^M.*'}}
    $exists   属性是否存在          {'age':{'$exists':True}}
    $type     类型判断              {'age':{'$type':'int'}}
    $mod    数字模操作              {'age':{'$mod':[5,0]}}  年龄模5余0
    $text     文本查询               {'$text':{'$search':'ming'}} 
    $where     高级查询              {'$where':'obj.fans_count==obj_follows_count'}
    
    ```
- 更详细用法，前往[mongodb官网](https://docs.mongodb.com/manual/reference/operator/query/)
- 案列v2

## 3. 计数、排序
- count()
    ```
    count = table .find(condition).count()
    print('count: ',count )```

- sort('age',pymongo.ASCENDING)
    ```
    results = table .find ().sort('name',pymongo .ASCENDING )
    print([result ['name'] for result in results ])
    ```
- 偏移与限制
    ```cython
    #偏移skip(number)忽略前几个数，从第number+1个元素开始,限制结果数量limit()
    results = table .find ().sort('name',pymongo .ASCENDING ).skip(2)
    print([result ['name'] for result in results ])

    #限制结果数量limit(),截取前几个结果
    results = table .find ().sort('name',pymongo .ASCENDING ).skip(2).limit(4)
    print([result ['name'] for result in results ])
    ```
- 案例v2

## 4. 更新数据
- update_one()
- update_many()
- 可实现数据去重操作
    - `result = table.update(condition,{'$set':data},True)`
- 案列v3

## 5. 删除数据
- remove(condition)
- delete_one(condition)
- delete_many(condition)
- 案列v3