from bs4 import BeautifulSoup
import re

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

#解析器：lxml
#实例化 可以自动更正格式
soup = BeautifulSoup (html,'lxml')

#比较好看的格式输出
print(soup.prettify() )

dd = soup.select('dd')
print(dd)

dd = soup.select('dd .board-index')
print(dd)

names = soup.select('dd .name')
for name in names:
    print(name)
    print(name.get_text ())
    print(name.string)

    print(name.a.attrs['href'])
    print(name.a['href'])