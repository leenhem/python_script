# _*_ coding:utf-8 _*_
from web.contrib.template import render_jinja
import web
import urllib2,urllib
urls=(
    '/','Index',#get post
    '/s','So',
    '/key','Key',
)

render = render_jinja(
    'templates'
)#实例化模板文件

def getdata(wd):#获取百度数据
    #类似于 爬虫
    wd=urllib.quote(wd.encode('utf-8'))
    html=urllib2.urlopen('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=nihao&oq=jianjia2%20github&rsv_pq=817cde4d0000de7c&rsv_t=8847JgOKEl7tDjIkQeqnjtD99r1fj43Sq7wJ8eDbfhyHi9g1eI7g08ctVLY&rqlang=cn&rsv_enter=1&inputT=3597&rsv_sug3=35&rsv_sug1=26&rsv_sug7=100&rsv_sug2=0&rsv_sug4=5156')
    html=urllib2.Request('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=nihao&oq=jianjia2%20github&rsv_pq=817cde4d0000de7c&rsv_t=8847JgOKEl7tDjIkQeqnjtD99r1fj43Sq7wJ8eDbfhyHi9g1eI7g08ctVLY&rqlang=cn&rsv_enter=1&inputT=3597&rsv_sug3=35&rsv_sug1=26&rsv_sug7=100&rsv_sug2=0&rsv_sug4=5156')
    html.add_data('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.3 Safari/537.36')
    return html

def getkey(wd):
    # req =
    pass

class Index():
    def GET(self):
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

if __name__ == '__main__':
    web.application(urls,globals()).run()


#ajxs 异步

