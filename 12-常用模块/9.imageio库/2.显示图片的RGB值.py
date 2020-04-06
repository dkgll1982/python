import imageio
import numpy

numpy.set_printoptions(threshold=numpy.inf) #打印数组所有元素
    
im = imageio.imread(r"images\python.PNG")
print(im.shape)
print(im[:, :, :, ])