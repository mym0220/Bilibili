import os
import json
import shutil
from lxml import etree

# python os.path模块
'''
os.path.abspath(path) #返回绝对路径
os.path.basename(path) #返回文件名
os.path.commonprefix(list) #返回list(多个路径)中，所有path共有的最长的路径。
os.path.dirname(path) #返回文件路径
os.path.exists(path)  #路径存在则返回True,路径损坏返回False
os.path.lexists  #路径存在则返回True,路径损坏也返回True
os.path.expanduser(path)  #把path中包含的"~"和"~user"转换成用户目录
os.path.expandvars(path)  #根据环境变量的值替换path中包含的”$name”和”${name}”
os.path.getatime(path)  #返回最后一次进入此path的时间。
os.path.getmtime(path)  #返回在此path下最后一次修改的时间。
os.path.getctime(path)  #返回path的大小
os.path.getsize(path)  #返回文件大小，如果文件不存在就返回错误
os.path.isabs(path)  #判断是否为绝对路径
os.path.isfile(path)  #判断路径是否为文件
os.path.isdir(path)  #判断路径是否为目录
os.path.islink(path)  #判断路径是否为链接
os.path.ismount(path)  #判断路径是否为挂载点（）
os.path.join(path1[, path2[, ...]])  #把目录和文件名合成一个路径
os.path.normcase(path)  #转换path的大小写和斜杠
os.path.normpath(path)  #规范path字符串形式
os.path.realpath(path)  #返回path的真实路径
os.path.relpath(path[, start])  #从start开始计算相对路径
os.path.samefile(path1, path2)  #判断目录或文件是否相同
os.path.sameopenfile(fp1, fp2)  #判断fp1和fp2是否指向同一文件
os.path.samestat(stat1, stat2)  #判断stat tuple stat1和stat2是否指向同一个文件
os.path.split(path)  #把路径分割成dirname和basename，返回一个元组
os.path.splitdrive(path)   #一般用在windows下，返回驱动器名和路径组成的元组
os.path.splitext(path)  #分割路径，返回路径名和文件扩展名的元组
os.path.splitunc(path)  #把路径分割为加载点与文件
os.path.walk(path, visit, arg)  #遍历path，进入每个目录都调用visit函数，visit函数必须有
3个参数(arg, dirname, names)，dirname表示当前目录的目录名，names代表当前目录下的所有
文件名，args则为walk的第三个参数
os.path.supports_unicode_filenames  #设置是否支持unicode路径名
'''

# shutil model
'''
shutil.copyfile( src, dst)   #从源src复制到dst中去。 如果当前的dst已存在的话就会被覆盖掉
shutil.move( src, dst)  #移动文件或重命名
shutil.copymode( src, dst) #只是会复制其权限其他的东西是不会被复制的
shutil.copystat( src, dst) #复制权限、最后访问时间、最后修改时间
shutil.copy( src, dst)  #复制一个文件到一个文件或一个目录
shutil.copy2( src, dst)  #在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
shutil.copy2( src, dst)  #如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
shutil.copytree( olddir, newdir, True/Flase) #把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
shutil.rmtree( src )   #递归删除一个目录以及目录内的所有内容
'''

# 步骤
'''
打开1
name=提取文件名json
打开文件夹
如果0.blv-->1_name_1.mp4
如果1.blv-->1_name_2.mp4
如果2.blv-->1_name_3.mp4
打开2
name=提取文件名json
打开文件夹
如果0.blv-->1_name_1.mp4
如果1.blv-->1_name_2.mp4
如果2.blv-->1_name_3.mp4
'''


# D:\新建文件夹 (2)\24768482     D:\新建文件夹
def get_video(path, name, seris, dstfile):  # path=D:\24768482\1 || dstfile=操作系统_清华大学(向勇、陈渝)
    file_list = os.listdir('.')  # ['entry.json', 'lua.flv720.bili2api.64']
    for file_name in file_list:
        abs_path = os.path.join(path, file_name)  # abs_path = D:\6538245\1\entry.json
        if os.path.isdir(abs_path):  # 如果是文件夹
            os.chdir(abs_path)  # 进入 D:\6538245\2\lua.flv.bili2api.80
            for i in range(int(len(os.listdir(abs_path))/2)+2):
                old_name = str(i) + '.blv'
                if os.path.exists(old_name):
                    if clear_name == 'Y':
                        new_name = str(seris) + '_' + str(i) + ' ' + name + '.mp4'  # new_name='1_0  1.2 什么是操作系统.mp4'
                    else:
                        new_name = name + '.mp4'
                    os.renames(old_name, new_name)
                    print('正在重命名 %s ----> %s ...' % (old_name, new_name))
                    move_file(os.path.abspath(new_name), os.path.join(os.path.join(path2, dstfile), new_name))


