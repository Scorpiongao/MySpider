# pyquery

## 初始化
- 字符串初始化
    - ```cython
    from pyquery import PyQuery as pq
        html = '这是个html文档'
        doc = pq(html)
        dds = doc('dd')
        ```
- URL初始化
    - `doc = pq(url = 'http://www.baidu.com')`
- 文件初始化
    - `doc = pq(filename = 'demo.html')`
    
## CSS选择器
- tag
- class : `.`
- id : `#`

## 查找节点
- 子节点
    - 嵌套选择
    - find(selector)方法：选择所有符合的节点（子孙节点）
    - children(selector)：所有子节点
- 父节点
    - parent(selector)：父节点
    - parents(selector)：祖先节点
- 兄弟节点
    - siblings(siblings)：兄弟节点
    
## 遍历
- 选择的结果为一个或多个节点时，类型为PyQuery
- items()

## 获取信息
- 获取属性
    - tag.attr('key')
    - tag.attr.key
- 获取文本
    - tag.text()
- 获取节点的html
    - tag.html()
    
## 节点操作(class属性)
- addClass(value)
- removeClass(value)
- tag.attr(key,value)
- tag.text(text_item)
- tag.html(html_item)



