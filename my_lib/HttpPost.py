# -*- coding: UTF-8 -*-
'''
Created on 2016-12-12

@author: leenhem
'''

# buld post body data
import urllib2, time
import my_lib
import os
import commands

class Http_post(object):
    def POST(self, http_url, zippackage, logfile):
        print http_url
        print zippackage
        print logfile
        cmd='/usr/bin/curl -s -F "action=uploadfile" -F "file=@'+zippackage+'" '+http_url+'?APPID=$appid'
        print cmd
        # '/usr/bin/curl -F "action=uploadfile" -F "file=@$zipfile" http://192.168.39.109:8080/v3/uploadfile?APPID=$appid '
        result = commands.getoutput(cmd)
        
        #f=open(logfile,'a')
        #f.write(str(http_url)+ ':::' + zippackage + ':::' + result+'\n')
        #f.close()
        log = my_lib.ToLog.ToLogger()
        log.Tolog(logfile, str(http_url)+ ':::' + zippackage + ':::' + result)
        # basezip=os.path.basename(zippackage)
        # boundary = '----------%s' % hex(int(time.time() * 1))
        # data = []
        # data.append('--%s' % boundary)
        #
        # data.append('Content-Disposition: form-data; name="%s"\r\n' % 'username')
        # data.append('jack')
        # data.append('--%s' % boundary)
        #
        # data.append('Content-Disposition: form-data; name="%s"\r\n' % 'mobile')
        # data.append('13800138000')
        # data.append('--%s' % boundary)
        #
        # #        fr=open(r'/var/qr/b.png','rb')
        # #        zippackage='r'+"'"+zippackage+"'"
        # fr = open(zippackage, 'rb')
        # #        data.append('Content-Disposition: form-data; name="%s"; filename="1006.zip"' % 'profile')
        # tmp = 'Content-Disposition: form-data; name="%s"; filename="' + basezip + '"'
        # data.append(tmp % 'profile')
        # data.append('Content-Type: %s\r\n' % 'image/png')
        # data.append(fr.read())
        # fr.close()
        # data.append('--%s--\r\n' % boundary)
        # #        print data
        # #        http_url='http://192.168.204.12:9900/uploadfile'
        # http_body = '\r\n'.join(data)
        # # print http_body
        # #        http_body='\r\n'.join(data)
        # #        print http_body
        # try:
        #     # buld http request
        #     req = urllib2.Request(http_url, data=http_body)
        #     # header
        #     req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
        #     #    req.add_header('User-Agent','Mozilla/5.0')
        #     #    req.add_header('Referer','http://remotserver.com/')
        #     # post data to server
        #     resp = urllib2.urlopen(req, timeout=1)
        #     # get response
        #     qrcont = resp.read()
        #
        # except Exception, e:
        #     qrcont = 'http error' + str(e)
