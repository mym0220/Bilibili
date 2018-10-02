import requests
import json, re, time
from requests.exceptions import RequestException
import os
import time

def get_page(page, keyword):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                          ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        url = 'https://api.bilibili.com/x/web-interface/search/type?jsonp=jsonp&&search_type=' \
              'video&highlight=1&keyword={}&page={}'.format(keyword, page)
        r = requests.get(url, headers)
        if r.status_code == 200:
            if page == 1:
                print('网址请求成功~')
            return r.text
        else:
            print(r.status_code)
    except RequestException:
        print('网址请求失败！')
        return None


def parse_page(html, keyword, detail, page, path):
    data = json.loads(html)
    results = data['data']['result']
    dir = os.path.join(path, 'detail')
    file = os.path.join(dir, keyword)  # D:\IMAGE\detail\keyword
    if not os.path.exists(dir):  # 创建D:\IMAGE\detail
        os.mkdir(dir)
    with open(file + '.txt', 'a', encoding='utf8') as f_s:
        f_s.write('-' * 10 + '第%s页' % page + '-' * 10 + '\n')

    if detail == 'N':
        print('\n正在下载详细信息...\n')
        for result in results:
            image_url = 'http:' + result['pic']
            video_url = result['arcurl']
            author = result['author']
            description = re.sub(r'\n', '', re.sub(r'\r\n', '', result['description']))
            title = re.sub('</em>', '', re.sub(r'<em class="keyword">', '', result[
                'title']))  # re.sub('<em class="keyword">[Pp]ython</em>','Python',result['title'])
            play_num = result['play']
            favorites = result['favorites']
            pubdate = time.strftime('%Y-%m-%d', time.localtime(result['pubdate']))
            senddate = time.strftime('%Y-%m-%d', time.localtime(result['senddate']))

            with open(file + '.txt', 'a', encoding='utf8') as f:

                f.write('标题\t: {}'.format(title) + '\n')
                f.write('作者\t: {}'.format(author) + '\n')
                f.write('详情\t: {}'.format(description) + '\n')
                f.write('点赞数\t: {}'.format(favorites) + '\n')
                f.write('播放数\t: {}'.format(play_num) + '\n')
                f.write('发布时间\t: {}'.format(pubdate) + '\n')
                f.write('更新时间\t: {}'.format(senddate) + '\n')
                f.write('封面地址\t: {}'.format(image_url) + '\n')
                f.write('视频地址\t: {}'.format(video_url) + '\n' * 3)
    elif detail == 'Y':
        print('\n正在下载标题...\n')
        for result in results:
            title = re.sub('</em>', '', re.sub(r'<em class="keyword">', '', result[
                'title']))  # re.sub('<em class="keyword">[Pp]ython</em>','Python',result['title'])
            with open(file + '.txt', 'a', encoding='utf8') as f:
                f.write(title+ '\n' * 3)



def image_download(html, path, keyword):
    data = json.loads(html)
    results = data['data']['result']
    dir = os.path.join(os.path.join(path, 'images'), keyword)  # 创建D:\IMAGE\images\keyword
    if not os.path.exists(os.path.join(path, 'images')):       # 创建D:\IMAGE\images
        os.mkdir(os.path.join(path, 'images'))
    if not os.path.exists(dir):
        os.mkdir(dir)
    for result in results:
        image_url = 'http:' + result['pic']
        title = re.sub('</em>', '', re.sub(r'<em class="keyword">', '', result[
            'title']))  # re.sub('<em class="keyword">[Pp]ython</em>','Python',result['title'])
        file = os.path.join(dir, title + '.png')
        try:
            with open(file, 'wb') as f1:
                f1.write(requests.get(image_url).content)
                print('正在下载图片 ---> %s'%title)
        except:
            pass


def main(keyword, page, image, path, detail):
    print('\n\n')
    for page in range(1, page + 1):
        html = get_page(page=page, keyword=keyword)
        parse_page(html=html, keyword=keyword, page=page, path=path, detail=detail)
        if image == 'Y':
            image_download(html=html, path=path, keyword=keyword)


if __name__ == '__main__':
    print('如果输入有误请重新打开程序...')
    print('如果需要结束请直接关闭程序...')
    while True:
        try:
            print('\n\n')
            time.sleep(1)
            keyword = input('请输入想要搜索的内容:')
            page = int(input('想要搜索多少页数据？(每页20条/最多50页):'))
            image = input('是否下载封面图片?(Y/N):').upper()
            detail = input('只下载标题?(Y/N):').upper()
            path = input('文件下载到哪里(地址类似-->D:\DOWNLOAD):')
            main(keyword, page, image, path, detail)
        except:
            print('输入有误,请重新输入。\n\n')

    # if image == 'Y' or 'y':
    #   pass
