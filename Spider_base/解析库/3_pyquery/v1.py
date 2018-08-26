'''
pyquery用法
'''

from pyquery import PyQuery as pq


html = '''
<dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c" alt="霸王别姬" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
        <p class="star">
                主演：张国荣,张丰毅,巩俐
        </p>
<p class="releasetime">上映时间：1993-01-01(中国香港)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/2641" title="罗马假日" class="image-link" data-act="boarditem-click" data-val="{movieId:2641}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p0.meituan.net/movie/54617769d96807e4d81804284ffe2a27239007.jpg@160w_220h_1e_1c" alt="罗马假日" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/2641" title="罗马假日" data-act="boarditem-click" data-val="{movieId:2641}">罗马假日</a></p>
        <p class="star">
                主演：格利高里·派克,奥黛丽·赫本,埃迪·艾伯特
        </p>
<p class="releasetime">上映时间：1953-09-02(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
'''
#实例化
doc = pq (html)
print(doc('dd'))
print(type(doc('dd')))

#子节点
#嵌套
imgs = doc('dd .image-link')
print(imgs)
print(type(imgs))

#find()
dds = doc('dd')
imgs = dds('.image-link')
print(imgs)
print(type(imgs ))

imgs = dds.find('.image-link')
print(imgs)
print(type(imgs ))

imgs = dds.children('.image-link')
print(imgs)
print(type(imgs ))

#父节点
print(imgs.parent()  )
#祖先节点
print(imgs .parents())
print(imgs .parents().text() )

#兄弟节点
imgs = imgs('.board-img')
print(imgs)
print(imgs .siblings() )

#遍历
for i in imgs.siblings().items() :
    print(i,type(i))
    print(i.attr('src') )
    print(i.attr.src)