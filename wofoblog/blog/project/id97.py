import requests
import bs4
import os
import threading
import time
from threading import Thread
import urllib

gCondition = threading.Condition()



def get_html(url):  # 抓取网页
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "someting error"

def get_one_text(url):
    html = get_html(url)
    url_list = []
    info = {}
    soup = bs4.BeautifulSoup(html, 'lxml')
    move_list = soup.find_all('div', class_='col-xs-1-5 col-sm-4 col-xs-6 movie-item')
    for moves in move_list:

        file_name = moves.find('div', class_='meta').find('a').text  # 获取电影名
        file_url = moves.find('div', class_='movie-item-in').a['href']  # 获取链接
        image = moves.find('img', class_='lazy')['data-original']  # 获取图片下载链接
        # print(image)
        filename = 'E:/move/' + file_name
        path = '%s/%s.jpg' % (filename, file_name)
        # downimg(filename, path, image)
        # url_list.append(file_url)
        # print(file_url)
        attr = file_url.split('/')[-1]
        magnet, text = get_one_info(attr, filename, file_name)
        info[text] = magnet
        url_list.append(info)
        info = {}
    return url_list

def get_one_info(attr, path, name): # 获取每一个电影，并创建文本保存
    # url_list = []
    html = get_html('http://www.id97.com/videos/resList/'+attr)
    soup = bs4.BeautifulSoup(html, 'lxml')
    info = soup.find('table', class_='table table-hover')  # 获取网盘地址
    # print(info)
    text = info.find('td', class_='text-break').find('a')['title']
    magnet = info.find('td', class_='text-break').find('a')['href']
    # print('===')
    # print(text)
    # print("------")
    # print(magnet)
    # print('===')
    return magnet, text
    #print("完成%s的下载"% name)

def downimg(filename,path,image):
    folder = os.path.exists(filename)
    if not folder:
        os.makedirs(filename)
        if not os.access(path, os.F_OK):
            # time.sleep(1)
            urllib.request.urlretrieve(image, path)  # 下载图片
    else:
        if not os.access(path, os.F_OK):
            # time.sleep(1)
            urllib.request.urlretrieve(image, path)




if __name__ == '__main__':
    url = 'http://www.id97.com/movie/?tag=%E7%A7%91%E5%B9%BB'
    print('获取链接完毕，正在获取资源....')
    get_one_text(url)

    print('资源获取完毕')
    #print(text)

