'''
从qq邮箱导出的联系人中得到好友的qq
'''
import pandas as pd

# df=pd.read_csv ('QQmail.csv',encoding= 'utf-8')
# print(df['E-mail Address'])

import csv
qq_email_list=[]

def get_qq():
    with open('QQmail.csv','r')as csvfile:#打开csv
        reader=csv.reader(csvfile )
        for line in reader :
            if reader .line_num==1:#忽略第一行
                continue
            email=line[2].strip()#将第三列‘电子邮件’读取出来
            qq=email.split('@')[0]
            qq_email_list .append(qq)

    # print(qq_email_list.pop(0) )#删除自己的qq号
    print(list(set(qq_email_list)) )
    print(len(qq_email_list) )
    return qq_email_list
# get_qq()
