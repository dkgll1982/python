import argparse
#参考链接：https://cloud.tencent.com/developer/section/1370514
#参考链接：https://www.cnblogs.com/sherlockChen/p/8245512.html

def main():
    #创建解析器
    parser = argparse.ArgumentParser(description="Demo of argparse")
    #添加参数
    parser.add_argument('-n','--name', default=' Li ',help='this is 姓名')
    parser.add_argument('-a','--age', type=int, default='20',help='this is 年龄')
    parser.add_argument('-s','--sex', 
                        default='unkown', 
                        required=True, 
                        choices=['man', 'woman','unkown'],
                        help='this is 性别')
    #parse_args()如果不带任何参数，会自动从sys.argv中确定命令行参数
    #args = parser.parse_args()
    #解析参数
    args = parser.parse_args(['--n','dkgll','--s','man'])
    print(args)
    name = args.name
    age = args.age
    sex = args.sex
    print('Hello {}  {}  {}'.format(name,age,sex))

if __name__ == '__main__':
    main()
