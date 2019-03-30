import requests
# 导入lxml库的etree模块
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
url = 'http://maoyan.com/board/4'
response = requests.get(url, headers=headers)
html = response.text
# 调用HTML类进行初始化
html = etree.HTML(html)
# 粘贴我们copy的xpath，提取电影名 “霸王别姬”
result_bawangbieji = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[1]/a')
#　打印节点标签包含的文本内容
print(result_bawangbieji[0].text)
# 提取该页面所有电影名，即选择所有'dd'标签的电影名
result_all = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[1]/a')
#　打印所有提取出的电影名
print('该页面全部电影名：')
for one in result_all:
    print(one.text)
