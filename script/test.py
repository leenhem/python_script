#-*- coding:UTF-8-*-
import csv
import re
import os
args=[
    '终端型号',
    '手机厂商',
    '网络名称',
    '服务器信息',
    '终端内网地址',
    '终端外网地址',
    '终端MAC地址',
    '日志版本',
    '客户端版本号',
    'APN',
    'MNC',
    '省',
    '市',
    '手机号码',
    '测试描述',
    '用户角色',
    '测试地点',
    '接入运营商',
    'IMEI',
    '测试地点（手动）',
    '接入运营商（手动）',
    '开通宽带手机号'
]

path='100'

mm=1
for m,n,x in os.walk(path):
    for fff_i in x:
        fff= os.path.join(os.path.dirname(os.path.abspath(fff_i)),m,os.path.basename(os.path.abspath(fff_i)))
        csvd = csv.reader(open(fff,'r'))
        data=[]
        files=[]
        for item in csvd:
            if item != []:
                reg=pattern = re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.*')
                reg_data=re.findall(reg,','.join(item))
                if reg_data != []:
                    files.append(reg_data[0])
                for arg_index in range(0,len(args)-1):
                    if item[0].strip() == args[arg_index].strip():
                        # print item[0],item[1]
                        data.append(item[1])

        for i in range(0,len(files)):
            outfilename=str(mm)+'_'+str(i+1)
            fi=open(outfilename,'w')
            fi.write('@'.join(data)+'@'+files[i])
            fi.close()
        mm=mm+1

