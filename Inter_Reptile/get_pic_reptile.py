#!/usr/bin/python 
# -*- coding: utf-8 -*-
import urllib.request
import re
import os
import sys
import json
import time

from lxml import etree
from PIL import Image
from PIL import ImageFile
import startUi as SUI

ImageFile.LOAD_TRUNCATED_IMAGES = True

#全局变量
num=1


#浏览器请求抬头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
           ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
           ,'Accept-Encoding':'gzip, deflate'
           ,'Cache-Control':'max-age=0'
           ,'Upgrade-Insecure-Requests':'1'
           ,'Connection':'keep-alive'
           ,'Host':''
           ,'Accept-Language':'zh-CN,zh;q=0.9'}


# 执行API调用并储存响应
def download(url):
    #伪装成浏览器请求
    request=urllib.request.Request(url, headers=headers)
    index=urllib.request.urlopen(url)
    pic=index.read()
    return pic


#针对一页一图式的翻页处理
def next_pages(html,page):
    #为了加后缀转化列表
    new_add=list(html)
    #针对网页一图一页式加后缀
    new_add.insert(-5,'_%s'%page)
    #合并链列表
    new_page="".join((new_add))
    return new_page


def transformPng(ImageFile):
    # 分割文件路径和后缀名
    FilePath,Fileext = os.path.splitext(ImageFile)
    # 设置保存后的文件格式
    outImageFile = "{0}.png".format(FilePath)
    # 打开并保存
    Image.open(ImageFile).save(outImageFile)
    return



#正则寻找代码中图片的链接
def find_jpg(html):
    address=r'<img alt=[^\']+? src="(.*?)"'
    pattern=re.compile(address)
    get_pic=re.findall(pattern,repr(html))
    return get_pic
    '''htm=etree.HTML(html)
    #正则很难定位该scr链接,所以此处改用Xpath,速度比正则慢
    get_pic=htm.xpath('//div[@class="picsbox picsboxcenter"]//img/@src')
    return get_pic'''

def getName(html):
    #因为该HTML编码方式为GB2312，所以先解码，然后再转码为utf-8再解码得到标题
    html=html.decode('GB2312','ignore').encode('utf-8','ignore').decode('utf8','ignore')
    title=r'<h1 class="articleV4Tit">(.*?)</h1>'
    filesname=re.findall(title,repr(html))
    dst = '.'.join(filesname)
    sstr=str(dst)
    return sstr
    #此处将html转码,方便我匹配网页的中文标题
    '''html=html.decode('utf-8')
    title=r'<strong>(.*?)</strong>'
    filesname=re.findall(title,repr(html))
    dst = '.'.join(filesname)
    sstr=str(dst)
    return sstr'''


#创建文件夹
def mkdir(html,dst):  
    cur_dir='image1/'
    
    #判定是否存在路径cur_dir
    if os.path.isdir(cur_dir):
        os.mkdir(os.path.join(cur_dir, dst))
        path=os.getcwd()+'\image1\%s'%dst
        return path
    else:
        print('找不到文件夹')

def getPagesTotal(html):
    html=html.decode('utf-8')
    np=r'<div class="NewPages">.+?<a>共(.+?)页'
    numb=re.findall(np,repr(html))
    fig=int(numb[0])
    return fig


#下载图片    
def get_pic(html,htm):
    global num
    #寻找链接
    #headers['Host']='i1.umei.cc'
    get_pic=find_jpg(html)
    #寻找此页面的子页面总量
    #fig=getPagesTotal(html)
    dst=""
    dst=getName(html)
    print(dst)
    a=mkdir(html,dst)
      
    
    i=1
    #顺序存储每页图片
    while(1):
        #翻页后的处理
        if i>1:
            nPages=next_pages(htm,i)
            try:
                next_html=download(nPages)
            #若没有下一页,跳出循环
            except urllib.request.HTTPError:
                break
            get_pic=find_jpg(next_html)
        
        i+=1
        attempt=True
        while(attempt and get_pic):
            pic=get_pic[0]
            try:
                pict=download(pic)
                #赋予正确路径
                filename=a+'\%s.jpg'%num
                with open(filename,'wb') as fp:
                    fp.write(pict)
                    transformPng(filename)
                    fp.close()
                    #删除jpg文件
                    os.remove(filename)
                    print(pic+'\n第%s张图片下载完成\n'%num)
                    num+=1
                    time.sleep(3)
                    attempt=False
                    break
            except TypeError:
                print('格式错误')
                return
            except urllib.request.URLError:
                print("再试一次!")
            except ConnectionResetError:
                print("重连主机")
            else:
                print("Not Exactly!")
    num=1
    
    
#存储本次爬取的html地址
def save_html(lists):
    filename='html.json'
    with open(filename) as f:
        if os.path.getsize(filename)!=0:
            old_html=json.load(f)
            #将新的地址加到json取出的列表尾部
            lists=lists+old_html
        else:
            print("Kong")
        
    with open(filename,'w') as f:
        #以列表形式存储到json里
        json.dump(lists,f)
        print("存储成功!")
    f.close()


#检测是否有下载过的html地址并删除    
def rm_ele(list1):
    #赋值该列表
    list_copy=list1.copy()
    filename='html.json'
    with open(filename) as f:
        #从json中取出列表比对
        if os.path.getsize(filename)!=0:
            old_html=json.load(f)
            print("旧的html:",len(old_html))
            for i in list_copy:
                if i in old_html:
                    list1.remove(i)
        else:
            print("Kong")
        f.close()

    #比对两个列表，重复即删除该元素
    return list1
    
    
    
#获取次页面
def get_html(html):
    i_url=r'<li>.*?<a href="(http://www.27270.com/ent/meinvtupian/.*?/.*?.html)"'
    pattern=re.compile(i_url)
    get_first=re.findall(pattern,repr(html))
    get_htm={}.fromkeys(get_first).keys()
    get_htm=list(get_htm)
    print(get_htm)
    #调用rm_ele删除重复Html
    get_htm=rm_ele(get_htm)
    print(len(get_htm))
    
        
  #遍历页面并调用下载函数get_pic
    '''for htm in get_htm:
          print(htm)
          url=download(htm)
          get_pic(url,htm) 

    #保存本次访问的Html
    save_html(get_htm)'''
   
    
 
    
url='http://www.27270.com/ent/meinvtupian/list_11_4.html'
html=download(url)
get_html(html)
path=os.getcwd()+'\\image1'
SUI.run(path)

