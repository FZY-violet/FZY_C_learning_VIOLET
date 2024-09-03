import cv2  
import numpy as np  
import matplotlib.pyplot as plt  
  
# 读取图片并转换为灰度图像  
image_path = r'C:\Users\HP\Pictures\Screenshots\微信图片_20240318184420.jpg'  
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # 确保是灰度图像  
  
# 如果图像不是灰度图像，则进行转换  
if image is None or len(image.shape) != 2:  
    image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)  
  
# 归一化光强数据到0-1范围，以便在热力图中正确显示  
intensity_map = (image - np.min(image)) / (np.max(image) - np.min(image))  
  
# 使用matplotlib来创建热力图  
plt.figure(figsize=(8, 6))  
plt.imshow(intensity_map, cmap='hot', interpolation='nearest')  # 使用'hot'颜色映射  
plt.colorbar(label='光强')  # 添加颜色条并标记  
plt.title('图片热力图')  # 设置图表标题  
plt.axis('off')  # 关闭坐标轴显示  
plt.show()  # 显示图表
