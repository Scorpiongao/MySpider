'''
输出json
'''

import json

data = [
    {
        "name": "fengzi",
        "gender": "男",
        "birthday": "1899-1-1"
    },
    {
        "name": "哈哈",
        "gender": "男",
        "birthday": "1890-1-1"
    }

]

with open('data2.json','w',encoding= 'utf-8') as f:
    #indent=2表示缩进字符个数,ensure_ascii=False：解决中文乱码问题
    f.write(json .dumps(data,indent= 2,ensure_ascii= False ))