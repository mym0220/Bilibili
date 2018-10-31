import os
import shutil
import zipfile


def main(path):
    global music_dir
    global photo_dir
    name = os.path.join('F:\Get', os.path.split(path)[-1])
    music_dir = os.path.join(name, 'music')
    photo_dir = os.path.join(name, 'photo')
    os.mkdir(name)
    os.mkdir(music_dir)
    os.mkdir(photo_dir)
    get_all_dir(path)


def get_all_dir(path):
    files_list = os.listdir(path)

    for file_name in files_list:
        abs_path = os.path.join(path, file_name)  # 判断是否是路径(用绝对路径)

        if os.path.isdir(abs_path):
            get_all_dir(abs_path)

        else:
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
            if tail_name in ['.mp4']:
                try:
                    shutil.move(abs_path, mvdir)
                    print('正在移动 %s \n' % name)
                except:
                    print('移动 %s 失败!\n' % abs_path)


def unzip(path):  # path = r'F:\新建文件夹\---009_Python 定向爬虫入门'
    files_list = os.listdir(path)
    tail_name = os.path.split(path)[-1]
    head_name = 'D:\Python'
    new_path = os.path.join(head_name, tail_name)

    for zip_file in files_list:
        abs_path = os.path.join(path, zip_file)
        if not os.path.isdir(abs_path):
            if os.path.splitext(zip_file)[-1] in ['.zip']:
                z = zipfile.ZipFile(abs_path, 'r')
                z.extractall(path=new_path)
                print('正在解压 --> %s' % os.path.split(abs_path)[-1])

    rename(new_path)


def rename(new_path):  # new_path = r'D:\Python\---009_Python 定向爬虫入门'
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
            rename(abs_path)

        else:
            try:
                right_name = file_name.encode('cp437').decode('gbk')
                os.rename(abs_path, os.path.join(new_path, right_name))
                print('正在重命名 --> %s' % os.path.split(right_name)[-1])
            except:
                pass


if __name__ == '__main__':
    # rename('F:\新建文件夹\---009_Python 定向爬虫入门1')
    # rename(r'D:\新建文件夹\---009_Python 定向爬虫入门')
    # unzip(r'D:\Django+xadmin')
    mvdir = r'D:\Python\Django+xadmin\强力django+杀手级xadmin 打造上线标准的在线教育平台'
    get_all_dir(r'D:\Python\Django+xadmin\强力django+杀手级xadmin 打造上线标准的在线教育平台')
