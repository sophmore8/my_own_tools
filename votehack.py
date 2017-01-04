# -*- coding: gb2312 -*-
    #
    # FileName: ModifyIP.py
    # Date : 2008-01-15
    #
import wmi
import requests
import time
con = requests.get("http://192.168.100.1")
print con.content

print'正在修改IP,请稍候...'
wmiService = wmi.WMI()
colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)
objNicConfig = colNicConfigs[2]
print objNicConfig.IPAddress
for i in range(10,15):
    print i
    arrIPAddresses =['192.168.100.{0}'.format(i)]
    arrSubnetMasks = ['255.255.255.0']
    print arrIPAddresses
    returnValue = objNicConfig.EnableStatic(IPAddress= arrIPAddresses,SubnetMask= arrSubnetMasks)
    print returnValue[0]
    if returnValue[0]==0:
        print'设置IP成功'
        time.sleep(4)
        con=requests.get("http://192.168.100.1")
        print con.content
    elif returnValue[0]==1:
        print'设置IP成功'
        print'IP: ', ', '.join(objNicConfig.IPAddress)

    else:
        print'修改IP失败: IP设置发生错误'
        exit()
