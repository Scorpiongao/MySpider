'''
csv读取
'''

import csv

with open('data.csv','r',encoding= 'utf-8') as csvfile:
    #构造rerader对象
    reader = csv.reader(csvfile )
    #遍历每一行内容，每一行是一个列表，包含中文的话指定编码
    for row in reader :
        if len(row)>0:
            print(row)

import pandas as pd

df = pd.read_csv ('data2.csv')
print(df)