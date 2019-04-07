# 导入lxml库的etree模块
from lxml import etree

with open('01_save.html') as fobj:
    # 调用HTML类进行初始化
    html = etree.HTML(fobj.read())

# step1. 打印电影名
# 粘贴我们copy的xpath，提取电影名 “霸王别姬”
result_bawangbieji = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[1]/a')
#　打印节点标签包含的文本内容
print(result_bawangbieji[0].text)

# step2. 根据规则获取所有电影名
# 提取该页面所有电影名，即选择所有'dd'标签的电影名
result_all = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[1]/a')
# 打印所有提取出的电影名
for one in result_all:
    print(one.text)

# step3. 获取其他信息
item = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
for x in item:
    print('排名', x.xpath('./i/text()'))
    print('封面', x.xpath('./a/img[2]/@data-src'))
    print('电影名', x.xpath('./a/@title'))
    print('主演', x.xpath('.//p[@class = "star"]/text()'))
    print('上映时间', x.xpath('.//p[@class = "releasetime"]/text()'))
    print('评分', x.xpath('.//p[@class = "score"]/i[1]/text()')[0])
    print('评分', x.xpath('.//p[@class = "score"]/i[2]/text()')[0])

# 格式化后
# exit(0)
for x in item:
    print('排名', x.xpath('./i/text()')[0])
    # 去掉url后面的 @160w_220h_1e_1c 则是大图
    print(x.xpath('./a/img[2]/@data-src')[0].split('@')[0])
    print('电影名', x.xpath('./a/@title')[0])
    print('主演', x.xpath('.//p[@class = "star"]/text()')[0].strip().split('：')[1])
    print('上映时间', x.xpath('.//p[@class = "releasetime"]/text()')[0].strip()[5:])
    print('评分', x.xpath('.//p[@class = "score"]/i[1]/text()')[0] + x.xpath('.//p[@class = "score"]/i[2]/text()')[0])
