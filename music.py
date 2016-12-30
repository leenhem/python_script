# _*_ coding:utf-8 _*_

from Tkinter import *

import tkMessageBox
import urllib2,urllib
import time
import json
import threading
import mp3play
m_list = []
def music():
    text = entry.get().encode('utf-8')
    print text
    text=urllib.quote(text)
    print text
    if not text:
        tkMessageBox.showinfo('温馨提示','您可以输入以下内容进行搜索:\n1,歌曲名\n2,歌手名\n3.部分歌词')
        return
    html = urllib2.urlopen('http://s.music.163.com/search/get/?type=1&s=%s&limit=9'%(text))
    text=json.loads(html.read())
    list_s=text['result']['songs']

    listbox.delete(0,listbox.size())
    for i in range(0,len(list_s)):
        listbox.insert(i,list_s[i]['name']+'  '+list_s[i]['artists'][0]['name'])
        m_list.append(list_s[i]['audio'])
    print m_list

def play():
    label.pack(fill=Y,expand=1)
    sy=listbox.curselection()[0]
    print m_list[int(sy)]
    # print ','.join(listbox.selection_get().split('  '))
    s_name=listbox.selection_get().split('  ')[0].encode('utf-8')
    sr_name=listbox.selection_get().split('  ')[1].encode('utf-8')
    label.config(text = '正在缓冲 '+sr_name+' 的 '+s_name+' ...', font = 'Helvetica -12')
    m_name=listbox.selection_get().encode('utf-8')
    m_name=time.strftime('%Y%m%d%H%M%S')+'.mp3'
    urllib.urlretrieve(m_list[int(sy)],m_name)
    mp3=mp3play.load(m_name)
    label.config(text = '缓冲完成', font = 'Helvetica -12')
    mp3.play()
    scale.config( from_=0, to=mp3.seconds(), orient=HORIZONTAL, command=resize,troughcolor='gray50')

    for i in range(0,mp3.seconds()):
        print i
        time.sleep(1)
    # time.sleep(mp3.seconds())
    mp3.stop()

def th(event):
    t=threading.Thread(target=play)
    t.start()

def resize(ev=None):
    print scale.get()
    # label.config(font='Helvetica -%d bold' % scale.get())

root = Tk()
root.title("在线听歌")
root.geometry('+500+250') #窗口大小,窗口位置
entry=Entry(root)
entry.pack()
Button(root,text='搜索歌曲',command=music).pack()

var =StringVar()
listbox=Listbox(root,width=50,listvariable=var)
listbox.bind('<Double-Button-1>',th)
listbox.pack()

label = Label(root, text = '正在缓冲...', font = 'Helvetica -12')
scale = Scale(root, from_=0, to=40, orient=HORIZONTAL, command=resize,troughcolor='gray50')
scale.pack(fill=X, expand=1)

mainloop()