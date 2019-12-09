import os
from ruamel import yaml

curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curpath, "caps.yaml")

def up_yml(ip_server):
    with open(yamlpath, encoding="utf-8") as f:
        # 使用ruamel.yaml库里面函数参数Loader=ruamel.yaml.RoundTripLoader和Dumper=ruamel.yaml.RoundTripDumper
        # 可以用来保持新生成的yaml文件的表现和输入文件一致
        content = yaml.load(f, Loader=yaml.RoundTripLoader)
        # 修改yml文件中的参数
        content['chromeOptions']['data']['sub']['books'] = 'mysql_host = {}'.format(ip_server)
    with open(yamlpath, 'w', encoding="utf-8") as nf:
        yaml.dump(content, nf, Dumper=yaml.RoundTripDumper)

if __name__ == '__main__':
    up_yml(ip_server='10.20.0.0')

#————————————————
#版权声明：本文为CSDN博主「哇葫芦娃」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/weixin_40342792/article/details/85260927