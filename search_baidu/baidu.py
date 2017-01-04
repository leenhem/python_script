# _*_ coding:utf-8 _*_
from web.contrib.template import render_jinja
import web
import urllib2,urllib
import re,json
urls=(
    '/','Index',#get post
    # '/(js|css|images)/(.*)', 'static',
    '/s','So',
    '/key','Key',
)


render = render_jinja(
    'templates'
    # 'static'
)#实例化模板文件

def getdata(wd):#获取百度数据
    #类似于 爬虫
    wd=urllib.quote(wd.encode('utf-8'))
    # url='https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=%s' %(wd)
    url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%s' %(wd)
    add_headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    }
    req=urllib2.Request(url,headers=add_headers)
    html=urllib2.urlopen(req).read()
    return html


def getkey(wd):
    wd=urllib.quote(wd.encode('utf-8'))
    url='https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=%s' %(wd)
    add_headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    }
    req=urllib2.Request(url,headers=add_headers)
    html=urllib2.urlopen(req).read()
    reg=re.compile(r'window.baidu.sug\(\{q:"cc",p:false,s:\[(.*?)\]\}\);')
    html=reg.findall(html)
    print html
    # print json.loads(html[0])
    # for i in html[0]:
    #     print i

class Index():
    def GET(self):
        # return 'hello,world'
        return render.index()

class So:
    def GET(self):
        i=web.input()#获取用户请求的参数
        text=getdata(i.wd)
        return text

class Key:
    def GET(self):
        i=web.input()
        key=i.wd
        getkey(key)
        print 'key:',key
        # return key

if __name__ == '__main__':
    web.application(urls,globals()).run()


#ajxs 异步

