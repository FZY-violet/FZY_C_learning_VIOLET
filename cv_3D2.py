import cv2  
import numpy as np  
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt  
  
# 读取图像  
image = cv2.imread(r'C:\Users\HP\Pictures\Screenshots\微信图片_20240318184420.jpg', cv2.IMREAD_GRAYSCALE)  
  
# 确保图像不是None  
if image is None:  
    print("无法读取图片")  
    exit()  
  
# 将图像数据归一化到0-1范围  
image_normalized = image / 255.0  
  
# 创建高度图，这里简单地将图像亮度映射为高度  
# 假设最大高度为图像的最大值  
max_height = image_normalized.max()  
height_map = (image_normalized * max_height).astype(np.float32)  
  
# 创建Matplotlib的3D图形  
fig = plt.figure()  
ax = fig.add_subplot(111, projection='3d')  
  
# X和Y坐标直接使用图像的行列索引  
X, Y = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))  
  
# Z是高度图，已经是二维的，不需要展平  
Z = height_map  
  
# 绘制三维曲面  
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='gray', linewidth=0, antialiased=False)  
  
# 设置图形的标题和坐标轴标签  
ax.set_title('基于图像亮度的三维高度图')  
ax.set_xlabel('X')  
ax.set_ylabel('Y')  
ax.set_zlabel('Z (Height)')  
  
# 显示图形  
plt.show()