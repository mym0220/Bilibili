import os
import shutil
import pymongo

def get_file(path):
    os.chdir(path)  # 进入'D:\PanDownload\D033.刘润5分钟商学院实战（第二季）'

    music_dir = os.path.split(path)[-1]
    if not os.path.exists(music_dir):
        os.mkdir(music_dir)
    if not os.path.exists(music_dir+'photo'):
        os.mkdir(music_dir+'photo')

    dir_list = os.listdir(path)  # ['2017.10', '2017.11', '2017.12', '2018.01']
    for dir1 in dir_list:  # '2017.10'
        if dir1 != 'music' and dir1 != 'photo':
            os.chdir(dir1)  # 进入'2017.10'
            file_list = os.listdir(os.getcwd())  # ['lr1028.mp3','lr1028开学.mp3','lr1028新一季开学典礼.jpg']
            for file in file_list:  # 'lr1028.mp3'
                tail_name = os.path.splitext(file)[-1].lower()
                if tail_name == '.mp3' or tail_name == '.m4a':
                    try:
                        shutil.move(file, os.path.join(path, 'music'))
                        print('moving to music...')
                    except:
                        print('move music %s failed!' % file)
                if tail_name == '.jpg' or tail_name == '.png':
                    try:
                        shutil.move(file, os.path.join(path, 'photo'))
                        print('moving to photo... \n')
                    except:
                        print('move photo %s failed! \n' % file)

            # 清空一个文件夹之后
            try:
                if not os.listdir(os.getcwd()):
                    os.chdir(path)  # 进入'D:\PanDownload\D033.刘润5分钟商学院实战（第二季）'
                    shutil.rmtree(os.path.abspath(dir1))
                os.chdir(path)
            except:
                os.chdir(path)


def main(path):
    get_file(path)


if __name__ == '__main__':
    path = 'D:\PanDownload\D039.MXJ马徐俊~新知报告'
    main(path)
