# -*- coding: utf-8 -*-
    #
    # FileName: ModifyIP.py
    # Date : 2008-01-15
    #
import wmi
print'正在修改IP,请稍候...'
wmiService = wmi.WMI()
colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)

for objNicConfig in colNicConfigs:
    print objNicConfig.Index
    #print objNicConfig.SettingID
# print objNicConfig.Description.encode("cp936")
    print objNicConfig.IPAddress
# print objNicConfig.IPSubnet
# print objNicConfig.DefaultIPGateway
# print objNicConfig.DNSServerSearchOrder
if len(colNicConfigs)<1:
    print'没有找到可用的网络适配器'
    exit()
objNicConfig = colNicConfigs[2]
print objNicConfig.IPAddress
#for method_name in objNicConfig.methods:
# method = getattr(objNicConfig, method_name)
# print method
arrIPAddresses =['172.16.151.147']
arrSubnetMasks =['255.255.255.0']
arrDefaultGateways =['172.16.151.1']
arrGatewayCostMetrics =[1]
arrDNSServers =['172.16.151.10']
intReboot =0
returnValue = objNicConfig.EnableStatic(IPAddress= arrIPAddresses,SubnetMask= arrSubnetMasks)
print returnValue[0]
if returnValue[0]==0:
    print'设置IP成功'
elif returnValue[0]==1:
    print'设置IP成功'
    intReboot +=1
else:
    print'修改IP失败: IP设置发生错误'
    exit()
returnValue = objNicConfig.SetGateways(DefaultIPGateway= arrDefaultGateways,GatewayCostMetric= arrGatewayCostMetrics)
if returnValue[0]==0:
    print'设置网关成功'
elif returnValue[0]==1:
    print'设置网关成功'
    intReboot +=1
else:
    print'修改IP失败: 网关设置发生错误'
    exit()
returnValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder= arrDNSServers)
if returnValue[0]==0:
    print'设置DNS成功'
elif returnValue[0]==1:
    print'设置DNS成功'
    intReboot +=1
else:
    print'修改IP失败: DNS设置发生错误'
    exit()
if intReboot >0:
    print'需要重新启动计算机'
else:
    print''
    print'修改后的配置为：'
    print'IP: ',', '.join(objNicConfig.IPAddress)
    print'掩码: ',', '.join(objNicConfig.IPSubnet)
    print'网关: ',', '.join(objNicConfig.DefaultIPGateway)
    print'DNS: ',', '.join(objNicConfig.DNSServerSearchOrder)
    print'修改IP结束'
