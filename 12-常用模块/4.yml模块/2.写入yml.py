import os
from ruamel import yaml

curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curpath, "caps.yaml")

# 作者：上海-悠悠 QQ交流群：330467341

# 将字典写入到yaml
desired_caps = {
                'platformName': 'Android',
                'platformVersion': '7.0',
                'deviceName': 'A5RNW18316011440',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'automationName': 'Uiautomator2',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:tools',
                                  'data':{
                                      'username':'alex',
                                      'pwd':'123445',
                                      'url':'jczl.giscloud.com',
                                      'sub':{
                                          'books':'python cookbook',
                                          'aihao':'skitboard',
                                          'reduce':'prrogram'
                                      }
                                  }}
                }

# 写入到yaml文件
with open(yamlpath, "w", encoding="utf-8") as f:
    yaml.dump(desired_caps, f, Dumper=yaml.RoundTripDumper)