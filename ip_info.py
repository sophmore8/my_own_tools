# !/usr/bin/python
# encoding: utf-8

import sys
import re
from bs4 import BeautifulSoup, element
import requests


# get data from web
def ip138_get_data(query):
    url = "http://www.ip138.com/ips138.asp?ip=" + query
    res = requests.get(url)
    if(res.status_code != 200):
        return [{"title": u"网页无法打开"}]

    else:
        sss=res.content
        #print isinstance(res.content, unicode)
        #sss=res.content.decode("utf-8")
        #print sss.decode('gb2312')
        #print sss
        data = []
        res = BeautifulSoup(sss, "html.parser").findAll("table")[2]
        ip = res.h1.string
        match = re.search("(?<=[\s:])(\d+\.){3}\d+$", ip)
        if match:
            print match.group()
            #data.append({"title": ip, "arg": match.group()})
        else:
            print "无效域名或IP"
            #data.append({"title": u"无效的域名或IP"})
        #print res.ul
        if res.ul:
            for li in res.ul:
                print li.string
                #data.append({"title": li.string, "arg": li.string})
        return data

# get data from web
def hao7188_ip_get_data(query):
    data=""
    #url = "http://www.hao7188.com/ip/{0}.html".format(query)
    url="http://www.hao7188.com/ip.asp?mysoip1114={0}".format(query)
    res = requests.get(url)
    if(res.status_code != 200):
        return [{"title": u"网页无法打开"}]
    else:
        res = BeautifulSoup(res.content, "html.parser").select(".so_list_left > li")
        for li in res:
            try:
                data+= li.get_text()
            except :
                continue
    print data

def baidumap_ip_get_data(query):
    data=""
    ak="9w0bGND7tWoDQlbC2IGT3VGxe73rlEUG";
    url="https://api.map.baidu.com/highacciploc/v1?qcip="+query+"&ak="+ak+"&qterm=pc&extensions=1&coord=bd09ll&callback_type=json"

    res = requests.get(url)
    if(res.status_code != 200):
        return [{"title": u"网页无法打开"}]
    else:
        print res.content
    print data



if __name__ == '__main__':
    ip="120.27.183.127"
    print "hao7188查询结果"
    hao7188_ip_get_data(ip)
    print "ip138 查询结果"
    ip138_get_data(ip)
    #baidumap_ip_get_data(ip)


