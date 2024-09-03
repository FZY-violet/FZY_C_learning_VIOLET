import numpy as np  
import matplotlib.pyplot as plt  
import cv2  
  
# 假设你有一个二维数组，代表高度图（例如从某个函数计算得到的）  
# 这里我们创建一个简单的示例数组  
x = np.linspace(-5, 5, 400)  
y = np.linspace(-5, 5, 400)  
x, y = np.meshgrid(x, y)  
z = np.sin(np.sqrt(x**2 + y**2))  # 示例函数  
  
# 使用matplotlib绘制等高线图  
fig, ax = plt.subplots()  
contour = ax.contourf(x, y, z, 50, cmap='viridis')  # 50表示等高线的数量，cmap是颜色映射  
fig.colorbar(contour)  # 添加颜色条  
  
# 保存图像为文件  
plt.savefig('contour_plot.png', bbox_inches='tight', pad_inches=0)  
  
# 使用OpenCV读取并显示图像  
contour_image = cv2.imread('contour_plot.png')  
cv2.imshow('等高线图', contour_image)  
cv2.waitKey(0)  
cv2.destroyAllWindows()