# _*_ coding : utf-8 _*_
# @Time: 2022/12/9 10:10 AM
# @Author : 张安然
# @File : '019_urllib_异常处理
# @Project : python_space
import urllib.request
import urllib.error
if __name__ == '__main__':
    try:
        url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
        headers = {
            'X-Requested-With': "XMLHttpRequest",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        print(response)
    except urllib.error.HTTPError:
        print('请求出现错误!')
    except urllib.error.URLError:
        print('请求地址可能不对!')
