import cv2  
import numpy as np  
  
# 读取图像  
image = cv2.imread(r'C:\Users\HP\Pictures\Screenshots\微信图片_20240316125218.jpg')  
  
# 设置文本内容和位置  
text = '3D Text'  
org = (50, 50)  # 文本原始位置  
font = cv2.FONT_HERSHEY_SIMPLEX  
fontScale = 1  
color = (255, 255, 255)  # 文本颜色  
thickness = 2  
  
# 绘制原始文本  
cv2.putText(image, text, org, font, fontScale, color, thickness, cv2.LINE_AA)  
  
# 计算阴影的位置和颜色  
shadow_offset = (5, 5)  # 阴影偏移量  
shadow_color = (128, 128, 128)  # 阴影颜色  
shadow_org = (org[0] + shadow_offset[0], org[1] + shadow_offset[1])  
  
# 绘制阴影文本  
cv2.putText(image, text, shadow_org, font, fontScale, shadow_color, thickness, cv2.LINE_AA)  
  
# 显示图像  
cv2.imshow('Pseudo 3D Text', image)  
cv2.waitKey(0)  
cv2.destroyAllWindows()