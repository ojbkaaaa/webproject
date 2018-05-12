from multiprocessing import Pool
import requests
import bs4
import threading, time
import time

jobs = []


def get_html(url):  # 抓取网页
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "someting error"


def get_one_info(attr): # 获取每一个电影，并创建文本保存
    html = get_html('http://www.id97.com/videos/resList/' + attr)
    soup = bs4.BeautifulSoup(html, 'lxml')
    info = soup.find_all('table', class_='table table-hover')  # 获取网盘地址
    # print(info)
    d = {}
    if not info[0]:
        info = info[1]
    else:
        info = info[0]
    text = info.find('td', class_='text-break').find('a')['title']
    magnet = info.find('td', class_='text-break').find('a')['href']
    d[text] = magnet
    return d

def get_one_text():
    url = 'http://www.id97.com/movie/?tag=%E7%A7%91%E5%B9%BB'
    html = get_html(url)
    global jobs
    d = []
    soup = bs4.BeautifulSoup(html, 'lxml')
    move_list = soup.find_all('div', class_='col-xs-1-5 col-sm-4 col-xs-6 movie-item')
    for moves in move_list:
        # file_name = moves.find('div', class_='meta').find('a').text  # 获取电影名
        file_url = moves.find('div', class_='movie-item-in').a['href']  # 获取链接
        attr = file_url.split('/')[-1]
        # magnet, text = get_one_info(attr)
        # d[text] = magnet
        d.append(attr)
    return d

if __name__ == '__main__':
    info = get_one_text()
    start = time.time()
    p = Pool(processes=5)
    # d = mgr.dict()
    for i in info:
        jobs.append(p.apply_async(get_one_info, (i,)))

    p.close()
    p.join()
    end = time.time()
    print(end - start)
    # print(jobs)
    for job in jobs:
        print(job.get())


