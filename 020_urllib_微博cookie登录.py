# _*_ coding : utf-8 _*_
# @Time: 2022/12/9 10:51 AM
# @Author : 张安然
# @File : '020_urllib_微博cookie登录
# @Project : python_space
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'cookie': 'SUB=_2AkMU1SgTf8NxqwJRmPAXxWvhaoRyzgvEieKiidnIJRMxHRl-yT9kqhIstRB6P1UG_KW5xSFfFYdQYjXee_2hbmBRDAyb; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWKU7HvXKMKMCBpnWf61nLK; login_sid_t=77843caef22337c0578a75d8424bbc0a; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=7121590461997.704.1669965607472; SINAGLOBAL=7121590461997.704.1669965607472; ULV=1669965607475:1:1:1:7121590461997.704.1669965607472:; XSRF-TOKEN=2XpABkvVgK6AJTM_gKxhkmie; WBPSESS=durPiJxsbzq5XDaI2wW0N6DfDFQ5pnRqMJocrEAb9AiOLVJGUwGyq-88kVYSZ84hkFCayPCkiQgCTojrtXq16PkqeXDKu6D33Qk-7JGRQmvv8Rkof2N17U45o_VI6U3PeJ6ZwZk4nCicAeWyF_6Dabzrb_CXPzNl6L8I1AcrMb0=',
    'referer': 'https://weibo.com/',
}
url = 'https://weibo.com/ajax/profile/info?uid=1594296825'
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
