# -*- coding: UTF-8 -*-
'''
Created on 2016-12-8

@author: leenhem
'''
import time
import json
import os, re, sys
import glob
import threading
import Queue
sys.path.append('/home/ziranwei_report_distribute/')
# print sys.path
import my_lib
import subprocess
import commands
log = my_lib.ToLog.ToLogger()
import shutil
shutil.move()

# lasttime = time.strftime("%Y%m%d%H%M", time.localtime(time.time() - 60))  # 取上一分钟的日志所用的时间
# lasthour = time.strftime("%Y%m%d%H", time.localtime(time.time() - 3600)) + '*'
# lastday = time.strftime("%Y%m%d", time.localtime(time.time() - 3600 * 24)) + '*'
filetime = time.strftime("%Y%m%d%H%M", time.localtime(time.time() - 60))
lasttime = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time() - 60))
lasthour = time.strftime("%Y-%m-%d %H", time.localtime(time.time() - 3600))
lastday = time.strftime("%Y-%m-%d", time.localtime(time.time() - 3600 * 24))
log_time_path=time.strftime("%Y%m%d",time.localtime(time.time()))

#json_file = os.path.join(os.path.abspath('..'), 'configure', 'Distribute_load.json')
json_file='/home/ziranwei_report_distribute/configure/Distribute_load.json'
json_data = open(json_file, 'r').read()

police_file = os.path.join(os.path.abspath('..'), 'configure', json.loads(json_data)['conf_path'])
rule = json.loads(json_data)['frequency_rule']
log_file = json.loads(json_data)['script_log']
toana_log = json.loads(json_data)['analysismodel_log']
print lasttime
# t_file = str(json.loads(json_data)['log_path']).split('/00000000/')[0]+ '/' + str(lasttime)[:8] + '/' + str(json.loads(json_data)['log_path']).split('/00000000/')[1]
t_file = str(json.loads(json_data)['log_path']).split('/00000000/')[0]+ '/' + str(filetime)[:8] + '/'
t_args=str(json.loads(json_data)['log_path']).split('/00000000/')[1].split('-*-')[0]
print t_args
print t_file
if rule == 'minute':
    # strinfo = re.compile(r'\d+')
    # strinfo = re.compile(r'000000000000')
    # file = strinfo.sub(lasttime, t_file)
    filelist = []
    # for filename in glob.glob(file):
    #     print 'filename',filename
    #     filelist.append(filename)
    cmd='ls -hlt --full-time '+t_file+'|grep '+'"'+lasttime+'"'+'|awk \'{print $NF}\''+'|grep '+t_args

    for filename in range(0,len(str(commands.getoutput(cmd)).splitlines())):
        print 'filename:',filename
        filelist.append(str(commands.getoutput(cmd)).splitlines()[filename])
    print filelist
elif rule == 'hour':
    # strinfo = re.compile(r'000000000000')
    # file = strinfo.sub(lasthour, t_file)
    filelist = []
    cmd='ls -hlt --full-time '+t_file+'|grep '+'"'+lasthour+'"'+'|awk \'{print $NF}\''+'|grep '+t_args

    for filename in range(0,len(str(commands.getoutput(cmd)).splitlines())):
        print 'filename:',filename
        filelist.append(str(commands.getoutput(cmd)).splitlines()[filename])
    print filelist
    # for filename in glob.glob(file):
    #     filelist.append(filename)
elif rule == 'day':
    # strinfo = re.compile(r'000000000000')
    # file = strinfo.sub(lastday, t_file)
    filelist = []
    cmd='ls -hlt --full-time '+t_file+'|grep '+'"'+lastday+'"'+'|awk \'{print $NF}\''+'|grep '+t_args

    for filename in range(0,len(str(commands.getoutput(cmd)).splitlines())):
        print 'filename:',filename
        filelist.append(str(commands.getoutput(cmd)).splitlines()[filename])
    print filelist
    # for filename in glob.glob(file):
    #     filelist.append(filename)

print cmd
print 'logfilelist:::',filelist
police_data = open(police_file, 'r').read()


class thread_tozip(threading.Thread):
    def __init__(self,t_name,queue,reportfilelist,zipfilename,tozip_log):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue
        self.t_reportfilelist=reportfilelist
        self.t_zipfilename=zipfilename
        self.t_tozip_log=tozip_log
    def run(self):
        zipfile = tozip.Tozip(self.t_reportfilelist, self.t_zipfilename,self.t_tozip_log)  # 将zip文件名和reportfilelist传给 Tozip
        self.data.put(zipfile)

class thread_topost(threading.Thread):
    def __init__(self,t_name,queue,url,distrbute_log):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue
        self.t_url=url
        self.t_distrbute_log=distrbute_log
        # self.t_distrbute_log='http://192.168.39.109:8080/v3/uploadfile'
    def run(self):
        zipfile=self.data.get(1,5)
        distrbute = my_lib.HttpPost.Http_post()
        Urllist=str(self.t_url).split(';')
        for index in range(0,len(Urllist)):
            distrbute.POST(Urllist[index], zipfile, self.t_distrbute_log)

