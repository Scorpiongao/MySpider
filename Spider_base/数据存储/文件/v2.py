'''
JSON数据 读取
'''

import json

str = '''
[{
    "name":"ming",
    "gender":"male",
    "birthday":"1900-1-1"
    },
    {
    "name":"fengzi",
    "gender":"male",
    "birthday":"1899-1-1"
    }
]
'''

print(type(str))

#反序化为python数据类型
data = json .loads(str)
print(data)
print(type(data))

#获取元素属性
for i in data:
    print(i)
    print(i['name'])
    print(i.get('name'))


#文件读取
with open('data.json','r') as f:
    str = f.read()
    print(str,type(str))
    data =json.loads(str)
    print(data)
    print(type(data))