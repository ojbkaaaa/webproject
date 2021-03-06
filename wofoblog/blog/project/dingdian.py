from multiprocessing import Pool
import requests
import bs4,os,re
from lxml import etree
import threading, time
import time

jobs = []


def get_html(url):  # 抓取网页
    try:
        kv = {
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
            'Accept - Encoding': 'gzip, deflate, br',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Host': 'www.xxbiquge.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        r = requests.get(url, headers=kv, timeout=60)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "someting error"

def get_xs_url(ss):  # 获取书名相关的小说的信息
    # new = TF.transformation_quote(ss)
    url = 'https://www.xxbiquge.com/search.php?keyword=%s' % ss
    print(url)
    txt = {}
    list = []
    html = get_html(url)
    hh = bs4.BeautifulSoup(html, 'lxml')

    flag = hh.find('div', class_='result-item result-game-item')
    if flag:
        #  print('1111')
        div = hh.find('div', class_='result-list').find_all('div', class_='result-item result-game-item')
        # infos = div.find_all('li')
        for info in div:
            s = info.find('h3').find('a')
            new = info.find('p', class_='result-game-item-desc').text
            id = s['href'].split('/')[-2]
            url = '/blog/book/%s' % (s['href'].split('/')[-2])
            name = s.text
            p = info.find('div', class_='result-game-item-info').find_all('p')
            for xx in p:
                author = p[0].find_all('span')[1].text
            txt['id'] = id
            txt['url'] = url
            txt['name'] = name
            txt['author'] = author
            txt['jianjie'] = new
            list.append(txt)
            txt = {}

    else:
        #  print('2222')
        return ''
    return list

def get_xs_info(e):  # 获取小说所有章节链接
    # txt_list = get_xs_url(url)
    novel_txt = {}
    lists = []
    # url = txt_list[num]['url']
    url = 'https://www.xxbiquge.com/%s/' % e
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    # print(soup)
    novel_name = soup.find('div', id='maininfo').find('h1').text
    list = soup.find('div', id='list')
    # print(list)
    list_url = list.find_all('dd')
    #for info in list_url:  # 获取每一个章节相关信息
    for i in range(0, len(list_url)):
        name = list_url[i].find('a').text
        now_url = list_url[i].find('a')['href']
        if i == 0:  # 第一章
            url_1 = ''
        else:
            url_1 = list_url[i-1].find('a')['href']
        if (i+1) == len(list_url):  # 最后一章
            url_2 = ''
        else:
            url_2 = list_url[i + 1].find('a')['href']
        result_1 = re.findall('(\d+)', url_1)
        result_2 = re.findall('(\d+)', url_2)
        result = re.findall('(\d+)', now_url)
        id_now = '_'.join(result)
        id_1 = '_'.join(result_1)
        id_2 = '_'.join(result_2)
        id11 = '%s-%s-%s' % (id_1, id_now, id_2)
        now_url = '/blog/book_detail/%s' % id11
        novel_txt['name'] = name
        novel_txt['url'] = now_url
        novel_txt['id'] = id11
        lists.append(novel_txt)
        novel_txt = {}
    novel_txt['novel_name'] = novel_name
    lists.append(novel_txt)

    return lists

def get_xs_text(url):
    # list = get_xs_info(url, num)
    # print('====')
    # print(list)
    # url = list[num]['url']
    url = 'https://www.xxbiquge.com/%s' % url
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    name = soup.find('div', class_='con_top').find_all('a')[2].text
    main = soup.find('div', id='wrapper').find('div', class_='content_read').find('div', class_='box_con')
    book_name = main.find('div', class_='bookname').find('h1').text
    txt = main.find('div', id='content').text
    # p = txt.find('div', class_='read-content j_readContent').find_all('p')
    return book_name, txt, name


    pass


if __name__ == '__main__':
    # ss = input('要搜索的书名：')
    # new = TF.transformation_quote(ss)
    # url = 'https://www.qidian.com/search?kw=%s' % new
    # # print(url)
    # html = get_xs_text(url,0)  # 通过点击不同的链接得到不同的num
    #
    # # with open('html.txt', 'w', encoding='utf8') as f:
    #     f.write(html)
    url = 'https://www.xxbiquge.com/48_48573/2519266.html'
    book_name, txt, name = get_xs_text(url)
    print(book_name, txt, name)
