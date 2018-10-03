import os
import json
import shutil
from lxml import etree


class BiliDir:
    def __init__(self, srcpath, dstpath='D:\\', delete='Y'):  # D:\新建文件夹 (2)\24768482 || D:\
        self.srcpath = srcpath
        self.dstpath = dstpath
        self.delete = delete
        self.remove = True

    def start(self):
        n = max(list(map(lambda x: int(x), os.listdir(self.srcpath))))  # n=最大文件夹int
        os.chdir(self.srcpath)  # 进入D:\15123338
        for i in range(1, n + 1):
            try:
                os.chdir(str(i))  # 进入D:\15123338\1
                path = os.getcwd()  # path=D:\15123338\1
                with open('entry.json', 'r', encoding='utf8') as f:
                    file = f.read()
                    name = json.loads(file)['page_data']['part']  # name = 1.2 什么是操作系统
                    dir_name = json.loads(file)['title']  # 操作系统_清华大学(向勇、陈渝)
                self.__get_video(path, name, dir_name, i)
                self.__get_danmaku(path, name, os.path.join(self.dstpath, dir_name), i)

            except:
                self.remove = False
                print('处理第 %s 集出现错误!\n' % i)

            finally:
                os.chdir(self.srcpath)

        if self.remove:
            try:
                shutil.rmtree(self.srcpath)
                print('已删除文件夹 %s .' % self.srcpath)
            except:
                print('已清空文件夹 %s !' % self.srcpath)


    def __get_video(self, path, name, dir_name, seris):
        file_list = os.listdir('.')  # ['entry.json', 'lua.flv720.bili2api.64']

        for file_name in file_list:
            abs_path = os.path.join(path, file_name)  # abs_path = D:\6538245\1\entry.json

            if os.path.isdir(abs_path):  # 如果是文件夹
                os.chdir(abs_path)  # 进入 D:\6538245\2\lua.flv.bili2api.80
                for i in range(int(len(os.listdir(abs_path)) / 2) + 2):
                    old_name = str(i) + '.blv'
                    if os.path.exists(old_name):
                        new_name = str(seris) + '_' + str(i) + ' ' + name + '.mp4'  # new_name='1_0  1.2 什么是操作系统.mp4'
                        os.renames(old_name, new_name)
                        print('正在重命名 %s ----> %s ...' % (old_name, new_name))
                        self.__move_file(os.path.abspath(new_name),
                                         os.path.join(os.path.join(self.dstpath, dir_name), new_name))

    def __move_file(self, srcfile,
                    dstfile):  # scrfile='D:\6538245\1\lua.flv.bili2api.80\1_0  1.2 什么是操作系统.mp4' dstfile='D:\操作系统_清华大学(向勇、陈渝)\1_0  1.2 什么是操作系统.mp4'
        path_dir, name = os.path.split(dstfile)  # 分离文件名和路径 path_dir=D:\操作系统_清华大学(向勇、陈渝) name=1_0  1.2 什么是操作系统.mp4
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)  # 创建路径

        try:
            shutil.move(srcfile, dstfile)  # 移动文件
            print('正在移动 %s ----> %s ...' % (name, path_dir))
        except FileNotFoundError:
            print('文件名冲突，文件以移动至源文件夹。')
            shutil.move(srcfile, os.path.join(self.srcpath, name))  # 移动文件
            print('正在移动 %s ----> %s ...' % (name, self.srcpath))


    def __get_danmaku(self, path, name, path_dir, n):  # path_dir = D:\操作系统_清华大学(向勇、陈渝)
        if os.path.exists(os.path.join(path, 'danmaku.xml')):
            with open(os.path.join(path, 'danmaku.xml'), 'r', encoding='utf8') as f:
                file = f.read()
            element = etree.HTML(file.encode('utf8'))
            content = element.xpath('//d/text()')

            if not os.path.exists(path_dir):
                os.mkdir(path_dir)

            try:
                with open(os.path.join(path_dir, '弹幕.txt'), 'a', encoding='utf8') as f1:
                    f1.write('-' * 5 + name + '-' * 5 + '\n')
                    for con in content:
                        f1.write(con + '\n')
                    f1.write('\n' * 3)
                print('第%s集弹幕装填完毕...\n' % n)

            except FileNotFoundError:
                if n == 1:
                    print('文件名冲突，无法在该文件夹创建弹幕...\n\n\n')
                with open(os.path.join(self.srcpath, '弹幕.txt'), 'a', encoding='utf8') as f1:
                    f1.write('-' * 5 + name + '-' * 5 + '\n')
                    for con in content:
                        f1.write(con + '\n')
                    f1.write('\n' * 3)
                print('第%s集弹幕装填完毕...\n' % n)


if __name__ == '__main__':
    bili = BiliDir('D:\\')
    bili.start()
