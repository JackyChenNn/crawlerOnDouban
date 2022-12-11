# 需求： 对豆瓣“十二怒汉”电影的评论进行数据抓取分析

from spiderOnDouban import spiderOnDouban

if __name__ == '__main__':
    # 添加cookie信息，登陆用户后才能浏览11页以后的内容
    cookie_info = 'bid=kD1UIMAs4NM; _pk_ses.100001.4cf6=*; ap_v=0,6.0; dbcl2="255460056:q3xqQCNbSyk"; ck=mcxN; _pk_id.100001.4cf6=4077063b62d68fff.1670750661.1.1670751170.1670750661.; push_noty_num=0; push_doumail_num=0'
    if cookie_info != 'your cookie':
        cookie_list = [info.strip().split('=') for info in cookie_info.split(';')]
        cookies = {data[0]:data[1].replace('"','') for data in cookie_list}

    url = 'https://movie.douban.com/subject/1293182/comments?limit=20&status=P&sort=new_score'
    print('Spider Started!')
    times = 0
    if 'cookies' in locals().keys():
        spiderOnDouban(url, times, cookies = cookies)
    else:
        spiderOnDouban(url, times)
