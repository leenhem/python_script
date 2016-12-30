# -*- coding: UTF-8 -*-
'''
Created on 2016-12-12

@author: leenhem
'''

import zipfile
import my_lib
import os
class FileToZip(object):
    def Tozip(self,filelist,zipfilename,logfile):
        # print 'model1:',filelist,zipfilename
        log=my_lib.ToLog.ToLogger()
        if not os.path.exists(os.path.dirname(zipfilename)):
            os.makedirs(os.path.dirname(zipfilename))
        zfile = zipfile.ZipFile(zipfilename, mode='w') #create zip file
        Tsum=0
        for file_list_index in range(0,len(filelist)):  #loop reportfilelist
            # print 'model:Tozip:',filelist[file_list_index]
            zfile.write(filelist[file_list_index])  #Press the file to the zip file
            Tsum=Tsum+1
            log.Tolog(logfile, str(Tsum)+' '+filelist[file_list_index])
        zfile.close() #After compression is completed, close the open zip file
        # print 'tozip:',zipfilename
        return zipfilename