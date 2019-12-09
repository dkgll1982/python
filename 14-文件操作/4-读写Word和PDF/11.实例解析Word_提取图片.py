#参考链接：https://blog.csdn.net/qq_15969343/article/details/81673970
#功能：Python提取Word中的图片
'''
===========================================
  @author:  renjiaxin
  @time:    2018/8/9 0009   10:00
===========================================
'''
 
import zipfile
import os
import shutil 

def word2pic(path, zip_path, tmp_path, store_path):
    '''
    :param path:源文件
    :param zip_path:docx重命名为zip
    :param tmp_path:中转图片文件夹
    :param store_path:最后保存结果的文件夹（需要手动创建）
    :return:
    '''
    # 将docx文件重命名为zip文件
    os.rename(path, zip_path)
    # 进行解压
    f = zipfile.ZipFile(zip_path, 'r')
    # 将图片提取并保存
    for file in f.namelist():
        f.extract(file, tmp_path)
    # 释放该zip文件
    f.close()

    # 将docx文件从zip还原为docx
    os.rename(zip_path, path)
    # 得到缓存文件夹中图片列表
    pic = os.listdir(os.path.join(tmp_path, 'word/media'))

    # 将图片复制到最终的文件夹中
    for i in pic:
        # 根据word的路径生成图片的名称
        new_name = path.replace('\\', '_')
        new_name = new_name.replace(':', '') + '_' + i
        shutil.copy(os.path.join(tmp_path + '/word/media', i), os.path.join(store_path, new_name))

    # 删除缓冲文件夹中的文件，用以存储下一次的文件
    for i in os.listdir(tmp_path):
        # 如果是文件夹则删除
        if os.path.isdir(os.path.join(tmp_path, i)):
            shutil.rmtree(os.path.join(tmp_path, i))

if __name__ == '__main__':
    # 源文件
    path = r'backup\word\测试.docx'
    # docx重命名为zip
    zip_path = r'backup\word\log.zip'
    # 中转图片文件夹
    tmp_path = r'backup\word\tmp'
    # 最后保存结果的文件夹
    store_path = r'backup\word'
    m = word2pic(path, zip_path, tmp_path, store_path)