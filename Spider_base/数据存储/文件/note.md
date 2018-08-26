# 数据存储

## TXT文本存储

- 第一种方式
    - `file = open('zhihu.txt','a',encoding= 'utf-8')`
    ```
    file = open('zhihu.txt','a',encoding= 'utf-8')
    file .write('\n'.join([question ,author ,answer ]) )
    file.write('\n'+ '='*50+'\n')
    file .close()
    ```
    - 打开方式
        - r : 只读
        - rb : 二进制文件读取
        - r+ : 以二进制读写文件
        - w : 写入方式打开，已存在则覆盖
        - wb : 以二进制写入，已存在则覆盖
        - w+ : 读写方式打开，已存在则覆盖
        - wb+ : 二进制文件读写方式打开，已存在则覆盖
        - a : 追加方式写入
        - ab : 二进制文件追加写入
        - a+ : 读写方式追加
        - ab+ : 二进制文件读写方式追加
    - 案例
- 第二种方式(with)
    ```
    with open('zhihu.txt','a',encoding='utf-8') as file:
        file .write('\n'.join([question ,author ,answer ]) )
        file.write('\n'+ '='*50+'\n')
    ```
    
## JSON
- dumps() : 序列化，python数据（dict）转化为Json对象
- loads() : 反序列化，Json对象转化为python数据（dict,list）

- 读取
    - 案例v2
    - JSON数据需要用双引号""包围，单引号''会报错，json.decoder.JSONDecodeError
- 写入
    - 案例v3
    ```
    with open('data2.json','w',encoding= 'utf-8') as f:
    #indent=2表示缩进字符个数,ensure_ascii=False：解决中文乱码问题,需要指定编码格式
    f.write(json .dumps(data,indent= 2,ensure_ascii= False ))
    ```
## CSV
- Comma Separated Values （逗号分隔符值）
- 读取
    - 案例v4
    - 含中文的要指定编码，防止乱码，`encoding='utf-8'`
    - pandas.to_csv()
    ```
    zu_fang=pandas .DataFrame (data)
    zu_fang .to_csv ('zu_fang.csv',encoding= 'utf_8_sig')
    zu_fang .info()
    zu_fang .head(5)
    ```
- 写入
    - 案列v5
    - pandas.read_csv('filename')
    - ```cython
     import pandas as pd
     df = pd.read_csv ('data.csv')
     print(df) 
     ```   