# -*- coding: utf-8 -*-
# import xdrlib ,sys
import xlrd
import re
import datetime

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
#根据索引获取Excel表格中的数据 参数:file：Excel文件路径 colnameindex：表头列名所在行的所以 ，by_index：表的索引
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    #colnames = table.row_values(colnameindex) #某一行数据
    #colnames = table.row_values(1)
    colnames=table.col_values(5)
    pattern = re.compile(u'(\d月\d+日\d:\d+)-(\d+日\d+:\d+)')
    curTime = datetime.now()
    desTime = curTime.replace(hour=2, minute=0, second=0, microsecond=0)
    #m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
    for col in colnames:
        if col :
            print col
            #print type(col)
            match = pattern.search(col)
            #print col
            if match:

                print match.group(2)
            #print col
def main():
    tables = excel_table_byindex()
    #for row in tables:
        #print row
    #tables = excel_table_byname()
    #for row in tables:
       # print row
if __name__=="__main__":
    main()