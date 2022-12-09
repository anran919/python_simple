# _*_ coding : utf-8 _*_
# @Time: 2022/12/9 9:32 PM
# @Author : 张安然
# @File : '028_jsonpath_淘票票影院城市获取
# @Project : python_space

import urllib.request
import urllib.parse
import jsonpath
import json

if __name__ == '__main__':
    headers = {
        'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
        'bx-v': '2.2.3',
        'cookie': 'cna=rOnTG6ylLi4CAa8AjCEvyZG+; _m_h5_tk=ee6eb7b788c060ef6774abc33af36d5e_1670319607473; _m_h5_tk_enc=020913df971cd9a27f2026dbabcfb35d; t=bf5732c1d9d67897d4000be6cd217142; cookie2=17c584c58957ac39508e05304614035f; v=0; _tb_token_=335b66e3aee63; xlly_s=1; tb_city=440300; tb_cityName="ye7b2g=="; tfstk=cCsOByguPJHTQyVDYhUH3ATl0MwhZDVvOAOmDgeMONqzqEoAiXIl2BUb5KOy6JC..; isg=BIyMWUzjA0za9RctU169epZZXey-xTBvSnqlf-ZOMTfacS17DtMe_7oHEXHJOWjH; l=fBEoPo-lTooqaFUvBO5Clurza77TNQdb8sPzaNbMiIEGa61R9FTuiNCFnGmXWdtj_TfcTetrNY84xdEXlpzZwgiMW_NUnq5H_cp6-bpU-L5..',
        'referer': 'https://dianying.taobao.com/cinemaList.htm?spm=a1z21.6646277.city.5.249f4523r03EQp&n_s=new&city=440300',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    search = {
        'activityId': '',
        '_ksTS': '1670592684830_55',
        'jsoncallback': 'jsonp56',
        'action': 'cityAction',
        'n_s': 'new',
        'event_submit_doGetAllRegion': 'true'
    }
    url = 'https://dianying.taobao.com/cityAction.json?' + urllib.parse.urlencode(search)
    print(url)
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    content = content.split('(')[1].split(')')[0]
    # 保存到文件
    # with open('./json/淘票票城市数据.json', 'w', encoding='utf-8') as fp:
    #     fp.write(content)
    obj = json.load(open('./json/淘票票城市数据.json', 'r'))
    # city_list = jsonpath.jsonpath(obj, '$.returnValue[*][*].regionName')
    city_list = jsonpath.jsonpath(obj, '$..regionName')
    print(city_list)
