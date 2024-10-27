import cv2
import numpy as np

# 初始化摄像头
cap = cv2.VideoCapture(0)

while True:
    # 捕获每一帧
    ret, frame = cap.read()
    if not ret:
        break

    # 转换帧到HSV颜色空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 定义红色的HSV范围（可根据激光指示器颜色进行调整）
    lower_red = np.array([160, 100, 100])
    upper_red = np.array([179, 255, 255])

    # 创建掩膜以检测红色
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.GaussianBlur(mask, (9, 9), 2)

    # 在掩膜中查找轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # 过滤掉较小的轮廓以避免误报
        if cv2.contourArea(contour) > 100:
            (x, y), radius = cv2.minEnclosingCircle(contour)
            if radius > 5:  # 确保半径适合检测
                # 在检测到的激光点上画一个圆
                center = (int(x), int(y))
                cv2.circle(frame, center, int(radius), (0, 255, 0), 2)
                # 在圆的旁边显示坐标
                cv2.putText(frame, f"({int(x)}, {int(y)})", (int(x) + 10, int(y) - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # 显示视频流
    cv2.imshow("Laser Pointer Detection", frame)

    # 按'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()
