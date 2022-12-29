# Requirements: Search users enter movie names,
# search for corresponding movies in Douban, 
# then enter the comment page, and perform data 
# crawling and analysis on Douban movie comments

from tkinter import *
import ttkbootstrap as ttk
from crawlerOnDouban import crawlerOnComments, getid
from generateWordCloud import wordCloud
import matplotlib as plt
    
def crawler():
    cookie_info = 'your cookie'
    if cookie_info != 'your cookie':
        cookie_list = [info.strip().split('=') for info in cookie_info.split(';')]
        cookies = {data[0]:data[1].replace('"','') for data in cookie_list}

    if(name_input.get() != ''):
        movie_id = getid(name_input.get())
        url = 'https://movie.douban.com/subject/' + movie_id + '/comments?limit=20&status=P&sort=new_score'
        text.insert(END, 'Spider Started!')
        text.update()
        print('Spider Started!')
        times = 0
        if 'cookies' in locals().keys():
            crawlerOnComments(url, movie_id, times, cookies = cookies)
        else:
            crawlerOnComments(url, movie_id, times)
            
    else:
        text.insert(END, '未输入电影名')
        text.update()
    
if __name__ == '__main__':
    global name_input, text

    font_type = '微软雅黑'
    
    # 创建空白窗口,作为主载体 
    root = ttk.Window()
    style = ttk.Style(theme='cosmo')
    root.title('Crawler of Douban Short Commentary')
 
    # 窗口的大小，后面的加号是窗口在整个屏幕的位置 
    root.geometry('450x260+200+200')
 
    # 标签控件，窗口中放置文本组件 
    Label(root, text='请输入电影名:', font=(font_type, 15), fg='black').grid()
 
    # 定位 pack包 place位置 grid是网格式的布局 #Entry是可输入文本框 
    name_input = Entry(root, font=(font_type, 15))
    name_input.grid(row=0, column=1)
 
    # 列表控件 
    text = Listbox(root, font=(font_type, 15), width=45, height=10)
 
    # columnspan 组件所跨越的列数 
    text.grid(row=1, columnspan=2)
 
    # 设置按钮 sticky对齐方式，N S W E 
    button1 = Button(root, text='开始下载', font=(font_type, 15), command=crawler).grid(row=2, column=0, sticky=W)
    button2 = Button(root, text='退出', font=(font_type, 15), command=root.quit).grid(row=2, column=1, sticky=E)
 
    # 使得窗口一直存在 
    mainloop()