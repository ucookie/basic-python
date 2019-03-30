import requests
from requests.exceptions import RequestException

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None

# with open('01_页面.html', 'w+') as f:
    # f.write(get_one_page('https://maoyan.com/board/4?offset=0'))

# 由于大多数服务器都会通过请求头中的User-Agent识别客户端使用的操作系统及版本、浏览器及版本等信息，
# 所以爬虫程序也需要加上此信息，以此伪装浏览器；
# 如果不加上很可能别识别出为爬虫，比如当我们不加Headers对知乎进行get请求时
def get_zhihu():
    response = requests.get("https://www.zhihu.com")
    # 状态码
    print(response.status_code)
    # 响应体内容
    print(response.text)

get_zhihu()

'''
400
<html>
<head><title>400 Bad Request</title></head>
<body bgcolor="white">
<center><h1>400 Bad Request</h1></center>
<hr><center>openresty</center>
</body>
</html>
'''