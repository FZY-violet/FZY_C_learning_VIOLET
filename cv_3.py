import cv2  
import matplotlib.pyplot as plt  
  
# 读取图像  
image = cv2.imread(r'C:\Users\HP\Pictures\Screenshots\微信图片_20240316125218.jpg', 0)  
  
# 计算直方图  
hist = cv2.calcHist([image], [0], None, [256], [0, 256])  
  
# 绘制直方图  
plt.figure(figsize=(10, 6))  
plt.plot(hist, color='blue')  
plt.xlim([0, 256])  
plt.title('Intensity Histogram')  
plt.xlabel('Pixel Intensity')  
plt.ylabel('Frequency')  
plt.grid(True)  
plt.show()