if __name__ == "__main__":
    # print '__main__'
    analog = my_lib.AnalysisLog.AnaLog() #实例化log分析模块为analog
    tozip = my_lib.ToZip.FileToZip() #实例化zip压缩模块为tozip

    list_appid = locals()
    appid_list = []
    for json_array_index in range(0, len(json.loads(police_data))):  # 获取每个appid对应的配置--------待分发APPID 列表
        json_appid = json.loads(police_data)[json_array_index]['probeid']  # 获取appid
        #定义存放对应APPID的配置项为一个字典
        list_appid['appid_%s' % json_appid] = {'appid':'','reportfilezip_file':'','tozip_log':'','http_url':'','distrbute_log':'','reportlist':[]}
        #为字典中每个appid，取配置
        list_appid['appid_%s' % json_appid]['appid']=json.loads(police_data)[json_array_index]['probeid']# 获取appid
        node_alias=json.loads(police_data)[json_array_index]['node_alias']
        list_appid['appid_%s' % json_appid]['reportfilezip_file']=os.path.join(str(json.loads(police_data)[json_array_index]['zipmodel_fpath']),json_appid+'_'+str(node_alias)+'_'+str(filetime)+'.zip')# 获取zip包名
        list_appid['appid_%s' % json_appid]['tozip_log'] = json.loads(police_data)[json_array_index]['zipmodel_flog']  # 获取zip模块log
        list_appid['appid_%s' % json_appid]['http_url'] = str(json.loads(police_data)[json_array_index]['dismodel_posturi'])  # 获取分发uri
        list_appid['appid_%s' % json_appid]['distrbute_log'] = json.loads(police_data)[json_array_index]['dismodel_flog']  # 获取分发log目录
        #定义待分发的appid的列表
        tmp_appid_list = 'appid_' + json_appid
        appid_list.append(tmp_appid_list)
    print appid_list
    print list_appid[appid_list[0]]
    print list_appid[appid_list[1]]
    print list_appid[appid_list[2]]
    print

    sumfile = str(json.loads(json_data)['sum_log']).split('.log')[0]+'_'+str(filetime)+'.log'
    sumfilename=os.path.basename(sumfile)
    sumfilepath=os.path.join(os.path.dirname(sumfile),'log',log_time_path)
    sumfile=os.path.join(sumfilepath,sumfilename)
    if not os.path.isdir(sumfilepath):
        os.makedirs(sumfilepath)
    sum_file_f=open(sumfile,'w')
    print '文件列表：',filelist
    for l_file in range(0, len(filelist)):  # 将要被解析的文件列表
        tmp_file=open(os.path.join(t_file,filelist[l_file]),'rU')
        sum_file_f.write(tmp_file.read())
        tmp_file.close()
    sum_file_f.close()

    reportfile_list = analog.Analog(sumfile, toana_log)
    print len(reportfile_list)
    if len(reportfile_list) == 0:
        msg="reportfile_list is null."
        log.Tolog(toana_log,msg)
        sys.exit()

    for reportfile_list_index in range(0, len(reportfile_list)):  # 解析完成的文件列表
        appid = reportfile_list[reportfile_list_index].split('/')[8]  # 获取解析完成的报告文件的appid
        tmp_appid=appid
	for configappid_index in range(0,len(appid_list)):
            confappid=appid_list[configappid_index].split('_')[1]
            print '111',appid,confappid
            if appid == confappid:
            # print appid, type(list_appid['appid_%s' % appid]['reportlist'])
                print 'lihe',list_appid['appid_%s' % appid]['reportlist']
                list_appid['appid_%s' % appid]['reportlist'].append(reportfile_list[reportfile_list_index])#把APP ID对应的报告放到相应的appid列表里
                print "reportlist >>>>",list_appid['appid_%s' % appid]['reportlist']
            else:
                print "reportlistnull",reportfile_list[reportfile_list_index]

    print appid_list
    for thread_index in range(0,len(appid_list)):
        print thread_index,appid_list[thread_index]
        queue = Queue.Queue()
        id = str(appid_list[thread_index]).split('_')[1]
        # print id
        print list_appid['appid_%s' % id]['reportlist']
        if list_appid['appid_%s' % id]['reportlist'] != []:
            print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
            reportfile=list_appid['appid_%s' % id]['reportlist']
            tozipfile=list_appid['appid_%s' % id]['reportfilezip_file']
            toziplog=list_appid['appid_%s' % id]['tozip_log']
            http_url=list_appid['appid_%s' % id]['http_url']
            distrbute_log=list_appid['appid_%s' % id]['distrbute_log']
            distrbute_log=os.path.join(os.path.dirname(distrbute_log),log_time_path,os.path.basename(distrbute_log))
            toziplog=os.path.join(os.path.dirname(toziplog),'log',)
            print appid_list[thread_index], queue,reportfile,tozipfile,toziplog

            t_2_zip = thread_tozip(appid_list[thread_index], queue,reportfile,tozipfile,toziplog)
            t_2_zip.setDaemon(True)
            t_2_zip.start()
            print 'start post'
            t_2_post = thread_topost(str(appid_list[thread_index]) + '_post', queue,http_url,distrbute_log)
            t_2_post.setDaemon(True)
            t_2_post.start()

            t_2_zip.join()
            t_2_post.join()
            # t_2_post.run()
            # print t_2_zip, t_2_post
