# -*- coding: UTF-8 -*-
'''
Created on 2016-12-12

@author: leenhem
'''
#import logging
import time
import os


class ToLogger(object):
    #===========================================================================
    # def Tolog (self,logfile,message):
    #    log_file=logfile+str(nowtime)+'.log'
    #    print log_file
    #    logging.basicConfig(level=logging.DEBUG,
    #                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                datefmt='%a, %d %b %Y %H:%M:%S',
    #                filename=log_file,
    #                filemode='a')
    #    logging.debug(message)
    #===========================================================================
    def Tolog (self,logfile,message):
        nowtime=time.strftime("%Y%m%d%H",time.localtime(time.time())) #The time in the name of the log file to print per day
        log_t=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        log_file=logfile.replace(".log",'_'+str(nowtime)+'.log')
        log_file_path=os.path.dirname(log_file)
        if not os.path.exists(log_file_path):
            os.makedirs(log_file_path)
        # print log_file
        logf=open(log_file,'a')
        logf.write(log_t+' --- '+message+'\n')
        logf.close()