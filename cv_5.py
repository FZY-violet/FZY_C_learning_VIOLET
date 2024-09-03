import cv2  
import numpy as np  
import matplotlib.pyplot as plt  
  
# 读取图像文件  
image_path = r'C:\Users\HP\Pictures\Screenshots\微信图片_20240316125218.jpg' 
color_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # 读取为灰度图像  
  
# 假设灰度值代表光强，直接使用灰度值作为光强数据  
intensity_data = color_image.astype(float)  # 确保数据类型是浮点数，方便后续处理  
  
# 如果需要，可以对光强数据进行归一化或其他处理  
# intensity_data = (intensity_data - intensity_data.min()) / (intensity_data.max() - intensity_data.min())  
  
# 绘制等高线图  
plt.figure(figsize=(8, 6))  
plt.contourf(intensity_data, 50, cmap='gray')  
plt.colorbar(label='光强')  
plt.title('光强等高线图')  
plt.xlabel('X轴')  
plt.ylabel('Y轴')  
  
# 显示图形  
plt.show()