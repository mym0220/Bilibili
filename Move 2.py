import os
import shutil
import zipfile


class Move:
    def __init__(self, path):  # path='F:\---009_Python 定向爬虫入门'
        self.path = path

    def get_file(self, to_path='F:\Get'):
        global music_dir
        global photo_dir
        name_get = os.path.join(to_path, os.path.split(self.path)[-1])
        music_dir = os.path.join(name_get, 'music')
        photo_dir = os.path.join(name_get, 'photo')
        os.mkdir(name_get)
        os.mkdir(music_dir)
        os.mkdir(photo_dir)
        self.__get_all_dir(self.path)

    def unzip(self, to_path='D:\Python'):  # path = r'F:\新建文件夹\---009_Python 定向爬虫入门'
        files_list = os.listdir(self.path)
        tail_name = os.path.split(self.path)[-1]
        new_path = os.path.join(to_path, tail_name)

        for zip_file in files_list:
            abs_path = os.path.join(self.path, zip_file)
            if not os.path.isdir(abs_path):
                if os.path.splitext(zip_file)[-1] in ['.zip']:
                    z = zipfile.ZipFile(abs_path, 'r')
                    z.extractall(path=new_path)
                    print('正在解压 --> %s' % os.path.split(abs_path)[-1])

        self.__rename(new_path)

    def __get_all_dir(self, path):
        files_list = os.listdir(path)

        for file_name in files_list:
            abs_path = os.path.join(path, file_name)  # 判断是否是路径(用绝对路径)

            if os.path.isdir(abs_path):
                self.__get_all_dir(abs_path)

            else:
                self.__move_get(abs_path)

    def __move_get(self, abs_path):
        name = os.path.split(abs_path)[-1]
        tail_name = os.path.splitext(abs_path)[-1].lower()
        if tail_name in ['.mp3', '.m4a']:
            try:
                shutil.move(abs_path, music_dir)
                print('正在移动 %s \n' % name)
            except:
                print('移动 %s 失败!\n' % abs_path)
        if tail_name in ['.jpg', '.png', '.pdf', '.doc']:
            try:
                shutil.move(abs_path, photo_dir)
                print('正在移动 %s \n' % name)
            except:
                print('移动 %s 失败!\n' % abs_path)

    def __rename(self, new_path):  # new_path = r'D:\Python\---009_Python 定向爬虫入门'
        files_list = os.listdir(new_path)
        for file_name in files_list:
            abs_path = os.path.join(new_path, file_name)

            if os.path.isdir(abs_path):
                try:
                    right_name = file_name.encode('cp437').decode('gbk')
                    os.rename(abs_path, os.path.join(new_path, right_name))
                    print('正在重命名 --> %s' % os.path.split(right_name)[-1])
                    abs_path = os.path.join(new_path, right_name)
                except:
                    pass
                self.__rename(abs_path)

            else:
                try:
                    right_name = file_name.encode('cp437').decode('gbk')
                    os.rename(abs_path, os.path.join(new_path, right_name))
                    print('正在重命名 --> %s' % os.path.split(right_name)[-1])
                except:
                    pass

    def mv_file(self, path):
        files_list = os.listdir(path)

        for file_name in files_list:
            abs_path = os.path.join(path, file_name)  # 判断是否是路径(用绝对路径)

            if os.path.isdir(abs_path):
                self.__get_all_dir(abs_path)

            else:
                name = os.path.split(abs_path)[-1]
                tail_name = os.path.splitext(abs_path)[-1].lower()
                if tail_name in ['.mp4']:
                    try:
                        shutil.move(abs_path, self.path)
                        print('正在移动 %s \n' % name)
                    except:
                        print('移动 %s 失败!\n' % abs_path)


if __name__ == '__main__':
    loc = ''
    m = Move(loc)
    # m.get_file()
    # m.unzip()
    m.mv_file(loc)
