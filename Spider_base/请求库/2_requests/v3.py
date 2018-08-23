'''
二进制数据（图片，音频，视频）
'''


import requests

rsp = requests .get('https://github.com/favicon.ico')

#str类型，图片化为字符串，出现乱码
print(rsp.text )

#二进制数据，bytes类型
print(rsp.content )

#保存图片
with open('github.ico','wb') as f:
    f.write(rsp.content )
    print('图片保存成功！')
