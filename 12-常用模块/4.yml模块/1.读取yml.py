
# 参考链接：http://www.lemfix.com/topics/375
from ruamel.yaml import YAML
import os 
curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curpath, "人资1.yaml") 

# 第一步: 创建YAML对象
yaml = YAML(typ='safe')

# typ: 选择解析yaml的方式
#  'rt'/None -> RoundTripLoader/RoundTripDumper(默认)
#  'safe'    -> SafeLoader/SafeDumper,
#  'unsafe'  -> normal/unsafe Loader/Dumper
#  'base'    -> baseloader

# 第二步: 读取yaml格式的文件
with open(yamlpath, encoding='utf-8') as file:
    data = yaml.load(file)  # 为列表类型

print(f"data:\n{data}")
