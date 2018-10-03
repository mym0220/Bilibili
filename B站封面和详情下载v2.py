import requests
import json, re
from requests.exceptions import RequestException
import os
import time
import xlwt


class Bili:

    def __init__(self, keyword, page):
        self.keyword = keyword  # 'python'
        self.page = page  # 10
        # 为什么不能再此处实例化 book 和 excel

    def excel(self, path='D:\Source\detail'):
        book = xlwt.Workbook()
        excel = book.add_sheet(self.keyword)

        first_row = ['序号', '标题', '作者', '详情', '点赞数',
                     '播放数', '发布时间', '更新时间', '视频地址']
        for i, first in enumerate(first_row):
            excel.write(0, i, first)

        for page_m in range(1, self.page + 1):
            self.__parse_page(page_m, self.__get_page(page_m), book, excel, path)

    def __get_page(self, page_m):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            }
            url = 'https://api.bilibili.com/x/web-interface/search/type?jsonp=jsonp&&search_type=' \
                  'video&highlight=1&keyword={}&page={}'.format(self.keyword, page_m)
            r = requests.get(url, headers)
            if r.status_code == 200:
                if page_m == 1:
                    print('Url requests success~')
                return r.text
            else:
                print(r.status_code)
        except RequestException:
            print('Url requests failed~')
            return None

    def __parse_page(self, page_m, html, book, excel, path):  # path = D:\\Source
        data = json.loads(html)
        results = data['data']['result']

        for num, result in enumerate(results, start=1):
            video_url = result['arcurl']
            author = result['author']
            description = re.sub(r'\n', '', re.sub(r'\r\n', '', result['description']))
            title = re.sub('</em>', '', re.sub(r'<em class="keyword">', '', result[
                'title']))  # re.sub('<em class="keyword">[Pp]ython</em>','Python',result['title'])
            play_num = result['play']
            favorites = result['favorites']
            pubdate = time.strftime('%Y-%m-%d', time.localtime(result['pubdate']))
            senddate = time.strftime('%Y-%m-%d', time.localtime(result['senddate']))

            row = num + (page_m - 1) * 20
            contents = [row, title, author, description, int(favorites), int(play_num),
                        pubdate, senddate, video_url]
            for col, content in enumerate(contents):
                excel.write(row, col, content)

        book.save(os.path.join(path, self.keyword + '.xls'))  # 已存在的excel为什么不会报错？会不会覆盖？
        print('Saved the %d page to excel success..' % page_m)

    def image(self, path='D:\Source\images'):
        image_dir = os.path.join(path, self.keyword)

        for page_img in range(1, self.page + 1):
            html = self.__get_page(page_img)
            data = json.loads(html)
            results = data['data']['result']
            if not os.path.exists(image_dir):
                os.mkdir(image_dir)

            print('\nNow downloading the %d images...' % page_img)
            for result in results:
                image_url = 'http:' + result['pic']
                title = re.sub('</em>', '', re.sub(r'<em class="keyword">', '', result[
                    'title']))  # re.sub('<em class="keyword">[Pp]ython</em>','Python',result['title'])

                file = os.path.join(image_dir, title + '.png')
                try:
                    with open(file, 'wb') as f1:
                        f1.write(requests.get(image_url).content)
                        print('Downloading image ---> %s' % title)
                except:
                    print('Failed in download image %s' % title)


if __name__ == '__main__':
    project = Bili(keyword='猫', page=50)
    project.excel()
    # project.image()
