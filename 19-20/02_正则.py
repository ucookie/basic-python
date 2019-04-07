import re

# 1. 简单匹配
# 待匹配文本
h1 = '<H1>Chapter 3.2.1 - 介绍正则表达式</H1>'
# 将正则字符串编译成正则表达式对象，方便在后面的匹配中复用
pat = re.compile('<H1>(.*?)</H1>', re.S)
# re.search 扫描整个字符串并返回第一个成功的匹配
result = re.search(pat, h1)
# 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
# print(result.group(0))
# 匹配的第一个括号内的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
# print(result.group(1))

# 2. 匹配字符串
s = '''                <dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
      <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c" alt="霸王别姬" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
        <p class="star">
                主演：张国荣,张丰毅,巩俐
        </p>
<p class="releasetime">上映时间：1993-01-01</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>
    </div>

      </div>
    </div>

                </dd>'''
# step1 匹配排行
# robj = re.search('<dd>.*?board-index.*?>(\d+)', s)
# step2 匹配换行符
# robj = re.search('<dd>.*?board-index.*?>(\d+)', s, re.S)
# step3 匹配链接
# robj = re.search('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?', s, re.S)
# step4 匹配电影名
# robj = re.search('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>', s, re.S)
# step5 完整匹配
# robj = re.search('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',
#                  s,
#                  re.S)

# print(robj.groups())

# 3. 匹配全文
with open('01_save.html') as fobj:
    data = fobj.read()
    # r表示字符串不转义
    # 需要使用 re.S 参数用来匹配换行符
    pattern = re.compile(
        r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',
        re.S)
    # re.S表示匹配任意字符，如果不加.无法匹配换行符
    items = re.findall(pattern, data)
    for item in items:
        print(item)
