# 链接：https://blog.csdn.net/weixin_43343144/article/details/87901268

inkExtractor参数大全：
allow：接收一个正则表达式或一个正则表达式列表，提取绝对url于正则表达式匹配的链接，如果该参数为空，默认全部提取。

deny：接收一个正则表达式或一个正则表达式列表，与allow相反，排除绝对url于正则表达式匹配的链接，换句话说，就是凡是跟正则表达式能匹配上的全部不提取。

allow_domains：接收一个域名或一个域名列表，提取到指定域的链接。

deny_domains：和allow_doains相反，拒绝一个域名或一个域名列表，提取除被deny掉的所有匹配url。

restrict_xpaths：接收一个xpath表达式或一个xpath表达式列表，提取xpath表达式选中区域下的链接。

restrict_css：这参数和restrict_xpaths参数经常能用到，所以同学必须掌握

tags：接收一个标签（字符串）或一个标签列表，提取指定标签内的链接，默认为tags=（‘a’，‘area’）

attrs：接收一个属性（字符串）或者一个属性列表，提取指定的属性内的链接，默认为attrs=（‘href’，），示例，按照这个中提取方法的话，这个页面上的某些标签的属性都会被提取出来，如下例所示，这个页面的a标签的href属性值都被提取到了

process_value (callable) ：它接收来自扫描标签和属性提取每个值, 可以修改该值, 并返回一个新的, 或返回 None 完全忽略链接的功能｡如果没有给出, process_value 默认是 lambda x: x｡

cononicalize=(boolean) 规范化每个提取的url（使用w3lib.url.canonicalize_url）。默认为True。

unique=(boolean) 是否应对提取的链接应用重复过滤。

 

务必注意：提取css、jpg、png、js等有些链接的时候,process_value函数收到后给过滤了！所有link提取的值都会经过process_value这个函数,如果这个函数没指定,默认为lambda x: x
 LinkExtractor中allow正则表达式必须是没有被过滤的链接，否则返回来会是空（css、jpg、png、js文件类链接process_value函数过滤之后，返回来都是空列表）


# 强大之处慢慢体会：
# 可以自己定义、过滤、处理链接
# 配合 allow：接收一个正则表达式或一个正则表达式列表，提取绝对url于正则表达式匹配的链接，如果该参数为空，默认全部提取。
#      process_links：过滤处理链接

实例参见localhtml项目  