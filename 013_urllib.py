# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 4:27 PM
# @Author : 张安然
# @File : 'urllib
# @Project : python_space
import urllib.request

# 使用urllib获取网页源码

# 定义url
# url = 'http://jccs.5gchedao.com:18180/#/dashboard'
url = 'http://www.bilibili.com/'
# 模拟浏览器发送请求
# response = urllib.request.urlopen(url)

# 获取二进制数据,decode解码
# content = response.read().decode('utf-8')
# print(content)
# w = open('bilibili.html', 'w')
# w.write(content)
# w.close()

# response = urllib.request.urlopen(url)
# response 有6个方法
# print(response.read())
# print(response.readline())
# print(response.readlines())
# print(response.getcode())
# print(response.geturl())
# print(response.getheaders())

# urllib 下载
# 1下载网页
# url: 路径 ,filename: 文件名字
# urllib.request.urlretrieve(url, 'bilibili.html')
# 2下载图片
# image_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fblog%2F202010%2F05%2F20201005020640_00566.thumb.1000_0.jpeg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673082883&t=1b3e39646b9c5b19f060134550914a15'
# urllib.request.urlretrieve(image_url, 'lisa.jpg')
# 下载视频
# video_url = 'https://vd3.bdstatic.com/mda-jaui7pgvx32bfmph/sc/mda-jaui7pgvx32bfmph.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1670493084-0-0-853fc65cd4d35a8a56e881dcd999b7fa&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=1283931188&vid=12807408348326772677&abtest=104960_2&klogid=1283931188'
# urllib.request.urlretrieve(video_url, 'lisa.mp4')

bilibili_url = 'https://www.bilibili.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=bilibili_url, headers=headers)
b_res = urllib.request.urlopen(request)
b_content = b_res.read().decode('utf-8')
print(b_content)
