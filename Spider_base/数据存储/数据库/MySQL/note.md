# MySQL
- 关系型数据库
- 由行、列组成的表，每一列是一个字段，每一行是一条记录
- python3支持PyMySQL
- 安装：pip install pymysql

## 1. 创建数据库和表
- 案列v1
- 创建数据库
    ```cython
    import pymysql 
    # #声明mysql连接对象db
    db = pymysql .connect (host='localhost',user='root',password='ming123',port=3306)
    # #获取mysql操作游标
    cursor = db.cursor()
    # #执行语句：查看版本号
    cursor .execute('SELECT VERSION()')
    # #获得第一条语句结果
    data = cursor .fetchone()
    print('Database version: ',data)
    #
    # #mysql语句：创建数据库
    sql = 'create database my_spiders DEFAULT CHARACTER SET utf8'
    # #执行mysql的语句sql
    cursor .execute(sql)
    # #关闭连接
    db.close()
    ```

- 创建表
    ```
    #创建表
    #声明mysql连接对象db
    db = pymysql .connect (host='localhost',user='root',password='ming123',port=3306,db='my_spiders')
    #获取mysql操作游标
    cursor = db.cursor()

    sql = 'create table if not exists students(id VARCHAR (255) NOT NULL ,name VARCHAR (255)NOT NULL ,age INT NOT NULL ,PRIMARY KEY (id))'

    cursor .execute(sql)
    print('table students has been created.')
    db.close()
    ```

## 插入数据
- `insert into table_name(id,name,age...) values (value1,v2,v3..)`
- 案例v2
- 对数据库进行的更改操作都必须为一个事务，标准写法为
```cython
try:
    cursor .execute(sql,(id,name,age))
    db.commit() 
except :
    db.rollback()
```

## 更新数据
- 案例v3
```cython
import pymysql

#声明mysql连接对象db
db = pymysql .connect (host='localhost',user='root',password='ming123',port=3306,db='my_spiders')
#获取mysql操作游标
cursor = db.cursor()

table = 'students'

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
```

## 删除数据
```cython
table = 'students'
condition = 'age > 22'

sql = 'delete from {table} where {condition}'.format(table = table ,condition = condition ) 
try:
    cursor.execute(sql)
    db.commit()
    print('successful')
except :
    print('failed')
    db.rollback()
db.close()  
```

## 查询数据
- 案列v4
```cython
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
```