#import MySQLdb
import os
import time
f=open("C:\Users\leenhem\Desktop\ip_addr_bank.data",'r')
Da_ta=f.read()
print Da_ta
# nowtime=time.strftime("%Y%m%d%H",time.localtime(time.time()))
# lasttime=time.strftime("%Y%m%d%H",time.localtime(time.time()-3600))+"00"
# appid="default_app_id"
# memdisk="/dev/shm"
# src=memdisk+'/'+appid+'/'+lasttime
# outzippath="/opt/OTS_TS_REPORT"
# tmpzip="."+appid+"_uploadfile.zip.t"
# zipfileendpath=outzippath+"/"+appid+"/"+lasttime+"/"
# if not os.path.isdir(zipfileendpath):
#     os.makedirs(zipfileendpath)
# zipfilename=appid+'_'+lasttime+'.zip'
# LOG_FILE=zipfileendpath+appid+'_'+lasttime+'.log'
# def LOG(str):
#     os.chdir(outzippath)
#     Time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
#     f=open(LOG_FILE,'a')
#     f.write("%s      %s\n" %(Time,str))
#     f.close
#
# def addfile(path,Fsum,Tsum):
#     #    for file in os.listdir(path):
#     #	#file=os.path.join('/home/lihe',file)
#     #        if os.path.isfile(file):
#     #            zfile.write(file)
#     #	    Tsum=Tsum+1
#     #        else:
#     #	    Fsum=Fsum+1
#     #	    LOG(file)
#     #    for i in zfile.infolist():
#     #	print i.file_size, i.header_offset
#     if os.path.isdir(path):
#         zfile = zipfile.ZipFile(tmpzip, mode='w')
#         for dirpath,dirnames,filenames in os.walk(path):
#             for filename in filenames:
#                 os.chdir(memdisk)
#                 zfile.write(os.path.join(dirpath[len(memdisk)+1:],filename))
#                 Tsum=Tsum+1
#         zfile.close()
#     else:
#         LOG(path+"---- Directory does not exist.")
#     return Fsum,Tsum
# if __name__ == '__main__':
#     Fsum=0
#     Tsum=0
#     os.chdir(outzippath)
#     LOG('============= '+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))+' ============' )
#     zipfalse,ziptrue=addfile(src,Fsum,Tsum)
#     os.chdir(outzippath)
#     LOG('============= zip_sucessful('+str(ziptrue)+'), zip_faile('+str(zipfalse)+') =============')
#     os.chdir(outzippath)
#     if os.path.isfile(tmpzip):
#         os.rename(tmpzip,zipfileendpath+zipfilename)
#     LOG('============= '+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))+' ============' )