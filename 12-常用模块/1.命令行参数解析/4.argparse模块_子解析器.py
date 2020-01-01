import argparse
#参考链接：https://www.cnblogs.com/wongbingming/p/10409919.html
                           
def main_single(name, args):
    print("name: ", name)
    print("args: ", args)
    print("I am main_single")

# create the top-level parser
parser = argparse.ArgumentParser(prog='PROG')

#dest=files，是说将命令行中，--file 的参数值赋值给变量files，你可以用args.files访问。
#action=append，由于我们会有指定多个文件的需求，那就指定多次--file ，argparse会将其放在一个list里。
#type=argparse.FileType('rb')，既然是指定文件，那么参数应该为路径，并指定打开模式为rb，
# 如果如果要取得文件内容，可以用 args.files[0].read()
parser.add_argument('--file', '-f', action='append',
                    dest='files',
                    help=('additional yaml configuration files to use'),
                    type=argparse.FileType('rb')) 

parser.add_argument("-g", "--gender", default='male',
                    choices=['male', 'female'],help='this is sex!!!')

# 添加一个子解析器
subparsers = parser.add_subparsers(help='sub-command help')

parser_single = subparsers.add_parser('single',help='run a single module')

# require=True，是说如果命令行指定了single解析器，就必须带上 --name 的参数。
parser_single.add_argument("--name", '-n', action="store",
                           help="module name to run",
                           required=True)

# 对single 子解析器添加 action 函数。
parser_single.set_defaults(action=('single', main_single))

args = parser.parse_args(['-f','backup\\test.txt','--gender', 'female', 'single','--name', 'ZhangSan'])

(name, functor) = args.action
if name in ["single"]:
    functor(name, args)

#取得文件内容，可以用 args.files[0].read()    
print('file content:%s'%args.files[0].read().decode('utf-8'))