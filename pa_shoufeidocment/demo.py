#_*_ coding:utf-8 _*_
#写爬虫不是先写代码，是先分析网站

import urllib2
import cookielib
import re
#创建一个cookie对象来保存cookie
cookie = cookielib.CookieJar()
handler= urllib2.HTTPCookieProcessor(cookie)#urllib2创建一个cookie
opener=urllib2.build_opener(handler)#构建一个handler对象
#opener可以直接打开网站
def login():
    # Request URL:http://www.ks5u.com/user/inc/UserLogin_Index.asp
    # Request Method:POST
    # username=a&password=a&c_add=0
    user='formekeepsilence@163.com'
    passw='suyue918'
    req=urllib2.Request('http://www.ks5u.com/user/inc/UserLogin_Index.asp',data='username=%s&password=%s&c_add=0'%(user,passw))
    html=opener.open(req).read()
    # html=urllib2.urlopen('http://www.ks5u.com/user/inc/UserLogin_Index.asp',data='username=%s&password=%s&c_add=0'%(user,passw)).read()#打开网页
    return html

# def

if 'formekeepsilence@163.com' in login():
    print '登录成功'
else:
    print '登录失败'

def getlist():
    req=urllib2.Request('http://www.ks5u.com/zhuantimoni/ashx/jinbang.ashx')
    req.add_data('xueke=1&shenfen=32')
    text= opener.open(req).read()
    reg=re.compile(r'<a href="(.*?)" target="_blank" title="(.*?)">')
    text=reg.findall(text)
    return text

def getfile(id,name):
    # req=urllib2.Request('http://www.ks5u.com/USER/INC/DownCom.asp?id=%s'%(id))
    req=urllib2.Request('http://www.ks5u.com/USER/INC/DownCom.asp?id=2493361')
    print
    # req.add_data('Referer','http://www.ks5u.com/zhuantimoni/yimo.html')
    print opener.open(req).read()
for i in  getlist():
    url= i[0]
    name=i[1]
    id=url.split('/')[-1][:6]
    getfile(id,name)
    print id,name
    break