def move_file(srcfile,
              dstfile):  # scrfile='D:\6538245\1\lua.flv.bili2api.80\1_0  1.2 什么是操作系统.mp4' dstfile='D:\操作系统_清华大学(向勇、陈渝)\1_0  1.2 什么是操作系统.mp4'
    path_dir, name = os.path.split(dstfile)  # 分离文件名和路径 path_dir=D:\操作系统_清华大学(向勇、陈渝) name=1_0  1.2 什么是操作系统.mp4
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)  # 创建路径
    shutil.move(srcfile, dstfile)  # 移动文件
    print('正在移动 %s ----> %s ...' % (name, path_dir))
    return path_dir


def get_danmaku(path, name, path_dir, n):
    if os.path.exists(os.path.join(path, 'danmaku.xml')):
        with open(os.path.join(path, 'danmaku.xml'), 'r', encoding='utf8') as f:
            file = f.read()
        element = etree.HTML(file.encode('utf8'))
        content = element.xpath('//d/text()')
        danmaku_file = os.path.join(path_dir)
        if not os.path.exists(danmaku_file):
            os.mkdir(danmaku_file)
        with open(os.path.join(danmaku_file, '弹幕.txt'), 'a', encoding='utf8') as f1:
            f1.write('-' * 5 + name + '-' * 5 + '\n')
            for con in content:
                f1.write(con + '\n')
            f1.write('\n' * 3)
        print('第%s集弹幕装填完毕...' % n)
        print('\n')


def main(path):
    remove = True
    n = max(list(map(lambda x: int(x), os.listdir(path))))  # n=最大文件夹int
    os.chdir(path)  # 进入D:\15123338
    for i in range(1, n + 1):
        try:
            os.chdir(str(i))  # 进入D:\15123338\1
            path_3 = os.getcwd()  # path_3=D:\15123338\1
            try:
                with open('entry.json', 'r', encoding='utf8') as f:
                    file = f.read()
                    name = json.loads(file)['page_data']['part']  # name = 1.2 什么是操作系统
                    dstfile = json.loads(file)['title']  # dstfile = 操作系统_清华大学(向勇、陈渝)
                get_video(path_3, name=name, seris=i, dstfile=dstfile)
                get_danmaku(path_3, name, os.path.join(path2, dstfile), i)
            except:
                remove = False
                print('处理第 %s 集出现错误!\n' % i)
            finally:
                os.chdir(path)
        except:
            pass

    if delete == 'Y':
        try:
            if remove:
                shutil.rmtree(path)
                print('已删除文件夹 %s .' % path)
        except:
            print('已清空文件夹 %s !' % path)


if __name__ == '__main__':
    print('-' * 5 + '此程序仅用于整理B站视频,技术受限,并不能合并分段视频.请勿用作其他商业用途.' + '-' * 5)
    print('*' * 5 + '程序作者:饮冰十年_难凉热血  有问题请联系QQ:821346679' + '*' * 5)
    print('')
    print(r'手机缓存好之后一般在 [Android\data\tv.danmaku.bili\download] 里面.')
    while True:
        print('\n')
        try:
            path = input('请输入源地址,例如(D:\\24329135):')
            clear_name = input('是否需要重新整理文件名?(Y/N):').upper()
            delete = input('移动完成后是否删除源文件夹及其所有文件?(Y/N):').upper()
            path2 = input('请输入整理后地址,例如(D:\\video):')
            if path2[-1] == ':':
                path2 = path2 + '\\'
            print('\n\n')
            main(path)
        except:
            print('输入有误或文件格式异常,请检查后重新输入!')
    # os.remove(r'D:\24329135')
    # print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
