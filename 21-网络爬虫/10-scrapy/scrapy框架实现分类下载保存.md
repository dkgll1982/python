# 参考链接：https://blog.csdn.net/weixin_44750138/article/details/88432258?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.control

python—scrapy_Pipelines分类下载

此处以图片下载为例

1. items中添加images参数储存图片的相关信息…如：路径，下载的url，图片的效验码。
car_cat_name = scrapy.Field()  # 此处保存图片的类别
images = scrapy.Field()  # 储存图片的相关信息(如：路径，下载的url，图片的效验码)  需要额外定义
image_urls = scrapy.Field()  # image_urls里面储存图片的链接

2. 重写Pipleline方法 （1）.定义路径`# 当前目录
# 外层包一下，代表上一层目录
# os.path_join 拼接路径
self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
if not os.path.exists(self.path):
    os.mkdir(self.path)
else:
    print('文件夹已存在')`


（1）.创建图片所属类别的文件夹，以类别为文件名
def process_item(self, item, spider):

    # 此处传过来的是一个字典，需要取出来
    car_cat_name = item['car_cat_name']
    car_cat_url = item['car_cat_url']
    # 拼接文件路径与文件名
    car_cat_name_path = os.path.join(self.path, car_cat_name)
    # 判断是否存在，不存在则创建一个新的文件夹
    if not os.path.exists(car_cat_name_path):
        os.mkdir(car_cat_name_path)
    # 遍历图片的url
    for url in car_cat_url:
        # 以 _ 分割
        image_name = url.split('_')[-1]
        # 将分割后的字符串最后一个作为图片的名字，并下载图片
        request.urlretrieve(url, car_cat_name_path+'/' + image_name)
    return item


（2).重写路径与下载请求(类似模板，需要的时候有稍微改动，如：列表中的值遍历出来的对象，方法2 中储存路径后缀的名字，)
class CarImagesPipline(ImagesPipeline):

    # 会在请求前调用，需要用这个方法发起请求
    def get_media_requests(self, item, info):
        # 继承父类中的方法并重构，获取到了父类中的文件名其原方法为: full/%s.jpg(此处已经自定义.jpg方法，如需修改，请到其所指向的地方进行修改)
        request_objs = super(CarImagesPipline, self).get_media_requests(item, info)
        # 得到的是一个列表，需要进行遍历
        for request_obj in request_objs:
            request_obj.item = item  # 需要获取到文件中的item的值
        # 返回请求，该方法在原代码中作用是发起请求
        return request_objs

    # 在图片将要被存储的时候调用，在这里获取图片存储的路径
    def file_path(self, request, response=None, info=None):
        path = super(CarImagesPipline, self).file_path(request, response, info)
        car_cat_name = request.item.get('car_cat_name')  # 获取items.py中的car_cat_name(从网页获取到的类别名字)
        images_store = settings.IMAGES_STORE  # 获取路径
        car_cat_name_path = os.path.join(images_store, car_cat_name)  # 路径与名字组合为当前文件夹所在路径
        if not os.path.exists(car_cat_name_path):  # 判断是否存在该文件夹
            os.mkdir(car_cat_name_path)  # 不存在的话就创建一个
        images_name = path.replace('full/', '')  # 在重构该方法的时候原方法会自动将文件 存在full文件夹中
        images_path = os.path.join(car_cat_name_path, images_name)  # 拼接图片的储存路径出来
        return images_path  # 返回该路径

3. 修改settings.py文件
(1).修改ITEM_PIPELINES参数
1
ITEM_PIPELINES = {
    'Car.pipelines.CarImagesPipline': 1,
}


(2). 添加下载路径

IMAGES_STORE = os.path.join(os.path.dirname(os.path.dirname(__file__)),('images'))

！！！仅作参考