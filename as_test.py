# coding=utf-8
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""

from datetime import datetime
import time
import os
import xlrd
import re
import winsound

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
#根据索引获取Excel表格中的数据 参数:file：Excel文件路径 colnameindex：表头列名所在行的所以 ，by_index：表的索引
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=1):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames=table.col_values(5)
    pattern = re.compile(u'(\d+)月(\d+)日(\d+):(\d+)-(?:(\d+)日){0,1}(\d+):(\d+)')
    curTime = datetime.now()
    now_year=curTime.year
    now_day=curTime.day
    #desTime = curTime.replace(hour=2, minute=0, second=0, microsecond=0)
    list2 = []
    for col in colnames:
        if col :
            col = col.replace(" ", "")
            match = pattern.search(col)
            list1=[]
            if match:
                print col
                group5 = now_day
                if match.group(5):
                    group5 = int(match.group(5))
                datetime1=datetime(now_year, int(match.group(1)), int(match.group(2)), int(match.group(3)),int(match.group(4)))
                datetime2=datetime(now_year, int(match.group(1)), group5, int(match.group(6)), int(match.group(7)))
                #写入定时计划
                scheduler.add_job(tick, 'date', run_date=datetime1)  # 在指定的时间，只执行一次
                scheduler.add_job(tick, 'date', run_date=datetime2)  # 在指定的时间，只执行一次
def tick():
    print('Tick! The time is: %s' % datetime.now())
    #播放alert.wav
    winsound.PlaySound("alert.wav", winsound.SND_FILENAME)


if __name__ == '__main__':

    #scheduler.add_job(tick, 'interval', seconds=3)
    excel_table_byindex()
    #每月的最后一天，读取excel表格，写入任务
    scheduler.add_job(excel_table_byindex, 'cron', day='last')
    scheduler.start()    #这里的调度任务是独立的一个线程
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    scheduler.print_jobs()
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)    #其他任务是独立的线程执行
            #print('sleep!')
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')