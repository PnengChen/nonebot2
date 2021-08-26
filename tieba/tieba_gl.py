import requests, json
import requests
import urllib.parse
import re
from lxml import etree  # 导入xpath
from urllib import request


async def get_tieba_data(msg):
    key = urllib.parse.quote(msg)
    theme = "&un=&rn=10&pn=0&sd=&ed=&sm=1&only_thread=1"
    ur = "https://tieba.baidu.com/f/search/res?ie=utf-8&kw=%E5%A5%A5%E5%A5%87%E4%BC%A0%E8%AF%B4&qw="

    # print(key)
    url = ur + key + theme
    # print(url)
    r = requests.get(url).text
    # print(r)
    # 获取攻略链接
    matches = re.findall('<div class="s_post"><span class="p_title"><a data-tid=(.*?) data-fid=(.*?) class="bluelink" href="(.*?)" class="bluelink" target="_blank" >',r)

    # print(matches)
    ur = []
    for i in matches:
        ur.append('https://tieba.baidu.com/' + i[2])

    # print(ur)
    # 定义树形结构解析器
    selector = etree.HTML(r, parser=None, base_url=None)
    detail_text = selector.xpath("/html/body/div[@class='wrap1']/div[@class='wrap2']/div[@class='s_container clearfix']/div[@class='s_main']/div[@class='s_post_list']/div[@class='s_post']")

    inf = []
    for j in detail_text:
        z = j.xpath('string(.)').strip()
        x = z.split("    ")
        mytest = [i for i in x if i != '']
        inf.append(mytest)

    # inf为攻略标题，时间
    infor = ''
    if inf != []:
        for n in range(len(ur)):
            x = inf[n]
            infor = infor + x[0] + ' ' + '时间: ' + x[-1] + '\n' + ur[n] + '\n'
    else:
        for n in range(len(ur)):
            infor = infor + ur[n] + '\n'
    return infor


