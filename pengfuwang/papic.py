#coding:utf-8
# pythonr爬取捧腹网
# 1.知识点:爬虫模块 urllib re
#2.原理：打开网址urlopen--read源码---获取内容---下载urlretrieve
#[\s\S]* 匹配 全部 包 \n
import urllib,re,sys
reload(sys)
sys.setdefaultencoding('utf-8')#输出的内容为UTF-8


#打开网址，获取源码
def getHtml(pg):
    url='http://www.pengfu.com/index_%s.html'%(pg)
    html=urllib.urlopen(url).read()
    return html

def title(test): #compile 把正则表达式 转换为 正则表达式对象 提高效率
    reg=re.compile(r'<h1 class="dp-b"><a href=".*?" target="_blank">(.*?)</a>[\s\S]*?width=.*?src="(.*?)">')
    list=reg.findall(test)
    return list


def download(name,url):
    # 先解码 编码，windows 识别gbk
    path='img\%s.jpg'%name.decode('utf-8').encode('gbk')
    print path
    urllib.urlretrieve(url,path)
if __name__ == '__main__':
    for mm in range(1,20):
        pic_list=title(getHtml(mm))
        for i in pic_list:
            print i[0],i[1]
            download(i[0],i[1])